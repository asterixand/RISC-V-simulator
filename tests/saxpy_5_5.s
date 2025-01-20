# ans = 0xffffffe9 (a0)
        .text
        .align  2
        .globl  _start

_start:          
        lui     sp, 0x80f10
        addi    sp,sp,-64
        sw      ra,60(sp)
        li      a5,-10
        sw      a5,28(sp)
        li      a5,7
        sw      a5,8(sp)
        li      a4,-8
        sw      a4,32(sp)
        sw      a5,12(sp)
        li      a4,-6
        sw      a4,36(sp)
        sw      a5,16(sp)
        li      a4,-4
        sw      a4,40(sp)
        sw      a5,20(sp)
        li      a4,-2
        sw      a4,44(sp)
        sw      a5,24(sp)
        addi    a2,sp,8
        addi    a1,sp,28
        li      a0,2
        call    saxpy
        lw      a5,8(sp)
        lw      a4,12(sp)
        add     a5,a5,a4
        lw      a0,20(sp)
        add     a0,a5,a0
        lw      ra,60(sp)
        addi    sp,sp,64
        ebreak
saxpy:
        mv      a5,a2
        addi    a2,a2,20
.L2:
        lw      a3,0(a1)
        mul     a3,a0,a3
        lw      a4,0(a5)
        add     a4,a4,a3
        sw      a4,0(a5)
        addi    a1,a1,4
        addi    a5,a5,4
        bne     a5,a2,.L2
        ret