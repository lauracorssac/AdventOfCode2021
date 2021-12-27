def build_dic(initial_ages):
    dic = {}
    for age in initial_ages:
        if age not in dic:
            dic[age] = 1
        else:
            dic[age] += 1
    return dic

def pre_process_input(initial_ages, final_day, fish_counter_list):
    dic = build_dic(initial_ages)
    print(dic)
    for fish_age in dic:
        quantity = dic[fish_age]
        day_next_birth = fish_age + 1
        while day_next_birth <= final_day:
            fish_counter_list[day_next_birth] += quantity
            day_next_birth += 7
    
    return fish_counter_list

def find_total(final_day, fish_counter_list):

    for day in range(1, final_day + 1):
        quantity = fish_counter_list[day]
        if quantity == 0: 
            continue
        day_next_birth = day + 8 + 1
        while day_next_birth <= final_day:
            fish_counter_list[day_next_birth] += quantity
            day_next_birth += 7
    return fish_counter_list
        
file = open('input.txt', 'r')
line = file.readline()
initial_ages = list(map(int, line.split(',')))
final_day = 256
initial_ages_len = len(initial_ages)
fishes = [0] * (final_day + 1)
fishes[0] = initial_ages_len
fishes = pre_process_input(initial_ages, final_day, fishes)
print(fishes)
fishes = find_total(final_day, fishes)
print(fishes)
print("Problem 1 = ", sum(fishes))

