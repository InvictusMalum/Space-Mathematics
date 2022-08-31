from Vector3 import Vector3
import math
from functions import distance


## Problem 1
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
    
print(rot3D(Vector3(2.03,-2.81,.336), Vector3(0,0,-28*math.pi/180)).roundedVec(3))
    
## Problem 2