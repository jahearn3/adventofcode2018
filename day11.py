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


def populate_grid(size):
    grid = np.zeros((size, size))
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
    return grid


def find_max_power(summed, square_size=3):
    max_power, max_square_size, max_x, max_y = 0, 0, 0, 0
    for i in range(size - (square_size - 1)):
        for j in range(size - (square_size - 1)):
            # total_power = 0
            # for ii in range(square_size):
            #     for jj in range(square_size):
            #         total_power += grid[i+ii][j+jj]
            total_power = (
                summed[i + square_size, j + square_size]
                - summed[i, j + square_size]
                - summed[i + square_size, j]
                + summed[i, j]
            )

            if total_power > max_power:
                max_power = total_power
                max_square_size = square_size
                max_x = i + 1
                max_y = j + 1
    return max_power, max_square_size, max_x, max_y


# Set up grid and zero-padded table
grid = populate_grid(size)
summed = np.zeros((size + 1, size + 1))
summed[1:, 1:] = grid.cumsum(axis=0).cumsum(axis=1)

# Part 1
max_power, max_square_size, max_x, max_y = find_max_power(summed)
print(max_x, max_y)

# Part 2
max_power_, max_square_size_, max_x_, max_y_ = 0, 0, 0, 0
for square_size in range(1, 301):
    max_power, max_square_size, max_x, max_y = find_max_power(
        summed, square_size=square_size
        )
    if max_power > max_power_:
        max_power_ = max_power
        max_square_size_ = max_square_size
        max_x_ = max_x
        max_y_ = max_y

print(max_x_, max_y_, max_square_size_)
