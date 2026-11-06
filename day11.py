# Day 11: Chronal Charge

import os
import numpy as np

f = os.path.basename(__file__)
day = f[3:5]

grid_serial_number = 8
grid_serial_number = 18
grid_serial_number = 42
grid_serial_number = 7857

size = 300
grid = np.zeros((size, size))

# populate grid
for i in range(size):
    x = i + 1
    rack_id = x + 10
    for j in range(size):
        y = j + 1
        power_level = rack_id * y
        power_level += grid_serial_number
        power_level *= rack_id
        if power_level < 100:
            power_level = -5
        else:
            # get hundreds digit
            hundreds_digit = int(str(power_level)[-3])
            power_level = hundreds_digit - 5
        grid[i][j] = power_level

# loop through grid to calculate power in each 3x3 square
max_power, max_x, max_y = 0, 0, 0
for i in range(size - 2):
    for j in range(size - 2):
        total_power = 0
        for ii in range(3):
            for jj in range(3):
                total_power += grid[i+ii][j+jj]
        if total_power > max_power:
            max_power = total_power
            max_x = i + 1
            max_y = j + 1

print(max_x, max_y)
