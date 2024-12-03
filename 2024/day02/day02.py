from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

import numpy as np

def check_report(report: np.array):
    is_first = True
    is_decreasing = True
    for i in range(len(report)):
        if is_first:
            if report[i] < report[i+1]:
                is_decreasing = False
            is_first = False
            continue
        
        if is_decreasing and report[i-1] < report[i]:
            break
        elif not is_decreasing and report[i-1] > report[i]:
            break
        
        diff = abs(report[i-1] - report[i])
        if diff == 0 or diff > 3:
            break
        
        if i == len(report)-1:
            return True
    return False

lines = file.read().split("\n")

total_sum = 0
for line in lines:
    report = np.array(list(map(int, line.split(" "))))
    
    if check_report(report):
        total_sum += 1

print("Part One: {}".format(total_sum))

total_sum = 0
for line in lines:
    report = np.array(list(map(int, line.split(" "))))
    
    if check_report(report):
        total_sum += 1
        continue
    
    for i in range(len(report)):
        new_report = np.delete(report, i)
        
        if check_report(new_report):
            total_sum += 1
            break

print("Part Two: {}".format(total_sum))