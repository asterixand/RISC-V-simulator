# x31 = 1

    .text
    .align  2
    .globl  _start
_start:                         # code entry point
    lui     t0, 0x80010
    li      x31, 3
    sw      x31, 0(t0)
    addi    x31, x31, 10
    lw      x31, 0(t0)
    addi    x31, x31, -1
    addi    x31, x31, -1
    ebreak
    


