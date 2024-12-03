from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

import re

text = file.read().replace("\n", "")

# text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, text)

total_sum = 0
for match in matches:
    numbers = re.findall(r"\d{1,3}", match)
    x, y = map(int, numbers)
    total_sum += x * y

print("Part One: {}".format(total_sum))

mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
state_pattern = r"do\(\)|don't\(\)"
matches = re.findall(f"{mul_pattern}|{state_pattern}", text)

mul_enabled = True
total_sum = 0
for match in matches:
    if match == "do()":
        mul_enabled = True
    elif match == "don't()":
        mul_enabled = False
    elif mul_enabled and match.startswith("mul"):
        numbers = re.findall(r"\d{1,3}", match)
        x, y = map(int, numbers)
        total_sum += x * y

print("Part Two: {}".format(total_sum))