from definitions import *
from structure import *




class RISCVSIM(object):

    # --------------------------------------------------------------
    # TASK--IMPLEMENTATION NEEDED
    # Guide:
    # Check the structure.py and definitions.py
    # Only 1 line is needed for each variable
    def __init__(self):
        # progam counter is a register
        self.pc =  REG(IMEM_START)
        # register files
        self.rf = RF()
        # instruction memory
        self.imem = MEM(IMEM_START,IMEM_SIZE,WORD_SIZE)
        # data memory
        self.dmem = MEM(DMEM_START,DMEM_SIZE,WORD_SIZE)
    # --------------------------------------------------------------
    

    def run(self, entry_point):
        SIMULATOR.run(self, entry_point)


class SIMULATOR(object):
    # simulator will work as the riscv platform
    @staticmethod
    def run(simulator:RISCVSIM, entry_point):
        SIMULATOR.core = simulator

        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part A
        # Guide:
        # Set the program counter
        # Check where is the register binds to
        # Only 1 line is needed
        SIMULATOR.core.pc.write(entry_point)
        # --------------------------------------------------------------

        while True:
            status = SIMULATOR.cycle()

            # --------------------------------------------------------------
            # TASK--IMPLEMENTATION NEEDED
            # Part A
            # Guide:
            # update the stats, you used it in Task 2
            # update cycle and instruction count here
            # 2 lines are enough
            STATS.cycle +=1 # add cycle count
            STATS.icount +=1 # add excuted instructions count
            
            # --------------------------------------------------------------

            if not status == EXC_NONE:
                pc = SIMULATOR.core.pc.read()
                if status == EXC_EBREAK:
                    print("[ebreak] Stop Simulation")
                else:
                    print("Exception at 0x%08x: " % pc)
                    print(EXC_MSG[status])
                break
            
        # deal with the exceptions if any
        print("Simulation Finished")
        
        SIMULATOR.core.rf.dump()

        

        
    # return status
    @staticmethod
    def cycle():
        
        pc, inst, status = SIMULATOR.IF()
        
        # Exception: instruction memory error 
        if status == False:
            return EXC_IMEM_ERROR

        opcode, isa_info = SIMULATOR.ID(inst)

        # Exception: illegal instruction encoding
        if opcode == EXC_ILLEGAL_INST:
            return EXC_ILLEGAL_INST  
        
        status = SIMULATOR.EX(pc, inst, opcode, isa_info)
        
        SIMULATOR.MEM()
        
        SIMULATOR.WB()

        return status

    @staticmethod
    def alu_fn(pc, inst, opcode, isa_info):
        np.seterr(all='ignore')



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  update the stats, you used it in Task 2
        STATS.inst_alu+=1  
        # --------------------------------------------------------------



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   prepare all the operands
        #   check rv32i.py

        # get register index
        rs1 = INSTRUCTION.get_rs1(inst)
        rs2 = INSTRUCTION.get_rs2(inst)
        rd = INSTRUCTION.get_rd(inst)

        # get register values
        rs1_val = SIMULATOR.core.rf.read(rs1)
        rs2_val = SIMULATOR.core.rf.read(rs2)

        # get immediate values
        imm_i = INSTRUCTION.get_imm_i(inst)
        imm_u = INSTRUCTION.get_imm_u(inst)
        # --------------------------------------------------------------
            
        # decide the operand 1
        # check the IN_ALU1 options
        op_1 = None
        if isa_info[IN_ALU1] == OP1_RS1:
            op_1 = rs1_val
        elif isa_info[IN_ALU1] == OP1_PC:
            op_1 = pc
        else:
            op_1 = WORD(0)

        # decide the operand 2
        # check the IN_ALU2 options
        op_2 = None
        if isa_info[IN_ALU2] == OP2_RS2:
            op_2 = rs2_val
        elif isa_info[IN_ALU2] == OP2_IMI:
            op_2 = imm_i
        elif isa_info[IN_ALU2] == OP2_IMU:
            op_2 = imm_u
        else:
            op_2 = WORD(0)
        


        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   0. decide the output based on the op_1 and op_2
        #   1. check the IN_OP options
        #   2. check ref [2]
        #   3. each case can be done in 1~2 lines
        out = None
        if isa_info[IN_OP] == ALU_ADD:
            out = (op_1 + op_2) & 0xffffffff
        elif isa_info[IN_OP] == ALU_SUB:
             out = (op_1 - op_2) & 0xffffffff
        elif isa_info[IN_OP] == ALU_MUL:
            out = (op_1 * op_2) & 0xffffffff
        elif isa_info[IN_OP] == ALU_MULHU:
            out = ((WORD(op_1) * WORD(op_2)) >> 32) & 0xffffffff
        elif isa_info[IN_OP] == ALU_AND:
            out = op_1 & op_2
        elif isa_info[IN_OP] == ALU_OR:
            out = op_1 | op_2
        elif isa_info[IN_OP] == ALU_XOR:
            out = op_1 ^ op_2
        elif isa_info[IN_OP] == ALU_SLT:
            # set less than (signed)
            out = SWORD(op_1) < SWORD(op_2)
        elif isa_info[IN_OP] == ALU_SLTU:
            # set less than (unsigned)
            out = op_1 < op_2
        elif isa_info[IN_OP] == ALU_SLL:
            out = (op_1 << (op_2 & 0x1f)) & 0xffffffff
        elif isa_info[IN_OP] == ALU_SRA:
            out = SWORD(op_1) >> (op_2 & 0x1f)
        elif isa_info[IN_OP] == ALU_SRL:
            out = (op_1 >> (op_2 & 0x1f)) & 0xffffffff
        else:
            out = WORD(0)
        # --------------------------------------------------------------



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   set the pc to the next instruction
        #   2 lines are enough
        SIMULATOR.core.pc.write(pc + 4)
        pc = SIMULATOR.core.pc.read()
        # --------------------------------------------------------------



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   Commit results
        #   1 line is enough
        SIMULATOR.core.rf.write(rd, out)
        # --------------------------------------------------------------
        return EXC_NONE

    
    @staticmethod
    def mem_fn(pc, inst, opcode, isa_info):

        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  update the stats, you used it in Task 2
        STATS.inst_mem+=1 
        # --------------------------------------------------------------



        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  1. prepare the operands
        #  2. notice that imm will be treated as signed
        rs1 = INSTRUCTION.get_rs1(inst)
        rs1_val = SIMULATOR.core.rf.read(rs1)
        # LOAD 
        if isa_info[IN_OP] == MEM_LD:

            # lw rd, rs1, imm
            rd = INSTRUCTION.get_rd(inst)
            imm_i =  INSTRUCTION.get_imm_i(inst)
            addr = rs1_val + imm_i
            # read from memory
            data, status = SIMULATOR.core.dmem.access(True, addr,None, M_XRD)


            if status:
                # write to destination
                SIMULATOR.core.rf.write(rd, data)
            else:
                print("Exception at 0x%08x: " % pc, end="")
                print(EXC_MSG[EXC_DMEM_ERROR])
                return EXC_DMEM_ERROR
        else: # STORE
            
            # sw rs1, rs2, imm
            rs2 = INSTRUCTION.get_rs2(inst)
            rs2_val =  SIMULATOR.core.rf.read(rs2)
            imm_s  = INSTRUCTION.get_imm_s(inst)
            addr =  rs1_val + imm_s
            # write to memory
            data, status = SIMULATOR.core.dmem.access(True, addr, rs2_val, M_XWR) 
            
            # Exception: data memory error
            if not status:
                print("Exception at 0x%08x: " % pc, end="")
                print(EXC_MSG[EXC_DMEM_ERROR])
                return EXC_DMEM_ERROR
        # --------------------------------------------------------------
    


        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  set the pc to the next instruction
        #  2 lines are enough
        SIMULATOR.core.pc.write(pc + 4)
        pc = SIMULATOR.core.pc.read()
        # --------------------------------------------------------------



        return EXC_NONE

    
    @staticmethod
    def ctrl_fn(pc, inst, opcode, isa_info):


        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   set the pcs
        #   2 lines are enough
        STATS.inst_ctrl+=1  
        
        # --------------------------------------------------------------



        # for now ebreak will stop simulation
        # ecall is os syscall, not implemented now
        # Exception: ebreak
        if inst == EBREAK or inst == ECALL:
            return EXC_EBREAK
        


        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  prepare the operands
        #  check rv32i.py
        rs1 = INSTRUCTION.get_rs1(inst)
        rs2 = INSTRUCTION.get_rs2(inst)

        # used by jal and jalr to store the return address
        rd = INSTRUCTION.get_rd(inst)

        rs1_val = SIMULATOR.core.rf.read(rs1)
        rs2_val = SIMULATOR.core.rf.read(rs2)

        imm_i = INSTRUCTION.get_imm_i(inst)
        imm_j = INSTRUCTION.get_imm_j(inst)
        imm_b = INSTRUCTION.get_imm_b(inst)
        # --------------------------------------------------------------



        # the return address for jal and jalr
        pc_prepare = pc + 4
        
        
        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #   check ref [2]
        #   notice the sign or unsigned when comparing the values
        #   decide the next pc in each case
        pc_next = None
        if opcode == JAL:
            pc_next = pc + imm_j
        elif opcode == BEQ:
            pc_next = pc + imm_b if rs1_val == rs2_val else pc_prepare
        elif opcode == BNE:
            pc_next = pc + imm_b if rs1_val != rs2_val else pc_prepare
        elif opcode == BLT:
            # signed
            pc_next = pc + imm_b if SWORD(rs1_val) < SWORD(rs2_val) else pc_prepare
        elif opcode == BGE:
            # signed
            pc_next = pc + imm_b if SWORD(rs1_val) >= SWORD(rs2_val) else pc_prepare
        elif opcode == BLTU: 
            # unsigned
            pc_next = pc + imm_b if rs1_val < rs2_val else pc_prepare
        elif opcode == BGEU: 
            # unsigned
            pc_next = pc + imm_b if rs1_val >= rs2_val else pc_prepare     
        elif opcode == JALR:
            pc_next = rs1_val + imm_i    
        else:
            pc_next = pc_prepare

        if opcode == JAL or opcode == JALR:
            # a register is changed
            # 1 line is enough
            SIMULATOR.core.rf.write(rd, pc_prepare)
        # --------------------------------------------------------------

        # pc_next is has been decided
        # Update PC
        SIMULATOR.core.pc.write(pc_next)
        return EXC_NONE
    
    @staticmethod
    def IF():
        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part A
        # Guide:
        #  1. get the pc
        #  2. access the instruction memory, valid is True
        pc = SIMULATOR.core.pc.read()
        inst, status = SIMULATOR.core.imem.access(True, pc, None, M_XRD)
        # --------------------------------------------------------------

        # Exception: instruction memory error
        if not status:
            print("Exception at 0x%08x: " % pc, end="")
            return EXC_IMEM_ERROR, 0,False
        
        return pc,inst,status

    @staticmethod
    def ID(inst):
        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part A
        # Guide:
        #  1. get the opcode
        #  2. get the isa info though the opcode
        #  3. we defined all isa info in isa_encodings.py
        opcode = INSTRUCTION.get_opcode(inst) #extract opcode 

        # Exception: illegal instruction
        if opcode == ILLEAGAL:
            return EXC_ILLEGAL_INST,None
        
        isa_info = rv32i_t.get(INSTRUCTION.get_opcode(inst),None)
        if isa_info is None:
            return EXC_ILLEGAL_INST, None
     
        #isa_info = next((info for instr, info in rv32i_t.items() if (instr&0x7f) ==opcode),None)
        
        # for key, isa_info in rv32i_t.items():
        #     mask = isa_info[1]
        #     if (inst & mask) == (key & mask):
            
        #         return opcode, isa_info

    
        return opcode,isa_info
        # ------------------------------------------------------------


    @staticmethod
    def EX(pc, inst, opcode, isa_info):
        # --------------------------------------------------------------
        # TASK--IMPLEMENTATION NEEDED
        # Part B
        # Guide:
        #  1. assume the function units (alu, mem, ctrl) are implemented
        #  2. decide which function unit to issue
        #  3. each function unit will return a status and EX will also return it
        #  4. check the definitions.py [Which function unit to use]
        #  5. 6 lines are enough
       if isa_info[IN_CLASS] == CL_ALU:
        return SIMULATOR.alu_fn(pc, inst, opcode, isa_info)
       elif isa_info[IN_CLASS] == CL_MEM:
            return SIMULATOR.mem_fn(pc, inst, opcode, isa_info)
       elif isa_info[IN_CLASS] == CL_CTRL:
            return SIMULATOR.ctrl_fn(pc, inst, opcode, isa_info)
        # --------------------------------------------------------------


    # --------------------------------------------------------------
    # !!!DO NOT MODIFY!!!
    # We dont need to implement these functions in this task
    @staticmethod
    def MEM():
        pass

    @staticmethod
    def WB():
        pass
    # --------------------------------------------------------------


@staticmethod
def helper_dis(pc,inst):
    from parser import PROGRAM
    decode = PROGRAM.disassemble(pc,inst)
    print(decode)