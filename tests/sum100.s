# This program computes the sum of integers from 1 to 100.
# x31 = 5050 = 0x13ba

    .text
    .align  2
    .globl  _start
_start:                         # code entry point
    li      t0, 1
    li      t1, 100
    li      x31, 0
Loop:
    add     x31, x31, t0
    addi    t0, t0, 1
    ble     t0, t1, Loop
    ebreak

