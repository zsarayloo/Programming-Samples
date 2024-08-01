

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



