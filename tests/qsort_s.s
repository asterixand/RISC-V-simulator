# 10 19 26 31 34 35
#  t0 ---------> t5
# t0 = 0x0000000a
# t1 = 0x00000013
# t2 = 0x0000001a
# t3 = 0x0000001f
# t4 = 0x00000022
# t5 = 0x00000023


        .text
        .align  2
        .globl  _start

_start:          
        lui     sp, 0x80f10
        addi    sp,sp,-48
        sw      ra,44(sp)
        sw      s0,40(sp)
        li      a5,0
        j       .L16
.L17:
        addi    a2,a5,1
        slli    a3,a2,2
        add     a3,a3,a2
        slli    a4,a3,1
        mul     a3,a5,a5
        sub     a4,a4,a3
        slli    a5,a5,2
        addi    a3,sp,8
        add     a5,a5,a3
        sw      a4,0(a5)
        mv      a5,a2
.L16:
        li      a4,5
        ble     a5,a4,.L17
        addi    s0,sp,8
        mv      a2,a4
        li      a1,0
        mv      a0,s0
        call    quickSort

        lw t0, 0(s0)
        lw t1, 4(s0)
        lw t2, 8(s0)
        lw t3, 12(s0)
        lw t4, 16(s0)
        lw t5, 20(s0)

        lw      a0,8(sp)
        lw      ra,44(sp)
        lw      s0,40(sp)
        addi    sp,sp,48
        ebreak

swap:
        lw      a5,0(a0)
        lw      a4,0(a1)
        sw      a4,0(a0)
        sw      a5,0(a1)
        ret
partition:
        addi    sp,sp,-32
        sw      ra,28(sp)
        sw      s0,24(sp)
        sw      s1,20(sp)
        sw      s2,16(sp)
        sw      s3,12(sp)
        sw      s4,8(sp)
        sw      s5,4(sp)
        mv      s1,a0
        mv      s0,a1
        mv      s2,a2
        slli    s5,a2,2
        add     s5,a0,s5
        lw      s4,0(s5)
        addi    s3,a1,-1
        j       .L3
.L4:
        addi    s0,s0,1
.L3:
        bge     s0,s2,.L7
        slli    a1,s0,2
        add     a1,s1,a1
        lw      a5,0(a1)
        bge     a5,s4,.L4
        addi    s3,s3,1
        slli    a0,s3,2
        add     a0,s1,a0
        call    swap
        j       .L4
.L7:
        addi    s3,s3,1
        slli    a0,s3,2
        mv      a1,s5
        add     a0,s1,a0
        call    swap
        mv      a0,s3
        lw      ra,28(sp)
        lw      s0,24(sp)
        lw      s1,20(sp)
        lw      s2,16(sp)
        lw      s3,12(sp)
        lw      s4,8(sp)
        lw      s5,4(sp)
        addi    sp,sp,32
        jr      ra
quickSort:
        blt     a1,a2,.L14
        ret
.L14:
        addi    sp,sp,-32
        sw      ra,28(sp)
        sw      s0,24(sp)
        sw      s1,20(sp)
        sw      s2,16(sp)
        sw      s3,12(sp)
        mv      s2,a0
        mv      s1,a1
        mv      s0,a2
        call    partition
        mv      s3,a0
        addi    a2,a0,-1
        mv      a1,s1
        mv      a0,s2
        call    quickSort
        mv      a2,s0
        addi    a1,s3,1
        mv      a0,s2
        call    quickSort
        lw      ra,28(sp)
        lw      s0,24(sp)
        lw      s1,20(sp)
        lw      s2,16(sp)
        lw      s3,12(sp)
        addi    sp,sp,32
        jr      ra