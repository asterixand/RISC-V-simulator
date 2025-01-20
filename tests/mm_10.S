# A X B = C
# A: 10x10
# B: 10x10
# C: 10x10
# Ans = 6210 
# So a0 = 6210 = 0x1842


        .text
        .align  2
        .globl  _start

_start:          
        lui     sp, 0x80f10
        addi    sp,sp,-16
        sw      ra,12(sp)
        sw      s0,8(sp)
        addi    s0,sp,16
        addi    sp,sp,-400
        mv      a0,sp
        addi    sp,sp,-400
        mv      t4,sp
        addi    sp,sp,-400
        mv      t5,sp
        li      a1,10
        li      t1,0
        li      a7,0
        mv      t3,a1
.L2:
        mv      a6,a7
        mv      a5,t1
        mv      a4,a7
        li      a3,0
.L3:
        add     a2,a0,a5
        sw      a3,0(a2)
        add     a2,t4,a5
        sw      a4,0(a2)
        add     a2,t5,a5
        sw      zero,0(a2)
        add     a3,a3,a6
        addi    a4,a4,1
        addi    a5,a5,4
        bne     a4,a1,.L3
        addi    a7,a7,1
        addi    t1,t1,40
        addi    a1,a1,1
        bne     a7,t3,.L2
        mv      t1,a0
        mv      t0,t5
        addi    t3,a0,400
        addi    t6,t4,440
.L4:
        addi    a0,t4,400
        mv      a6,t0
.L8:
        mv      a7,a6
        lw      a2,0(a6)
        addi    a5,a0,-400
        mv      a3,t1
.L5:
        lw      a4,0(a3)
        lw      a1,0(a5)
        mul     a4,a4,a1
        add     a2,a2,a4
        addi    a3,a3,4
        addi    a5,a5,40
        bne     a5,a0,.L5
        sw      a2,0(a7)
        addi    a6,a6,4
        addi    a0,a0,4
        bne     a0,t6,.L8
        addi    t1,t1,40
        addi    t0,t0,40
        bne     t1,t3,.L4
        lw      a0,396(t5)
        addi    sp,s0,-16
        lw      ra,12(sp)
        lw      s0,8(sp)
        addi    sp,sp,16
        ebreak