# Solved using Breath-First Search
from collections import deque
from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

grid = [list(x) for x in file.read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr, sc = r, c
            grid[r][c] = "a"
        elif item == "E":
            er, ec = r, c
            grid[r][c] = "z"

q = deque()
q.append((0, sr, sc))

vis = {(sr, sc)}

while q:
    d, r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if (nr, nc) in vis:
            continue
        if (ord(grid[nr][nc]) - ord(grid[r][c])) > 1:
            continue
        if nr == er and nc == ec:
            print(d + 1)
            q.clear()
            break
        q.append((d + 1, nr, nc))
        vis.add((nr, nc))

# --------------------------------------------------

# In reverse - From 'E' till first 'a'
file = open(path.join(path.dirname(__file__), "input.txt"))
grid = [list(x) for x in file.read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            grid[r][c] = "a"
        elif item == "E":
            er, ec = r, c
            grid[r][c] = "z"

q = deque()
q.append((0, er, ec))

vis = {(er, ec)}

while q:
    d, r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if (nr, nc) in vis:
            continue
        if (ord(grid[nr][nc]) - ord(grid[r][c])) < -1:
            continue
        if grid[nr][nc] == "a":
            print(d + 1)
            q.clear()
            break
        q.append((d + 1, nr, nc))
        vis.add((nr, nc))