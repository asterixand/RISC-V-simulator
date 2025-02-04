# RISC-V CPU Simulator

This project is a Python-based simulator for a simplified RISC-V processor. It simulates the entire instruction cycle of a RISC-V processor, including instruction fetch, decode, execute, memory access, and write-back stages.

The simulator includes the following components:
- **Registers**: A 32-register file (including special registers like `x0` which is always zero).
- **ALU Operations**: Support for RISC-V ALU instructions such as addition, subtraction, bitwise operations, and more.
- **Memory Management**: Simulation of instruction memory (IMEM) and data memory (DMEM), with word-aligned access for load/store operations.
- **Control Flow**: Implements control instructions like branches, jumps (JAL, JALR), and system calls (ECALL, EBREAK).
- **Performance Metrics**: Tracks CPU cycles, instruction count, and provides stats on the types of instructions executed (ALU, memory, control).

The project is designed to provide a working understanding of how RISC-V processors operate at a low level, from instruction decoding to execution. The codebase is modular, making it easy to extend and experiment with various aspects of the RISC-V architecture.

1.1	Simple Cache-Memory Simulator:
- i.	The determine_miss_penalty method calculates the latency penalty associated with accessing a specific memory address based on whether it results in a row buffer hit or a row buffer miss. 
- ii.	A row buffer hit happens when the requested memory data is already loaded into cache and when occurs, there’s an additional delay since the data must be fetched from a lower (slower) memory hierarchy (like main memory). When there’s a row buffer hit, it directly improves performance as he the data access is faster with minimal latency and a row buffer miss slows down the overall performance leading to higher miss penalties.

1.2	Verifying with real traces:
- i.	The link to the output files: 
https://drive.google.com/drive/folders/1uFgUyWM-XQJzMFJSWY-Kfsw3O8idChQe?usp=sharing

1.3	Cache Design Space Exploration:
- i.	AIM: The goal of this experiment is to evaluate the impact of cache parameters—cache size, block size and associativity—on cache performance, measured in terms of the CPI Stall metric. The aim is to identify an optimal cache configuration that minimizes the geometric mean CPI stall across multiple real-world traces.

ii.	EXPERIMENTAL SETUP:
- 1.	Cache Size: Fixed at 16 KB (16384 bytes).
- 2.	Block Sizes Tested: 128B, 256B, 512B, 2048B.
- 3.	Associativities Tested: 1-way (direct-mapped), 4-way, 8-way, 16-way, 32-way.
- 4.	Trace Files: 462.libquantum.gz, 464.h264ref.gz, 403.gcc.gz, 445.gobmk.gz
- 5.	Number of Trace Lines Simulated: 1000 lines per trace.

iii.	RESULTS:

   Analysis:
 
Graphical Analysis
A bar chart visualizing the geometric mean CPI stall for all configurations is provided below. Configurations are represented as (Block Size, Associativity) pairs. The lower the CPI stall, the better the performance. The data shows a clear inverse relationship between the block size and CPI stalls.

 


3. Key Observations
1.4	Block Size Effect:
- i.	Larger block sizes (e.g., 2048B and 512B) generally result in lower CPI stalls since larger blocks can store more contiguous data thereby reducing the miss rate. However, this can sometimes lead to inefficient usage of cache space if the working set is smaller than the block size.
- ii.	Small block sizes (e.g., 128B) exhibit significantly higher CPI stalls due to increased miss rates as they require more frequent cache accesses lowering the cache efficiency.

1.5	Associativity Effect:
- i.	Higher associativities (e.g., 8-way, 16-way) reduce CPI stalls compared to direct-mapped or low-associativity caches since more sets in cache reduce the chances of conflict misses.
- ii.	However, the performance improvement tapers off as associativity increases beyond 8 or 16 as increasing associativity beyond 8-way shows diminishing returns. This shows that higher associativity after a certain point doesn’t really improve performance. 
- iii.	The performance difference between various associativity levels (A:1 to A:32) is relatively small compared to block size effects and when we consider associativity changes within each block size group, it has a minimal impact.

1.6	Optimal Configuration:
- i.	The configuration with the lowest geometric mean CPI stall is Block Size: 2048B, Associativity: 8, achieving a CPI stall of 35.00. The 2048B with 4-8 way associativity has the best performance and balances between complexity and performance. 
- ii.	Block size has a significant impact on cache performance. Larger block sizes reduce CPI stalls due to lower miss rates.
- iii.	Associativity also has a crucial role as higher associativity reduces conflict misses but improvement diminishes beyond a certain point. 
From the observation we can infer that when optimizing cache performance, both block size and associativity must be considered carefully. While larger block sizes and higher associativities provide performance benefits, there is a point beyond which increasing either parameters gives us diminishing returns as we must consider other factors like cost and complexity of implementation. 

