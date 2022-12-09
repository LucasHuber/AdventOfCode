from os import path
file = open(path.join(path.dirname(__file__), "test.txt"))

from Knot import Vector, Knot

lines = file.read().split("\n")

dir = {
    "U": Vector(0, 1),
    "D": Vector(0, -1),
    "L": Vector(-1, 0),
    "R": Vector(1, 0)
}

Head = Knot(Vector(0, 0))
Tail = Knot(Vector(0 ,0))

for line in lines:
    direction, value = line.split(" ")
    for i in range(int(value)):
        Head.move(dir[direction])
        Tail.follow(Head.vec, dir[direction])

print(Tail.visited_positions)
print(len(Tail.visited_positions))