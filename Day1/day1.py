import os

f = open(F"{os.getcwd()}/Day1/input.txt", "r")

lines = f.readlines()

previous_value = 0
count = 0
max_count = 0

# Part 1
# for line in lines:
#     if int(line) > previous_value:
#         count += 1
#     previous_value = int(line)
#     # else:
#     #     if max_count < count:
#     #         max_count = count
#     #     count = 0
# print(max_count)
# print(count)

#Part 2

i = 0

while i < (len(lines) - 3):
    first_set = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    second_set = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
    i += 1
    if second_set > first_set:
        count += 1

print(count)



f.close()
