# Day 4: Repose Record

import load_data as ld
import os
import numpy as np

f = os.path.basename(__file__)
day = f[3:5]

# data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

sleep_times = {}
for line in data:
    contents = line.split()
    date = contents[0][1:].split('-')
    month, day = int(date[1]), int(date[2])
    time = contents[1].strip(']').split(':')
    event = contents[2:]
    if time[0] == '23':
        if day < 28:
            day += 1
        elif month == 2:
            month += 1
            day = 1
        elif day in [28, 29]:
            day += 1
        elif day == 31:
            month += 1
            day = 1
        elif day == 30:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                day += 1
            else:
                month += 1
                day = 1
        else:
            print(f"Unexpected date: month={month}, day={day}")
        if month == 13:
            month = 1
    if (month, day) not in sleep_times:
        sleep_times[(month, day)] = {"guard": 0, "awake": [], "asleep": []}
    if event[0] == "Guard":
        sleep_times[(month, day)]["guard"] = int(event[1].strip('#'))
    elif event[0] == "wakes":
        sleep_times[(month, day)]["awake"].append(int(time[1]))
    elif event[0] == "falls":
        sleep_times[(month, day)]["asleep"].append(int(time[1]))

guards = {}
for k, v in sleep_times.items():
    if v["guard"] not in guards:
        guards[v["guard"]] = 0
    assert len(v["awake"]) == len(v["asleep"])
    sorted_sleep = sorted(v["asleep"])
    sorted_wake = sorted(v["awake"])
    for i in range(len(sorted_sleep)):
        guards[v["guard"]] += sorted_wake[i] - sorted_sleep[i]

max_sleep_time = 0
max_sleep_guard = 0
for k, v in guards.items():
    if v > max_sleep_time:
        max_sleep_time = v
        max_sleep_guard = k

minutes = np.zeros(60)
for k, v in sleep_times.items():
    if v["guard"] == max_sleep_guard:
        sorted_sleep = sorted(v["asleep"])
        sorted_wake = sorted(v["awake"])
        for i in range(len(sorted_sleep)):
            for j in range(sorted_sleep[i], sorted_wake[i]):
                minutes[j] += 1
print(max_sleep_guard * np.argmax(minutes))

# Part 2
guard_sleep_minutes = {}
for k, v in sleep_times.items():
    if v["guard"] not in guard_sleep_minutes:
        guard_sleep_minutes[v["guard"]] = []
    sorted_sleep = sorted(v["asleep"])
    sorted_wake = sorted(v["awake"])
    for i in range(len(sorted_sleep)):
        for j in range(sorted_sleep[i], sorted_wake[i]):
            guard_sleep_minutes[v["guard"]].append(j)

mode_sleep_time = 60
mode_sleep_amount = 0
mode_sleep_guard = 0
for k, v in guard_sleep_minutes.items():
    if len(v) > 0:
        counts = np.bincount(v)
        mode = np.argmax(counts)
        amount = counts[mode]
        if amount > mode_sleep_amount:
            mode_sleep_amount = amount
            mode_sleep_time = mode
            mode_sleep_guard = k

print(mode_sleep_guard * mode_sleep_time)
