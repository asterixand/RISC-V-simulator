from definitions import *

# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Guide:
#
# These constants are for R type
#
# Here is an explanation of the ADD instruction encoding
# as ref [1] documented:
#
# opcode = 0110011 (7 bits) from bit 0:6
# funct3 = 000 (3 bits) from bit 12:14
# funct7 = 0000000 (7 bits) from bit 25:31
#
# You can decide a binary string to be an ADD instruction by
# checking the opcode, funct3 and funct7 bits
# That's how ADD and ADD_MASK are defined
#
# Hint:
# Based on [1] and how ADD and ADD_MASK are defined
# Define SUB and AND
# only 4 lines are needed
ADD         = WORD(0b0000_0000_0000_0000_0000_0000_0011_0011)
ADD_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

SUB         = WORD(0b0100_0000_0000_0000_0000_0000_0011_0011)
SUB_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

# Extended Multiplication - R type
MUL         = WORD(0b0000_0010_0000_0000_0000_0000_0011_0011)
MUL_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

MULHU       = WORD(0b0000_0010_0000_0000_0011_0000_0011_0011)
MULHU_MASK  = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

XOR         = WORD(0b0000_0000_0000_0000_0100_0000_0011_0011)
XOR_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

OR          = WORD(0b0000_0000_0000_0000_0110_0000_0011_0011)
OR_MASK     = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

AND         = WORD(0b0000_0000_0000_0000_0111_0000_0011_0011)
AND_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

SLL         = WORD(0b0000_0000_0000_0000_0001_0000_0011_0011)
SLL_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

SRL         = WORD(0b0000_0000_0000_0000_0101_0000_0011_0011)
SRL_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

SRA         = WORD(0b0100_0000_0000_0000_0101_0000_0011_0011)
SRA_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

SLT         = WORD(0b0000_0000_0000_0000_0010_0000_0011_0011)
SLT_MASK    = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)

SLTU        = WORD(0b0000_0000_0000_0000_0011_0000_0011_0011)
SLTU_MASK   = WORD(0b1111_1110_0000_0000_0111_0000_0111_1111)
# --------------------------------------------------------------


# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Guide:
#  These constants are for I type
#  ADDI as ref [1] documented, funct7 is not used, only opcode and funct3
ADDI        = WORD(0b0000_0000_0000_0000_0000_0000_0001_0011)
ADDI_MASK   = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

XORI        = WORD(0b0000_0000_0000_0000_0100_0000_0001_0011)
XORI_MASK   = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

ORI         = WORD(0b0000_0000_0000_0000_0110_0000_0001_0011)
ORI_MASK    = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

ANDI        = WORD(0b0000_0000_0000_0000_0111_0000_0001_0011)
ANDI_MASK   = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

SLLI        = WORD(0b0000_0000_0000_0000_0001_0000_0001_0011)
SLLI_MASK   = WORD(0b1111_1100_0000_0000_0111_0000_0111_1111)

SRLI        = WORD(0b0000_0000_0000_0000_0101_0000_0001_0011)
SRLI_MASK   = WORD(0b1111_1100_0000_0000_0111_0000_0111_1111)

SRAI        = WORD(0b0100_0000_0000_0000_0101_0000_0001_0011)
SRAI_MASK   = WORD(0b1111_1100_0000_0000_0111_0000_0111_1111)

SLTI        = WORD(0b0000_0000_0000_0000_0010_0000_0001_0011)
SLTI_MASK   = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

SLTIU       = WORD(0b0000_0000_0000_0000_0011_0000_0001_0011)
SLTIU_MASK  = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

# I type
LW          = WORD(0b0000_0000_0000_0000_0010_0000_0000_0011)
LW_MASK     = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)
# --------------------------------------------------------------



# S type
SW          = WORD(0b0000_0000_0000_0000_0010_0000_0010_0011)
SW_MASK     = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)



