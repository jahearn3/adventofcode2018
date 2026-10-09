# Day 1: Chronal Calibration

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

# data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
freq = sum(int(line) for line in data)
print(freq)

# Part 2
prev = [0]
freq = 0
duplicate = False
i = 0
while duplicate is False:
    # Reset the index at 0 if we reach the end and haven't found the duplicate
    if i == len(data):
        i = 0
    # Modify the current frequency
    freq += int(data[i])
    # Check if the current frequency has been reached before
    if freq in prev:
        duplicate = True
    # Add current frequency to the history
    prev.append(freq)
    # Increase the counter for the next iteration
    i += 1

print(freq)
