
file = open('input.txt', 'r')
lines = list(map(int, file.readlines()))
number_of_lines = len(lines)

previous = lines[0]
increase_counter_1 = 0

for line in lines[1:]:
    if line > previous:
        increase_counter_1 += 1
    previous = line

print("counter 1 = ",  increase_counter_1)

previous_sum = sum(lines[0:3])
increase_counter_2 = 0

for line in range(1,number_of_lines-2):
    current_sum = sum(lines[line:line+3])
    if current_sum > previous_sum:
        increase_counter_2 += 1
    previous_sum = current_sum

print("counter 2 = ", increase_counter_2)