# --------------------------------------------------------------
# TASK--IMPLEMENTATION NEEDED
# Guide:
#  These constants are for B type
#  As ref [1] documented, funct7 is not used, only opcode and funct3
BEQ         = WORD(0b0000_0000_0000_0000_0000_0000_0110_0011)
BEQ_MASK    = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

BNE         = WORD(0b0000_0000_0000_0000_0001_0000_0110_0011)
BNE_MASK    = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

BLT         = WORD(0b0000_0000_0000_0000_0100_0000_0110_0011)
BLT_MASK    = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

BGE         = WORD(0b0000_0000_0000_0000_0101_0000_0110_0011)
BGE_MASK    = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

BLTU        = WORD(0b0000_0000_0000_0000_0110_0000_0110_0011)
BLTU_MASK   = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

BGEU        = WORD(0b0000_0000_0000_0000_0111_0000_0110_0011)
BGEU_MASK   = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# I type
JALR        = WORD(0b0000_0000_0000_0000_0000_0000_0110_0111)
JALR_MASK   = WORD(0b0000_0000_0000_0000_0111_0000_0111_1111)

# J type
JAL         = WORD(0b0000_0000_0000_0000_0000_0000_0110_1111)
JAL_MASK    = WORD(0b0000_0000_0000_0000_0000_0000_0111_1111)

# U type
LUI         = WORD(0b0000_0000_0000_0000_0000_0000_0011_0111)
LUI_MASK    = WORD(0b0000_0000_0000_0000_0000_0000_0111_1111)

AUIPC       = WORD(0b0000_0000_0000_0000_0000_0000_0001_0111)
AUIPC_MASK  = WORD(0b0000_0000_0000_0000_0000_0000_0111_1111)

# I type
ECALL       = WORD(0b0000_0000_0000_0000_0000_0000_0111_0011)
ECALL_MASK  = WORD(0b1111_1111_1111_1111_1111_1111_1111_1111)

EBREAK      = WORD(0b0000_0000_0001_0000_0000_0000_0111_0011)
EBREAK_MASK = WORD(0b1111_1111_1111_1111_1111_1111_1111_1111)
# --------------------------------------------------------------



