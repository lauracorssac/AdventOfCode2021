
def find_total(day, initial_ages):

    n_fishes = len(initial_ages)
    a = len()
    number_closed_cicle = int(day / 7)
    rest = day - number_closed_cicle * 7

    for i in range(0, number_closed_cicle):
        n_fishes += n_fishes

    extra_fish_minimal_age = rest - 1
    extra_fishes = filter(lambda x: x <= extra_fish_minimal_age, initial_ages)
    n_extra_fishes = len(extra_fishes)
    
    for fish in extra_fishes:
        if fish < rest - 2:
            n_extra_fishes += number_closed_cicle
    
    return n_extra_fishes

file = open('input.txt', 'r')
line = file.readline()
initial_ages = list(map(int(line.split(','))))
print("Problem 1 = ", find_total(80, initial_ages))

