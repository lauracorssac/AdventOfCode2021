import re

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

x_position = 0
depth = 0

for line in lines:
    components = line.split(' ')
    command = components[0]
    command_value = int(components[1])

    if command == "forward":
        x_position += command_value
    elif command == "up":
        depth -= command_value
    elif command == "down":
        depth += command_value
    
print("solution 1 = ", x_position * depth)

aim = 0
x_position = 0
depth = 0

for line in lines:
    components = line.split(' ')
    command = components[0]
    command_value = int(components[1])

    if command == "forward":
        x_position += command_value
        depth += command_value * aim
    elif command == "up":
        aim -= command_value
    elif command == "down":
        aim += command_value

print("solution 2 = ", x_position * depth)



