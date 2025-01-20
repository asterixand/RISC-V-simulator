# DO NOT MODIFY EXISTING DEFINITIONS
import numpy as np

# define the data types
# unsigned and signed word (32-bit)
WORD = np.uint32
SWORD = np.int32

WORD_SIZE           = 4
NUM_REGS            = 32

YOUR_CODE_HERE      = None
# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Guide:
#   IMEM: 0x80000000 - 0x8000ffff (64KB)
#   DMEM: 0x80010000 - 0x8001ffff (15MB)
#   Use hex-value for address (0x--------)
#   SIZE is in bytes
#   See how ILLEAGAL is defined (these values are uint32)
#   Used in riscvsim.py to initialize the memory layout
#   All these numbers are unsigned (use WORD to warp them)
IMEM_START          = WORD(0x80000000) 
IMEM_SIZE           = WORD(0x00010000) #--64kb 
DMEM_START          = WORD(0x80010000)
# Set this size to 15MB
DMEM_SIZE           = WORD(0xF00000)
# --------------------------------------------------------------


# Used in rv31i.py when decoding an instruction is error
ILLEAGAL            = WORD(0xffffffff)


# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Guide:
# 1. Implemented BUBBLE using the encoding of:  xor x0,x0,x0
# 2. Implemented NOP using the encoding of:     addi x0, x0, 0
# 3. Use the hex value for both case
# 4. Follow the style of ILLEAGAL definition
#
# Extra Notes:
# Instructions like nop are called peudo-instructions
# e.g. you might see nop, mv, li etc. in the assembly code (*.s, *.objdump)
# But this simulator will dump them into the actual instructions
# See reference [1] page 4 for more details
# So the dumped instructions of this simulator may not match with the objdump
# You can check whether the mismatch instructions are  pseudo-instructions or not
BUBBLE              = WORD(0x00004033)
NOP                 = WORD(0x00000013) #0/0/0/0/0/0/1/3
# --------------------------------------------------------------



# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Guide:
# 1. Check reference [1], following the R-type encoding
# 2. Understand how OP_MASK and OP_SHIFT are encoded
# 3. These constants will be used in rv32i.py
# 4. Shift is counted from the right
RD_MASK             = WORD(0x00000f80)#1111/1000/0000
RD_SHIFT            = 7

RS1_MASK            = WORD(0x000f8000) #1111/1000/0000/0000/0000
RS1_SHIFT           = 15

RS2_MASK            = WORD(0x01f00000) #0001/1111/0000/0000/0000/0000/0000
RS2_SHIFT           = 20
# --------------------------------------------------------------



# --------------------------------------------------------------
# NO MORE IMPLEMENTATION NEEDED AFTER THIS LINE
# BUT MAKE SURE TO HAVE AN OVERVIEW OF THESE DEFINITIONS
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# Memory Control Signals
# Used in structure.py
# Read operation
M_XRD               = 0
# Write operation
M_XWR               = 1
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# Used to index the ISA information table (rv32i_t) defined in isa_encodings.py
IN_NAME             = 0
# Instruction mask for general encoding
# Decide the instruction type, e.g. ADD, SUB, etc.
IN_MASK             = 1
# R, I, S, B, U and J type
IN_TYPE             = 2
# ALU, MEM, CTRL
IN_CLASS            = 3
# Operands [if any]
IN_ALU1             = 4
IN_ALU2             = 5
# Function unit operation type
IN_OP               = 6
# Memory operation type
IN_MT               = 7
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# rv32i_t[IN_TYPE]
# Used in parser.py to decode/disassemble the instruction
R_TYPE              = 0
I_TYPE              = 1
IL_TYPE             = 2     # I_TYPE, but load instruction
IJ_TYPE             = 3     # I_TYPE, but jalr instruction
IS_TYPE             = 4     # I_TYPE, but shift instructions
U_TYPE              = 5
S_TYPE              = 6
B_TYPE              = 7
J_TYPE              = 8
X_TYPE              = 9
ISA_TYPES = [0,1,2,3,4,5,6,7,8,9]
# --------------------------------------------------------------

# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# rv32i_t[IN_CLASS]
# Which function unit to use
# Used in risvcsim.py to select the function unit
CL_ALU              = 0
CL_MEM              = 1
CL_CTRL             = 2
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# rv32i_t[IN_ALU1] 
# Used to select the first operand for the ALU
# X means no operand
# Used in risvcsim.py
OP1_X               = 0
OP1_RS1             = 1         
# some instructions use PC as operand (auipc)
OP1_PC              = 2
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# rv32i_t[IN_ALU2] 
# Used to select the first operand for the ALU
# X means no operand
# Used in risvcsim.py
OP2_X               = 0
# R type register 2
OP2_RS2             = 1         
# I type immediate
OP2_IMI             = 2         
# S type immediate
OP2_IMS             = 3         
# U type immediate
OP2_IMU             = 4
# J type immediate
OP2_IMJ             = 5
# B type immediate
OP2_IMB             = 6
# --------------------------------------------------------------

# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# rv32i_t[IN_OP]
# Used to control the ALU and memory operation
# Used in risvcsim.py
ALU_X               = 0
ALU_ADD             = 1
ALU_SUB             = 2
ALU_SLL             = 3
ALU_SRL             = 4
ALU_SRA             = 5
ALU_AND             = 6
ALU_OR              = 7
ALU_XOR             = 8
ALU_SLT             = 9
ALU_SLTU            = 10
MEM_LD              = 11
MEM_ST              = 12
# Extended to support MUL operation
ALU_MUL             = 13
ALU_MULHU           = 14
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# rv32i_t[IN_MT]
# Memory operation type
# no memory operation
# used in isa_encodings.py
MT_X                = 0
# not used
MT_B                = 1
# not used
MT_H                = 2
# word
MT_W                = 3
# not used
MT_D                = 4
MT_BU               = 5
MT_HU               = 6
MT_WU               = 7
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# Exception codes and messages
# Used in riscvsim.py to handle exceptions
EXC_NONE            = 0         # EXC_NONE should be zero
EXC_IMEM_ERROR      = 1
EXC_DMEM_ERROR      = 2
EXC_ILLEGAL_INST    = 4
EXC_EBREAK          = 8

EXC_MSG = {         EXC_IMEM_ERROR:     "instruction mem access error", 
                    EXC_DMEM_ERROR:     "data mem access error",
                    EXC_ILLEGAL_INST:   "illegal instruction",
                    EXC_EBREAK:         "ebreak",
}
# --------------------------------------------------------------