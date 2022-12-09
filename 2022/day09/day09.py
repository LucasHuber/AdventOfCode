from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

from Knot import Vector, Knot

lines = file.read().split("\n")

dir = {
    "U": Vector(0, 1),
    "D": Vector(0, -1),
    "L": Vector(-1, 0),
    "R": Vector(1, 0)
}

head = Knot(Vector(0, 0))
tail = Knot(Vector(0 ,0))

for line in lines:
    direction, value = line.split(" ")
    for i in range(int(value)):
        head.move(dir[direction])
        tail.follow(head.vec)

print("Part One: {}".format(len(tail.visited_positions)))

rope = [Knot(Vector(0, 0)) for _ in range(10)]

for line in lines:
    direction, value = line.split(" ")
    for i in range(int(value)):
        rope[0].move(dir[direction])
        for i in range(1, len(rope)):
            rope[i].follow(rope[i-1].vec)

print("Part Two: {}".format(len(rope[9].visited_positions)))