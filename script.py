import os
import subprocess
from math import log, exp
import matplotlib.pyplot as plt

block_sizes = [128, 256, 512, 2048]
associativities = [1, 4, 8, 16, 32]
cache_size = 16384
trace_files = [
    "462.libquantum.gz",
    "464.h264ref.gz",
    "403.gcc.gz",
    "445.gobmk.gz"
]
num_lines = 1000

results = {}

for block_size in block_sizes:
    for associativity in associativities:
        print(f"\n\nRunning simulations for Block Size: {
              block_size}, Associativity: {associativity}")
        cpi_stalls = []

        for trace in trace_files:
            command = f"python sim_sa.py {trace} {cache_size} {
                associativity} {block_size} {num_lines}"
            try:
                result = subprocess.run(
                    command, shell=True, capture_output=True, text=True)
                output = result.stdout

                print(f"\nCommand output for {trace}:")
                print(output)

                if result.stderr:
                    print(f"Error output:")
                    print(result.stderr)

                cpi_found = False
                for line in output.splitlines():
                    if "CPI_stall" in line:
                        cpi = float(line.split()[-1])
                        cpi_stalls.append(cpi)
                        cpi_found = True
                        print(f"Found CPI: {cpi}")
                        break

                if not cpi_found:
                    print(f"Warning: No CPI_stall found in output for {trace}")

            except Exception as e:
                print(f"Error running command: {command}")
                print(f"Exception: {str(e)}")

        if cpi_stalls:
            geometric_mean_cpi = sum((cpi)
                                     for cpi in cpi_stalls) / len(cpi_stalls)
            results[(block_size, associativity)] = geometric_mean_cpi

print("\nResults (sorted by Geometric Mean CPI):")
sorted_results = sorted(results.items(), key=lambda x: x[1])
for (block_size, associativity), cpi in sorted_results:
    print(f"Block Size: {block_size}, Associativity: {
          associativity}, Geometric Mean CPI: {cpi:.2f}")

configs = [f"B:{b}, A:{a}" for b, a in results.keys()]
cpis = list(results.values())

plt.figure(figsize=(12, 6))
plt.bar(configs, cpis)
plt.xlabel("Configurations (Block Size, Associativity)")
plt.ylabel("Geometric Mean CPI Stall")
plt.title("Cache Design Space Exploration")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
