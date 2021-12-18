import operator

def invert(number_char): 
    return '1' if number_char == '0' else '0'

def problem_one(lines, n_columns, n_lines):
    one_counter = [0] * n_columns
    for line in lines:
        for i in range(0, n_columns):
            one_counter[i] += 1 if line[i] == '1' else 0
    
    gamma_rate = ['0'] * n_columns
    for i in range(0, n_columns):
        gamma_rate[i] = '1' if one_counter[i] > n_lines/2 else '0'
    
    epslon_rate = list(map(invert, gamma_rate))
    epslon_rate = ''.join(epslon_rate)
    gamma_rate = ''.join(gamma_rate)
    gama_rate_dec = int(gamma_rate, 2)
    epslon_rate_dec = int(epslon_rate, 2)
    return epslon_rate_dec * gama_rate_dec

def get_most_commom(lines, n_lines, index):
    
    one_counter = 0
    for line in lines:
        one_counter += 1 if line[index] == '1' else 0
    
    return '1' if one_counter >= n_lines/2 else '0'

def filter_all(n_columns, n_lines, lines, operator):
    i = 0
    while i < n_columns and n_lines > 1:
        most_common = get_most_commom(lines, n_lines, i)
        lines = list(filter(lambda x: operator(x[i], most_common), lines))
        n_lines = len(lines)
        i += 1
    
    final_string = lines[0]
    return int(final_string, 2)

def problem_two(lines, n_columns, n_lines):

    oxigen_gen = filter_all(n_columns, n_lines, lines, operator.eq)
    carbon_scrub = filter_all(n_columns, n_lines, lines, operator.ne)
    return oxigen_gen * carbon_scrub

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

print(problem_one(lines, 12, len(lines)))
print(problem_two(lines, 12, len(lines)))
