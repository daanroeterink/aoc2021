import os

f = open(F"{os.getcwd()}/Day2/input.txt", "r")

lines = f.readlines()

forward_position = 0
depth = 0
aim = 0

for line in lines:
    if "forward" in line:
        forward_position += int(line.split()[1])
        # part 2 for part 1 disable line 15 and enable 17, 20
        depth += (aim * int(line.split()[1]))
    elif "up" in line:
        # depth -= int(line.split()[1])
        aim -= int(line.split()[1])
    elif "down" in line:
         #depth += int(line.split()[1])
         aim += int(line.split()[1])

print(forward_position * depth)

f.close()
