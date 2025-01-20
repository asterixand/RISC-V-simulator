# A X B = C
# A: 100x100
# B: 100x100
# C: 100x100
# Ans = 81021600 
# So a0 = 81021600 = 0x4D44AA0


        .text
        .align  2
        .globl  _start

_start:          
        lui     sp, 0x80f10
        addi    sp,sp,-16
        sw      ra,12(sp)
        sw      s0,8(sp)
        addi    s0,sp,16
        li      a5,-40960
        addi    a5,a5,960
        add     sp,sp,a5
        mv      t5,sp
        add     sp,sp,a5
        mv      t0,sp
        add     sp,sp,a5
        mv      t6,sp
        mv      t4,sp
        mv      t3,t0
        mv      t1,t5
        li      a0,100
        li      a7,0
        mv      t2,a0
.L2:
        mv      a6,a7
        mv      a1,t4
        mv      a2,t3
        mv      a5,a7
        mv      a3,t1
        li      a4,0
.L3:
        sw      a4,0(a3)
        sw      a5,0(a2)
        sw      zero,0(a1)
        add     a4,a4,a6
        addi    a3,a3,4
        addi    a5,a5,1
        addi    a2,a2,4
        addi    a1,a1,4
        bne     a5,a0,.L3
        addi    a7,a7,1
        addi    t1,t1,400
        addi    t3,t3,400
        addi    t4,t4,400
        addi    a0,a0,1
        bne     a7,t2,.L2
        li      t3,0
        li      t2,40960
        addi    t2,t2,-960
        li      t1,40960
        addi    t1,t1,-560
        add     t1,t0,t1
        li      t4,-40960
        addi    t4,t4,960
.L4:
        add     a6,t6,t3
        add     a0,t0,t2
.L8:
        mv      a7,a6
        lw      a2,0(a6)
        add     a3,t5,t3
        add     a5,a0,t4
.L5:
        lw      a4,0(a3)
        lw      a1,0(a5)
        mul     a4,a4,a1
        add     a2,a2,a4
        addi    a3,a3,4
        addi    a5,a5,400
        bne     a5,a0,.L5
        sw      a2,0(a7)
        addi    a6,a6,4
        addi    a0,a0,4
        bne     a0,t1,.L8
        addi    t3,t3,400
        bne     t3,t2,.L4
        li      a5,40960
        add     t6,t6,a5
        lw      a0,-964(t6)
        addi    sp,s0,-16
        lw      ra,12(sp)
        lw      s0,8(sp)
        addi    sp,sp,16
        ebreak