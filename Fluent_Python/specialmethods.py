# Understanding  special methods for the class Vector. (Operator Overloading)
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self): # sets printout form of the object.
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self): # returns magnitude.
        return math.hypot(self.x, self.y)
    
    def __bool__(self): # returns boolean value.
        return bool(self.x or self.y)
    
    def __add__(self, other): # '+' operator will call this method.
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar): # '*' operator will cal this method.
        return Vector(self.x * scalar, self.y * scalar)