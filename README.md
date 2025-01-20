# RISC-V CPU Simulator

This project is a Python-based simulator for a simplified RISC-V processor. It simulates the entire instruction cycle of a RISC-V processor, including instruction fetch, decode, execute, memory access, and write-back stages.

The simulator includes the following components:
- **Registers**: A 32-register file (including special registers like `x0` which is always zero).
- **ALU Operations**: Support for RISC-V ALU instructions such as addition, subtraction, bitwise operations, and more.
- **Memory Management**: Simulation of instruction memory (IMEM) and data memory (DMEM), with word-aligned access for load/store operations.
- **Control Flow**: Implements control instructions like branches, jumps (JAL, JALR), and system calls (ECALL, EBREAK).
- **Performance Metrics**: Tracks CPU cycles, instruction count, and provides stats on the types of instructions executed (ALU, memory, control).

The project is designed to provide a working understanding of how RISC-V processors operate at a low level, from instruction decoding to execution. The codebase is modular, making it easy to extend and experiment with various aspects of the RISC-V architecture.
