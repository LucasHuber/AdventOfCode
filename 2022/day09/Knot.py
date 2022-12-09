class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)
    
sign = lambda x: 1 if x > 0 else ( -1 if x < 0 else 0 )

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
        
        if (0 <= abs(dx) <= 1 and 0 <= abs(dy) <= 1):   # follow_vector still connected to knot
            return
        else:
            self.move(Vector(sign(dx), sign(dy)))
