import os

f = open(F"{os.getcwd()}/Day3/input.txt", "r")

lines = f.readlines()

gamma = ""

# for i in range(len(lines[0]) - 1):
#     count_0 = 0
#     count_1 = 0
#     for line in lines:
#         if int(line[i]) == 1:
#             count_1 += 1
#         else:
#             count_0 += 1
#     if count_1 > count_0:
#         gamma += "1"
#     else:
#         gamma += "0"

# print(gamma)
# print(int(gamma, 2))

# epsilon = gamma.replace('1','2').replace('0','1').replace('2','0')

# print(epsilon)
# print(int(epsilon, 2))

# print(int(gamma, 2) * int(epsilon, 2))

# Part 2 comes tommorow
found = False
i = 0
while(not found):

    filterchar = ""
    count_0 = 0
    count_1 = 0
    for line in lines:
        if int(line[i]) == 1:
            count_1 += 1
        else:
            count_0 += 1
    if count_1 < count_0: # >= for first value < for second value
        filterchar = "1"
    else:
        filterchar = "0"

    filtered = filter(lambda line: line[i] == filterchar, lines)
    lines = list(filtered)
    i += 1
    if len(lines) == 1:
        found = True

print(int(lines[0],2))












f.close()
