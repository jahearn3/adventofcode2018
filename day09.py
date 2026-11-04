# Day 9: Marble Mania

import load_data as ld
import os
from collections import deque

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

n_players = int(data[0].split()[0])
last_marble_pts = int(data[0].split()[6])

scores = {}
circle = [0]
current_player = 1
current_marble_idx = 0
for i in range(1, last_marble_pts + 1):
    if i % 23 != 0:
        diff = len(circle) - (current_marble_idx + 2)
        if len(circle) == 1 or diff == 0:
            circle.append(i)
            current_marble_idx = len(circle) - 1
        elif diff == -1:
            circle.insert(1, i)
            current_marble_idx = 1
        else:
            circle.insert(current_marble_idx + 2, i)
            current_marble_idx = current_marble_idx + 2
        current_marble = i
    else:
        if current_player not in scores:
            scores[current_player] = 0
        scores[current_player] += i
        # print(f"Player {current_player} get {i} points")
        # Find marble 7 spaces ccw
        remove_idx = (current_marble_idx - 7) % len(circle)
        bonus_marble = circle.pop(remove_idx)
        # Add it to their score
        scores[current_player] += bonus_marble
        # print(f"Player {current_player} get {bonus_marble} points")
        # Remove it from circle
        current_marble_idx = remove_idx % len(circle)
        current_marble = circle[current_marble_idx]
    # print(current_player, circle, current_marble, current_marble_idx)
    current_player += 1
    if current_player > n_players:
        current_player = 1

hi = 0
for k, v in scores.items():
    if v > hi:
        hi = v

print(hi)

# Part 2
last_marble_pts *= 100  # multiply the last marble points by 100
circle = deque([0])
scores = [0] * n_players

for marble in range(1, last_marble_pts + 1):
    if marble % 23 != 0:
        circle.rotate(-1)
        circle.append(marble)
    else:
        circle.rotate(7)
        player = (marble - 1) % n_players
        scores[player] += marble + circle.pop()
        circle.rotate(-1)

print(max(scores))
