import dimod
from dwave.system import LeapHybridSampler
import numpy as np

# Define the number of bits to represent x (adjust for higher precision)
num_bits = 10

# Generate QUBO matrix representing x
Q = {(i, i): 1 for i in range(num_bits)}

# Add constraint: x >= 50
constraint = 50
for i in range(num_bits):
    if constraint & (1 << i):
        Q[(i, i)] -= 2 ** i

# Create a binary quadratic model
bqm = dimod.BinaryQuadraticModel.from_qubo(Q)

# Use D-Wave's Leap Hybrid Solver
sampler = LeapHybridSampler()
sampleset = sampler.sample(bqm)

# Get the lowest energy sample (solution)
solution = sampleset.first.sample

# Convert the binary representation to the integer value of x
x = sum(2**i * v for i, v in solution.items())

print(f"Optimal x: {x}")