# --------------------------------------------------------------
# !!!DO NOT MODIFY!!!
# Will be used in riscvsim.py
rv32i_t = {
    # Name      name_str  identify_mask  type    class   op1      op2     alu      mem
    #-------------------------------------------------------------------------------------------
    ADD     : [ "add",      ADD_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_ADD,  MT_X,  ],
    SUB     : [ "sub",      SUB_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_SUB,  MT_X,  ],
    MUL     : [ "mul",      MUL_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_MUL,  MT_X,  ],
    MULHU   : [ "mulhu",    MULHU_MASK, R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_MULHU,MT_X,  ],
    XOR     : [ "xor",      XOR_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_XOR,  MT_X,  ],
    OR      : [ "or",       OR_MASK,    R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_OR,   MT_X,  ],
    AND     : [ "and",      AND_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_AND,  MT_X,  ],
    SLL     : [ "sll",      SLL_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_SLL,  MT_X,  ],
    SRL     : [ "srl",      SRL_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_SRL,  MT_X,  ],
    SRA     : [ "sra",      SRA_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_SRA,  MT_X,  ],
    SLT     : [ "slt",      SLT_MASK,   R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_SLT,  MT_X,  ],
    SLTU    : [ "sltu",     SLTU_MASK,  R_TYPE,  CL_ALU,  OP1_RS1, OP2_RS2, ALU_SLTU, MT_X,  ],
    #-------------------------------------------------------------------------------------------
    ADDI    : [ "addi",     ADDI_MASK,  I_TYPE,  CL_ALU,  OP1_RS1, OP2_IMI, ALU_ADD,  MT_X,  ],
    XORI    : [ "xori",     XORI_MASK,  I_TYPE,  CL_ALU,  OP1_RS1, OP2_IMI, ALU_XOR,  MT_X,  ],
    ORI     : [ "ori",      ORI_MASK,   I_TYPE,  CL_ALU,  OP1_RS1, OP2_IMI, ALU_OR,   MT_X,  ],
    ANDI    : [ "andi",     ANDI_MASK,  I_TYPE,  CL_ALU,  OP1_RS1, OP2_IMI, ALU_AND,  MT_X,  ],
    SLLI    : [ "slli",     SLLI_MASK,  IS_TYPE, CL_ALU,  OP1_RS1, OP2_IMI, ALU_SLL,  MT_X,  ],
    SRLI    : [ "srli",     SRLI_MASK,  IS_TYPE, CL_ALU,  OP1_RS1, OP2_IMI, ALU_SRL,  MT_X,  ],
    SRAI    : [ "srai",     SRAI_MASK,  IS_TYPE, CL_ALU,  OP1_RS1, OP2_IMI, ALU_SRA,  MT_X,  ],
    SLTI    : [ "slti",     SLTI_MASK,  I_TYPE,  CL_ALU,  OP1_RS1, OP2_IMI, ALU_SLT,  MT_X,  ],
    SLTIU   : [ "sltiu",    SLTIU_MASK, I_TYPE,  CL_ALU,  OP1_RS1, OP2_IMI, ALU_SLTU, MT_X,  ],
    #-------------------------------------------------------------------------------------------
    LW      : [ "lw",       LW_MASK,    IL_TYPE, CL_MEM,  OP1_RS1, OP2_IMI, MEM_LD,   MT_W,  ],
    #-------------------------------------------------------------------------------------------
    SW      : [ "sw",       SW_MASK,    S_TYPE,  CL_MEM,  OP1_RS1, OP2_IMS, MEM_ST,   MT_W,  ],
    #-------------------------------------------------------------------------------------------
    BEQ     : [ "beq",      BEQ_MASK,   B_TYPE,  CL_CTRL, OP1_RS1, OP2_IMB, ALU_X,    MT_X,  ],
    BNE     : [ "bne",      BNE_MASK,   B_TYPE,  CL_CTRL, OP1_RS1, OP2_IMB, ALU_X,    MT_X,  ],
    BLT     : [ "blt",      BLT_MASK,   B_TYPE,  CL_CTRL, OP1_RS1, OP2_IMB, ALU_X,    MT_X,  ],
    BGE     : [ "bge",      BGE_MASK,   B_TYPE,  CL_CTRL, OP1_RS1, OP2_IMB, ALU_X,    MT_X,  ],
    BLTU    : [ "bltu",     BLTU_MASK,  B_TYPE,  CL_CTRL, OP1_RS1, OP2_IMB, ALU_X,    MT_X,  ],
    BGEU    : [ "bgeu",     BGEU_MASK,  B_TYPE,  CL_CTRL, OP1_RS1, OP2_IMB, ALU_X,    MT_X,  ],
    #-------------------------------------------------------------------------------------------
    JAL     : [ "jal",      JAL_MASK,   J_TYPE,  CL_CTRL, OP1_RS1, OP2_IMJ, ALU_X,    MT_X,  ],
    JALR    : [ "jalr",     JALR_MASK,  IJ_TYPE, CL_CTRL, OP1_RS1, OP2_IMI, ALU_ADD,  MT_X,  ],
    #-------------------------------------------------------------------------------------------
    LUI     : [ "lui",      LUI_MASK,   U_TYPE,  CL_ALU,  OP1_X,   OP2_IMU, ALU_ADD,  MT_X,  ],
    AUIPC   : [ "auipc",    AUIPC_MASK, U_TYPE,  CL_ALU,  OP1_PC,  OP2_IMU, ALU_ADD,  MT_X,  ],
    #-------------------------------------------------------------------------------------------
    ECALL   : [ "ecall",    ECALL_MASK, X_TYPE,  CL_CTRL, OP1_X,   OP2_X,   ALU_X,    MT_X,  ],
    EBREAK  : [ "ebreak",   EBREAK_MASK,X_TYPE,  CL_CTRL, OP1_X,   OP2_X,   ALU_X,    MT_X,  ],
}
# --------------------------------------------------------------
