import math
from functions import distance

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

    def rot3D(p1, rpy):
        rollTheta = math.atan2(p1.z,p1.y)
        dist = distance(p1.y,p1.z)
        pOut = Vector3(p1.x, dist*math.cos(rollTheta+rpy.x), dist*math.sin(rollTheta+rpy.x))
        
        pitchTheta = math.atan2(pOut.x,pOut.z)
        dist = distance(p1.z,p1.x)
        pOut = Vector3(dist*math.sin(pitchTheta+rpy.y), pOut.y, dist*math.cos(pitchTheta+rpy.y))
        
        yawTheta = math.atan2(pOut.y,pOut.x)
        dist = distance(p1.x,p1.y)
        pOut = Vector3(dist*math.cos(yawTheta+rpy.z), dist*math.sin(yawTheta+rpy.z), pOut.z)
        
        return pOut
    
