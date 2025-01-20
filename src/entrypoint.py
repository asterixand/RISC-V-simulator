#!/usr/bin/env python3

import sys
import argparse
from definitions import *
from rv32i import *
from parser import *
from riscvsim import *


def _parse_args():
    parser = argparse.ArgumentParser(description="RISCV Simulator in Python")

    parser.add_argument("-l", "--log", help="Log file level: 0~6", type=int, default=0)
    parser.add_argument("-c", "--cycle", help="Log start cycle", type=int, default=0)
    parser.add_argument("filename", help="RISCV executable file")

    
    LOG.level = parser.parse_args().log
    if LOG.level > LOG.MAX_LEVEL:
        print("Log level should be in range 0~6")
        exit(1)
    LOG.start_at = parser.parse_args().cycle
    if LOG.start_at < 0:
        print("Start cycle should be positive")
        exit(1)
    
    args = parser.parse_args()
    #print(args)
    return args.filename



def main():

    filename = _parse_args()
    print(filename)
    if not filename:
        sys.exit(1)
    

    # Create the simulator instance
    # Instructions will be taken by this simulator instance    
    riscv_sim = RISCVSIM()

    # RISCV binary parser
    prog = PROGRAM()
    
    # Extract the entry point
    entry_point = prog.load_program(simulator=riscv_sim, filename=filename)
    if not entry_point:
        sys.exit(1)
    
    # check the program is correctly loaded
    # and the parsed instructions are correct
    # compare this output with the objdump output
    prog.dump(riscv_sim)

    # Start the simulation
    riscv_sim.run(entry_point)
    
    # Print the runtimr information
    STATS.print_stats()


if __name__ == "__main__":
    main()
