import math

def get_size_basin(matrix, line, column, max_int):
    print("recursion for", matrix[line][column], "line", line, "col", column)
    if matrix[line][column] == 9 or matrix[line][column] == max_int or matrix[line][column] == -1:
        return 0
    matrix[line][column] = -1
    return 1 + get_size_basin(matrix, line, column -1, max_int) + \
    get_size_basin(matrix, line, column + 1, max_int) + \
    get_size_basin(matrix, line - 1, column, max_int) + \
    get_size_basin(matrix, line + 1, column, max_int)

def update_largest(three_largest_basins, number):
    if number <= three_largest_basins[2]:
        return three_largest_basins
    if number >= three_largest_basins[0]:
        three_largest_basins.insert(0, number)
    elif number >= three_largest_basins[1]:
        three_largest_basins.insert(1, number)
    else:
        three_largest_basins.insert(2, number)
    del three_largest_basins[3]
    return three_largest_basins

def get_basins(matrix, n_lines, n_cols, max_int):

    three_largest_basins = [0,0,0]

    for line in range(1, n_lines - 1):
        for col in range(1, n_cols -1):
            if matrix[line][col] != -1 and matrix[line][col] != 9:
                basin_size = get_size_basin(matrix, line, col, max_int)
                three_largest_basins = update_largest(three_largest_basins, basin_size) 
               
    return math.prod(three_largest_basins)

def count_low(matrix, n_lines, n_cols):
    low_counter = 0
    low_value_accumulator = 0
    for line in range(1, n_lines - 1):
        for col in range(1, n_cols -1):
            if (matrix[line][col] < matrix[line-1][col] and 
            matrix[line][col] < matrix[line+1][col] and 
            matrix[line][col] < matrix[line][col-1] and 
            matrix[line][col] < matrix[line][col+1]):
                low_counter += 1
                low_value_accumulator += matrix[line][col]
    return low_counter + low_value_accumulator

file = open('input.txt', 'r')
lines = file.readlines()
file.close()
max_int = 10
n_cols = len(lines[0].strip()) + 2
matrix = [[max_int] * (n_cols + 2)]
for line in lines:
    line_list = [max_int]
    line_list += list(map(int, line.strip()))
    line_list.append(max_int)
    matrix.append(line_list)

matrix.append([max_int] * (n_cols + 2))
n_lines = len(matrix)
print("Problem 1 = ", count_low(matrix, n_lines, n_cols))
print("Problem 2 = ", get_basins(matrix, n_lines, n_cols, max_int))

