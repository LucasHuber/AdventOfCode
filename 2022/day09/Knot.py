class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        print("({}, {})".format(self.x, self.y))
        return "({}, {})".format(self.x, self.y)
             
class Knot:
    def __init__(self, vector: Vector) -> None:
        self.vec = vector
        self.visited_positions = set()
        self.visited_positions.add(str(self.vec))
        
    def print_visited_positions(self) -> None:
        print("Start")
        for pos in self.visited_positions:
            print(pos)
        
    def move(self, dir: Vector):
        self.vec.x += dir.x
        self.vec.y += dir.y
        self.visited_positions.add(str(self.vec))
    
    def follow(self, head_vector: Vector, dir: Vector):
        dx = self.vec.x - head_vector.x
        dy = self.vec.y - head_vector.y
        
        if (dx == 0 and dy == 0) or (dx + dy <= 1 and dx + dy >= -1) or (dx == 1 and dy == 1) or (dx == -1 and dy == -1):
            return
        elif dx == 0 or dy == 0:
            self.move(dir)
        else:
            if dx < 0 or dy < 0:
                if dx < dy:
                    self.move(Vector(-1, 0))
                else:
                    self.move(Vector(0, -1))
            else:
                if dx > dy:
                    self.move(Vector(1, 0))
                else:
                    self.move(Vector(0, 1))

