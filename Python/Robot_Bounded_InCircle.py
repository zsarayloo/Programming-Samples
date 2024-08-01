'''
## Problem :  On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
The north direction is the positive direction of the y-axis.    The south direction is the negative direction of the y-axis.
    The east direction is the positive direction of the x-axis.
    The west direction is the negative direction of the x-axis.

The robot can receive one of three instructions:

    "G": go straight 1 unit.
    "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
    "R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''


def isRobotBounded(instructions):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  
        dir_index = 0  

        for instruction in instructions:
            if instruction == 'G':
                x += directions[dir_index][0]
                y += directions[dir_index][1]
            elif instruction == 'L':
                dir_index = (dir_index - 1) % 4
            elif instruction == 'R':
                dir_index = (dir_index + 1) % 4

        return (x == 0 and y == 0) or (dir_index != 0)




Case1 = "GGLLGG"

print (isRobotBounded(Case1))



