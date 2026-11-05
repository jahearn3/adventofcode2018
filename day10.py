# Day 10: The Stars Align

import load_data as ld
import os
import re

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

lights = []
for line in data:
    coords = re.findall(r"<\s*(-?\d+\.?\d*)\s*,\s*(-?\d+\.?\d*)\s*>", line)
    positions = [int(coords[0][0]), int(coords[0][1])]
    velocities = [int(coords[1][0]), int(coords[1][1])]
    lights.append([positions[0], positions[1], velocities[0], velocities[1]])


def get_bounding_box(lights):
    min_x, max_x, min_y, max_y = None, None, None, None
    for light in lights:
        x, y = light[0], light[1]
        if min_x is None or x < min_x:
            min_x = x
        if max_x is None or x > max_x:
            max_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_y is None or y > max_y:
            max_y = y
    return min_x, max_x, min_y, max_y


def print_message(lights, output_file=None):
    min_x, max_x, min_y, max_y = get_bounding_box(lights)
    x_shifted = []
    y_shifted = []
    for light in lights:
        x, y = light[0], light[1]
        x_shifted.append(x - min_x)
        y_shifted.append(y - min_y)
    message = []
    for j in range(1 + max_y - min_y):
        row = ''
        for i in range(1 + max_x - min_x):
            char = '.'
            for x_s, y_s in zip(x_shifted, y_shifted):
                if i == x_s and j == y_s:
                    char = '#'
            row += char
        message.append(row)

    if output_file:
        with open(output_file, 'w') as f:
            for row in message:
                f.write(row + '\n')
        print(f'Message written to {output_file}')
    else:
        for row in message:
            print(row)


t = 0
min_area = float('inf')
best_t = 0
best_lights = lights[:]

# Find when the bounding box area is minimal
for iteration in range(20000):  # Reasonable upper bound
    min_x, max_x, min_y, max_y = get_bounding_box(lights)
    area = (max_x - min_x) * (max_y - min_y)

    if area < min_area:
        min_area = area
        best_t = t
        best_lights = [light[:] for light in lights]

    if area > min_area + 1000:  # Stop if area grows significantly
        break

    # Increase time
    t += 1
    # Update positions
    new_lights = []
    for light in lights:
        x, y, vx, vy = light
        light = [x + vx, y + vy, vx, vy]
        new_lights.append(light)
    lights = new_lights

print(f'Message at t = {best_t}')
print(f'Bounding box area: {min_area}')
print_message(best_lights, output_file='data/day10_output.txt')
