from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = file.read().split("\n")

position = 0
depth = 0
for line in lines:
    match line.split(" "):
        case ["forward", value]:
            position += int(value)
        case ["down", value]:
            depth += int(value)
        case ["up", value]:
            depth -= int(value)
            
print("Part One: {}".format(position * depth))

position = 0
depth = 0
aim = 0
for line in lines:
    match line.split(" "):
        case ["forward", value]:
            position += int(value)
            depth += aim * int(value)
        case ["down", value]:
            aim += int(value)
        case ["up", value]:
            aim -= int(value)
            
print("Part One: {}".format(position * depth))