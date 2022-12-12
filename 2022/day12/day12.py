from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

# ----------------------------------------------------------------------------------------------------

from collections import deque

shortest_path = None

def find_neighbors(x, y):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(terrain[0]) - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(terrain) - 1:
        neighbors.append((x, y + 1))
    return neighbors

def walk(path):
    global shortest_path
    x, y = path[-1]
    if x == ex and y == ey:
        if shortest_path is None:
            shortest_path = len(path)
        elif len(path) < shortest_path:
            shortest_path = len(path)
        # return path
    for neighbor in find_neighbors(x, y):
        # print(abs(ord(terrain[y][x])), abs(ord(terrain[neighbor[1]][neighbor[0]])), abs(abs(ord(terrain[y][x])) - abs(ord(terrain[neighbor[1]][neighbor[0]]))))
        if neighbor not in path and abs(abs(ord(terrain[y][x])) - abs(ord(terrain[neighbor[1]][neighbor[0]]))) <= 1:
            path.append(neighbor)
            walk(path.copy())
            # if result:
            #     return result
            path.pop()
    return None

# ----------------------------------------------------------------------------------------------------

lines = file.read().strip().splitlines()

terrain = []

for row in range(len(lines)):
    terrain.append([])
    for col in range(len(lines[0])):
        terrain[row].append(lines[row][col])

sx, sy, ex, ey = 0, 0, 0, 0
for line in lines:
    if "S" in line:
        sy = lines.index(line)
        sx = line.index("S")
    if "E" in line:
        ey = lines.index(line)
        ex = line.index("E")


terrain[sy][sx] = "a"
terrain[ey][ex] = "z"

path = deque()
path.append((sx, sy))

walk(path)

print(shortest_path - 1)