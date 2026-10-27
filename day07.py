# Day 7: The Sum of Its Parts

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

prerequisites = {}

for line in data:
    words = line.split()
    prerequisite = words[1]
    step = words[7]

    prerequisites.setdefault(prerequisite, set())
    prerequisites.setdefault(step, set())
    prerequisites[step].add(prerequisite)

remaining = set(prerequisites)
completed = set()
order = []

while remaining:
    available = [
        step for step in remaining
        if prerequisites[step].issubset(completed)
    ]
    if not available:
        raise ValueError("No available step: dependencies contain a cycle")
    step = min(available)
    remaining.remove(step)
    completed.add(step)
    order.append(step)

print("".join(order))

# Part 2
t = 0
remaining = set(prerequisites)
in_progress = {}
completed = set()
n_workers = 5  # 2 for example, 5 for puzzle
base_time = 60  # 0 for example, 60 for puzzle


while remaining or in_progress:
    available = sorted(
        step for step in remaining
        if prerequisites[step].issubset(completed)
    )
    free_workers = n_workers - len(in_progress)
    for step in available[:free_workers]:
        remaining.remove(step)
        duration = base_time + ord(step) - ord('A') + 1
        in_progress[step] = t + duration
    if not in_progress:
        raise ValueError("No available step: dependencies contain a cycle")
    t = min(in_progress.values())
    finished = [
        step for step, finish_time in in_progress.items()
        if finish_time == t
    ]
    for step in finished:
        completed.add(step)
        del in_progress[step]

print(t)
