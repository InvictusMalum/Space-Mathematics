import math

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
    

    def __sub__(self, other):
        return Vector3(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def __mul__(self, other):
        assert not(isinstance(other, Vector3))
        
        return Vector3(self.x*other, self.y*other, self.z*other)

    def __imul__(self, other):
        assert not(isinstance(other, Vector3))

        self.x *= other
        self.y *= other
        self.z *= other

    def roundedVec(self, figs=None):
        return Vector3(round(self.x, figs), round(self.y, figs), round(self.z, figs))
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    
    def getMagnitude(self):
        return math.sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))
    
