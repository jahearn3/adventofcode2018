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
