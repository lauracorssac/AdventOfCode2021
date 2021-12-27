
def find_total(fishes, final_day):

    if not fishes: 
        return 0

    fish_age = fishes[0][0]
    fish_birthday = fishes[0][1]
    quantity = fishes[0][2]
    day_next_birth = fish_birthday + fish_age + 1

    children_counter = 0
    while day_next_birth <= final_day:
        children_counter += quantity
        fishes.append((8,day_next_birth, quantity))
        day_next_birth += 7
    
    return children_counter + find_total(fishes[1:], final_day)
    


def pre_process_input(initial_ages):
    dic = {}
    for age in initial_ages:
        if age not in dic:
            dic[age] = 1
        else:
            dic[age] += 1
    return [(x, 0, dic[x]) for x in dic]
        
file = open('input.txt', 'r')
line = file.readline()
initial_ages = list(map(int, line.split(',')))
final_day = 30
initial_ages_len = len(initial_ages)
initial_ages = pre_process_input(initial_ages)
print(initial_ages)
print("Problem 1 = ",  initial_ages_len + find_total(initial_ages, final_day))

