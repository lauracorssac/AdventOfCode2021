def find_median(list):
    list.sort()
    median_index = int(len(list) / 2)
    return list[median_index]

def find_avg(list):
    return int(sum(list) / len(list))

def find_total_cost_alignment(align_pos, list):
    total_cost = 0
    for element in list:
        total_cost += abs(element - align_pos)
    return total_cost

file = open('input.txt')
lines = file.readline()
lines = list(map(int, lines.split(',')))
#median = find_median(lines)
avg = find_avg(lines)
#print("Problem 1 = ", find_total_cost_alignment(median, lines))
print("Problem 2 = ", find_total_cost_alignment(avg, lines))