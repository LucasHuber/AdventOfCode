class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)
             
class Knot:
    def __init__(self, vector: Vector) -> None:
        self.vec = vector
        self.visited_positions = set()
        self.visited_positions.add(str(self.vec))
        
    def move(self, dir: Vector):
        self.vec.x += dir.x
        self.vec.y += dir.y
        self.visited_positions.add(str(self.vec))
    
    def follow(self, follow_vector: Vector):
        dx = follow_vector.x - self.vec.x
        dy = follow_vector.y - self.vec.y
        
        if (0 <= abs(dx) <= 1 and 0 <= abs(dy) <= 1):
            return
        elif dx == 0:
            self.move(Vector(0, int(dy/2)))
        elif dy == 0:
            self.move(Vector(int(dx/2), 0))
        else:
            vec = Vector(0, 0)
            vec.x = 1 if dx > 0 else -1
            vec.y = 1 if dy > 0 else -1
            self.move(vec)
