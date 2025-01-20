# ------------------------------------
# DO NOT MODIFY THIS FILE
# NO IMPLEMENTATION NEEDED
# ------------------------------------
import sys
from elftools.elf import elffile as elf
from definitions import *
from rv32i import *
from structure import *
from riscvsim import *

# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
class ICACHE(object):
    def __init__(self):
        self.cache = {}
    
    def put(self, pc, inst):
        self.cache[pc] = inst
    
    def get(self, pc):
        return self.cache.get(pc)
# --------------------------------------------------------------




class PROGRAM(object):
    def __init__(self):
        # store instructions
        PROGRAM.icache = ICACHE()

    # load the binary program into the simulator
    def load_program(self, simulator:RISCVSIM, filename):
        self.sim = simulator
        try:
            fp = open(filename, "rb")
        except IOError:
            print("Error: Cannot open file")
            sys.exit(1)
        
        with fp:
            # parse the binary which is an ELF format file
            riscv_elf = elf.ELFFile(fp)

            # get header
            header = riscv_elf.header
            # make sure it's a 32-bit little-endian RISCV executable file
            e_ident = header['e_ident']
            if e_ident['EI_CLASS'] != 'ELFCLASS32':
                print("Error: Not a 32-bit ELF file")
                sys.exit(1)
            if e_ident['EI_DATA'] != 'ELFDATA2LSB':
                print("Error: Not a little-endian file")
                sys.exit(1)
            if header['e_machine'] != 'EM_RISCV' and header['e_machine'] != 243:
                print("Error: Not a RISCV file")
                sys.exit(1)
            if header['e_type'] != 'ET_EXEC':
                print("Error: Not an executable file")
                sys.exit(1)
            
            # where to start
            entry_point = WORD(header['e_entry'])

            # extract the instruction segment
            for seg in riscv_elf.iter_segments():
                addr = seg.header['p_vaddr']
                memsz = seg.header['p_memsz']
                # it should be a loadable segment
                if seg.header['p_type'] != 'PT_LOAD':
                    continue
                
                # check the objdump files
                if addr >= simulator.imem.start and addr + memsz < simulator.imem.end:
                    mem=simulator.imem
                elif addr >= simulator.dmem.start and addr + memsz < simulator.dmem.end:
                    mem=simulator.dmem
                else:
                    continue

                # store the instruction and data contents by word size
                for i in range(0, memsz, WORD_SIZE):
                    val = int.from_bytes(seg.data()[i:i+WORD_SIZE],byteorder='little')
                    #print('0x%08x' % val)
                    # init a memory write
                    mem.access(True, addr, val, M_XWR)
                    addr += WORD_SIZE
            return entry_point

    # pc is then where the ins stored in imem    
    @staticmethod
    def disassemble(pc, inst):
        pc = WORD(pc)   
        if inst == BUBBLE:
            decode = "BUBBLE"
            return decode
        elif inst == NOP:
            decode = "NOP"
            return decode
        
        opcode = INSTRUCTION.get_opcode(inst)
        if opcode == ILLEAGAL:
            decode = "(illegal)"
            PROGRAM.icache.put(pc, decode)
            return decode
        # get the instruction info
        inst_info = rv32i_t[opcode]
        # get the opcode string
        opcode_str = INSTRUCTION.get_opcode_str(opcode)
        # get operands
        rs1 = INSTRUCTION.get_rs1(inst)
        rs2 = INSTRUCTION.get_rs2(inst)
        rd = INSTRUCTION.get_rd(inst)
        # get immediate values
        imm_i = INSTRUCTION.get_imm_i(inst)
        imm_s = INSTRUCTION.get_imm_s(inst)
        imm_b = INSTRUCTION.get_imm_b(inst)
        imm_u = INSTRUCTION.get_imm_u(inst)
        imm_j = INSTRUCTION.get_imm_j(inst)
        # get type 
        inst_type = inst_info[IN_TYPE]
        type_val = ISA_TYPES[inst_type]
        match type_val:
            case 0: # R-type
                decode = "%-7s%s, %s, %s" % (opcode_str, registers[rd], registers[rs1], registers[rs2])
            case 1: # I-type
                decode = "%-7s%s, %s, %d" % (opcode_str, registers[rd], registers[rs1], SWORD(imm_i))
            case 2: # IL-type, load
                decode = "%-7s%s, %d(%s)" % (opcode_str, registers[rd], SWORD(imm_i), registers[rs1])
            case 3: # IJ-type, jalr
                decode = "%-7s%s, %s, %d" % (opcode_str, registers[rd], registers[rs1], SWORD(imm_i))
            case 4: # IS-type, shift
                decode = "%-7s%s, %s, %d" % (opcode_str, registers[rd], registers[rs1], SWORD(imm_i & 0x1f))
            case 6: # S-type
                decode = "%-7s%s, %d(%s)" % (opcode_str, registers[rs2], SWORD(imm_s), registers[rs1])
            case 7: # B-type
                decode = "%-7s%s, %s, 0x%08x" % (opcode_str, registers[rs1], registers[rs2], pc+SWORD(imm_b))
            case 8: # J-type
                decode = "%-7s%s, 0x%08x" % (opcode_str, registers[rd], pc+SWORD(imm_j))
            case 5: # U-type
                decode = "%-7s%s, 0x%05x" % (opcode_str, registers[rd], imm_u)
            case 9: # X-type
                return inst_info[IN_NAME]
            case _:
                decode = 'unknown'

        PROGRAM.icache.put(pc, decode)
        return decode
    
    def dump(self, simulator:RISCVSIM):
        illegal_cnt = 0
        for a in range(simulator.imem.start, simulator.imem.end, WORD_SIZE):
            ins, status = simulator.imem.access(True, a, 0, M_XRD)
            if not status:
                continue
            decoded = PROGRAM.disassemble(a, ins)
            if decoded != '(illegal)':
                print("0x%08x: %s" % (a, decoded))
            elif ins!=0:
                illegal_cnt += 1
                print("0x%08x: %08x %s" % (a, ins, "illegal instruction"))
        if illegal_cnt !=0:
            print("Illegal instructions: %d" % illegal_cnt)
        pass