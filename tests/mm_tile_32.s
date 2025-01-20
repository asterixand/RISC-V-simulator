# N = 100
# TILE_SIZE = 32
# a0 = 81021600 = 0x4D44AA0
        .text
        .align  2
        .globl  _start

_start: 
        lui     sp,0x80f10
        addi    sp,sp,-96
        sw      ra,92(sp)
        sw      s0,88(sp)
        sw      s1,84(sp)
        sw      s2,80(sp)
        sw      s3,76(sp)
        sw      s4,72(sp)
        sw      s5,68(sp)
        sw      s6,64(sp)
        sw      s7,60(sp)
        sw      s8,56(sp)
        sw      s9,52(sp)
        sw      s10,48(sp)
        sw      s11,44(sp)
        addi    s0,sp,96
        li      a5,-40960
        addi    a5,a5,960
        add     sp,sp,a5
        mv      t4,sp
        add     sp,sp,a5
        mv      t1,sp
        add     sp,sp,a5
        mv      a7,sp
        mv      t0,sp
        mv      t6,t1
        mv      t5,t4
        li      a0,100
        li      t3,0
        mv      t2,a0
.L2:
        mv      a6,t3
        mv      a1,t0
        mv      a2,t6
        mv      a5,t3
        mv      a3,t5
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
        addi    t3,t3,1
        addi    t5,t5,400
        addi    t6,t6,400
        addi    t0,t0,400
        addi    a0,a0,1
        bne     t3,t2,.L2
        li      a5,0
        li      a4,0
        li      a6,100
        li      a3,4096
        addi    s2,a3,-896
        li      s3,128
        mv      s1,a4
        j       .L4
.L5:
        sw      s5,0(s11)
        addi    s7,s7,1
        beq     s7,t0,.L7
        addi    s8,s8,4
        addi    a4,a4,4
        beq     s7,a6,.L7
.L9:
        mv      s11,s8
        lw      s5,0(s8)
        mv      t1,a4
        mv      a7,t3
        mv      a5,t6
.L6:
        lw      a1,0(a7)
        lw      s4,0(t1)
        mul     a1,a1,s4
        add     s5,s5,a1
        addi    a5,a5,1
        beq     a5,t4,.L5
        addi    a7,a7,4
        addi    t1,t1,400
        bne     a5,a6,.L6
        j       .L5
.L7:
        lw      a7,-68(s0)
        lw      a1,-72(s0)
        addi    a7,a7,1
        beq     a7,a0,.L8
        addi    t3,t3,400
        addi    a1,a1,400
        beq     a7,a6,.L8
.L11:
        mv      a4,s9
        mv      s8,a1
        lw      s7,-76(s0)
        sw      a7,-68(s0)
        sw      a1,-72(s0)
        j       .L9
.L8:
        lw      s5,-76(s0)
        lw      a5,-92(s0)
        lw      a7,-96(s0)
        mv      s7,a3
        addi    a5,a5,32
        add     a3,s10,s2
        addi    a7,a7,128
        li      a4,160
        beq     a5,a4,.L10
.L13:
        addi    t6,a5,-32
        slli    a4,a3,2
        add     s9,a4,t2
        lw      a1,-84(s0)
        mv      t3,a7
        lw      a4,-80(s0)
        mv      t4,a5
        sw      s5,-76(s0)
        sw      a5,-92(s0)
        mv      s10,a3
        sw      a7,-96(s0)
        mv      a7,a4
        mv      a3,s7
        j       .L11
.L10:
        lw      a7,-88(s0)
        mv      a3,s7
        mv      a1,s6
        mv      t1,a2
        mv      t3,a0
        mv      a0,s1
        addi    s5,s5,32
        beq     s5,s3,.L12
.L15:
        slli    a5,s5,2
        add     a4,a3,a5
        sw      a4,-84(s0)
        add     t2,t1,a5
        li      t6,0
        li      a5,32
        add     a4,s5,a5
        sw      a7,-88(s0)
        mv      a7,a1
        mv      s7,a3
        mv      a3,t6
        mv      s6,a1
        mv      s1,a0
        mv      a2,t1
        mv      t0,a4
        mv      a0,t3
        j       .L13
.L12:
        lw      s1,-80(s0)
        mv      t4,a0
        addi    s1,s1,32
        add     a5,t5,s2
        beq     s1,s3,.L20
.L4:
        slli    a4,a5,2
        add     a2,t4,a4
        add     a3,a7,a4
        li      s5,0
        addi    a4,s1,32
        sw      s1,-80(s0)
        mv      t5,a5
        mv      a1,a2
        mv      a0,t4
        mv      t3,a4
        j       .L15
.L20:
        li      a5,40960
        add     a7,a7,a5
        lw      a0,-964(a7)
        addi    sp,s0,-96
        lw      ra,92(sp)
        lw      s0,88(sp)
        lw      s1,84(sp)
        lw      s2,80(sp)
        lw      s3,76(sp)
        lw      s4,72(sp)
        lw      s5,68(sp)
        lw      s6,64(sp)
        lw      s7,60(sp)
        lw      s8,56(sp)
        lw      s9,52(sp)
        lw      s10,48(sp)
        lw      s11,44(sp)
        addi    sp,sp,96
        ebreak