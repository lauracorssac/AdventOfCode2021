import sys

def get_inputs():
    if len(sys.argv) < 3:
        return None
    return (sys.argv[1], sys.argv[2])

def parse_dots(lines):

    x = []
    y = []

    for line in lines:
        components = line.strip().split(',')
        if len(components) < 2:
            break
            
        x.append(int(components[0]))
        y.append(int(components[1]))
        
    return (x,y)
    
def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end= " ")
        print()
    
def build_matrix(max_x, max_y, x, y):

    cols = max_x + 1
    lines = max_y + 1
    
    matrix = [[0] * cols for _ in range(lines)]
    
    for xcoor, ycoord in zip(x,y):
        matrix[ycoord][xcoor] = 1
    return matrix

def make_x_fold(matrix, index, matrix_width, matrix_height):
    
    counter = 0
    
    left_side_width = index
    right_side_width = matrix_width - index - 1
    
    non_intersected_col = right_side_width - left_side_width
    
    rightmost_intersected_col = matrix_width - 1 if non_intersected_col <= 0 else index + index
    for y in range(0, matrix_height):
        for x in range(index+1,rightmost_intersected_col+1):
            
            diff_from_index = x - index
            counter += int(matrix[y][index - diff_from_index] or matrix[y][x])
    
    remaining_cols = matrix_width - (index+index+1)
    
    for y in range(0, matrix_height):
        for x in range(index+index+1, matrix_width):
            counter += matrix[y][x]
            
    return counter
    
def concat_x(matrix_height, left_side, right_side):
    
    for line in range(0, matrix_height):
        left_side[line] += right_side[line]
        
    return left_side

def make_x_fold_question_2(matrix, index, matrix_width, matrix_height):
    
    left_side_width = index
    right_side_width = matrix_width - index - 1
    
    non_intersected_col = right_side_width - left_side_width
    
    rightmost_intersected_col = matrix_width - 1 if non_intersected_col <= 0 else index + index
    for y in range(0, matrix_height):
        for x in range(index+1,rightmost_intersected_col+1):
            
            diff_from_index = x - index
            matrix[y][index - diff_from_index] = int(matrix[y][index - diff_from_index] or matrix[y][x])
    
    #flip rest
    remaining_cols = matrix_width - (index+index+1)
    for y in range(0, matrix_height):
        for x in range(index+index + 1, index+index + 1 + (remaining_cols//2)):
            temp = matrix[y][x]
            matrix[y][x] = matrix[y][x+remaining_cols -1]
            matrix[y][x+remaining_cols -1] = temp
    
    new_matrix = concat_x(matrix_height, [row[index+index+1:] for row in matrix],[row[:index] for row in matrix])

    return new_matrix

def make_y_fold_question_2(matrix, index, matrix_width, matrix_height):
    
    upper_height = index
    lower_height = matrix_height - index - 1
    
    non_intersected_lines = lower_height - upper_height
    intersected_lines = min(upper_height, lower_height)
    
    last_intersected_line = matrix_height - 1 if non_intersected_lines <= 0 else index + index
    
    for y in range(index-intersected_lines, intersected_lines+1):
        for x in range(0, matrix_width):
            matrix[y][x] = int(matrix[y][x] or matrix[index + index - y][x])
    
    remaining_lines = (matrix_height - 1 - last_intersected_line)
    
    for y in range(last_intersected_line+1, last_intersected_line+1 + remaining_lines//2):
        for x in range(0, matrix_width):
            temp = matrix[y][x]
            matrix[y][x] = matrix[y+ remaining_lines - 1][x]
            matrix[y+ remaining_lines - 1][x] = matrix[y][x]
    
    new_matrix = matrix[last_intersected_line+1:] + matrix[:index]
    return new_matrix
    
        
    
def make_first_fold(matrix_width, matrix_height, lines, matrix):

    instruction = lines.readline()
    components = instruction.split("=")
    if len(components) != 2:
        return
    index = int(components[1])
    axes = components[0][-1]
    
    print("index = ", index, "axes = ", axes)
    
    points = 0
    if axes == 'x':
        points = make_x_fold(matrix, index, matrix_width, matrix_height)
    elif axes == 'y':
        points = make_y_fold(matrix)
        
    print("points = ", points)
    
    return matrix
        
def solution1(lines):

    x, y = parse_dots(lines)
    
    max_x = max(x)
    max_y = max(y)
    matrix = build_matrix(max_x, max_y, x, y)
    
    print("original matrix")
    print_matrix(matrix)
    
    make_first_fold(max_x + 1, max_y + 1, lines, matrix)
    
def solution2(lines):

    x, y = parse_dots(lines)
    max_x = max(x)
    max_y = max(y)
    matrix = build_matrix(max_x, max_y, x, y)
    
    print("original matrix")
    print_matrix(matrix)
    
    for instruction in lines:
        components = instruction.split("=")
        if len(components) != 2:
            return
        index = int(components[1])
        axes = components[0][-1]
    
        if axes == 'x':
            matrix = make_x_fold_question_2(matrix, index, len(matrix[0]), len(matrix))
        elif axes == 'y':
            matrix = make_y_fold_question_2(matrix, index, len(matrix[0]), len(matrix))
    
    print("final matrix")
    print_matrix(matrix)

def main():
    file, question = get_inputs()
    if not question or not file:
        return
        
    lines = open(file, 'r')
    function = solution1 if int(question) == 1 else solution2
    function(lines)
    

main()
