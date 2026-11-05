# Day 10: The Stars Align

import load_data as ld
import os
import re
from collections import Counter

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


def print_message(lights):
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
    # print(min_x, max_x, min_y, max_y)
    x_shifted = []
    y_shifted = []
    for light in lights:
        x, y = light[0], light[1]
        x_shifted.append(x - min_x)
        y_shifted.append(y - min_y)
    # print(x_shifted, y_shifted)
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
    for row in message:
        print(row)


t = 0
keep_going = True
while keep_going:
    # Check for vertically connected lights
    x_positions = []
    for light in lights:
        x_positions.append(light[0])
    counter = Counter(x_positions)
    most_common_value, count = counter.most_common(1)[0]
    # print(most_common_value, count)
    if count >= 8:
        print('Message at t =', t)
        print_message(lights)
        keep_going = False

    # Increase time
    t += 1
    # Update positions
    new_lights = []
    for light in lights:
        x, y, vx, vy = light
        light = [x + vx, y + vy, vx, vy]
        new_lights.append(light)
    lights = new_lights
