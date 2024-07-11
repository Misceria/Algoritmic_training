
from math import fabs

def ManhattanDistance(coor_start, coor_end):
    return int(fabs(coor_start[0]-coor_end[0])+fabs(coor_start[1]-coor_end[1]))


print(ManhattanDistance((1, 2), (2, 1)))








