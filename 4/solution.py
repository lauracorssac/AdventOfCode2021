class NumberInfo:
    def __init__(self, l, c, marked):
        self.l = l
        self.c = c
        self.marked = marked
        
class MatrixInfo:
    def __init__(self, numbers_dic, line_control, column_control, won=False):
        self.numbers_dic = numbers_dic
        self.line_control = line_control
        self.column_control = column_control
        self.won = won

def transform_line(line):
    return line.strip().split()

def process_matrix(matrix, n_lines, n_columns):
    dic = { }
    matrix = list(map(transform_line, matrix))
    for line in range(0, n_lines):
        for column in range(0, n_columns):
            number = matrix[line][column]
            dic[number] = NumberInfo(line, column, False)
    matrix_info = MatrixInfo(dic, [0] * n_lines, [0] * n_columns)
    return matrix_info

def update_and_check_matrix(matrix_info, number, n_lines, n_columns):
    
    if number in matrix_info.numbers_dic:
        number_info = matrix_info.numbers_dic[number]
        matrix_info.numbers_dic[number].marked = True
        
        matrix_info.line_control[number_info.l] += 1
        matrix_info.column_control[number_info.c] += 1

        if (matrix_info.line_control[number_info.l] == n_lines or 
        matrix_info.column_control[number_info.c] == n_columns):
            return True
    return False

def get_sum_not_marked(matrix_info):
    total = 0
    for number in matrix_info.numbers_dic:
        if not matrix_info.numbers_dic[number].marked:
            total += int(number)
    return total

def check_winner(drawn_numbers, matrix_infos, n_lines, n_columns):
    for number in drawn_numbers:
        for matrix_info in matrix_infos:
            if update_and_check_matrix(matrix_info, number, n_lines, n_columns):
                return get_sum_not_marked(matrix_info) * int(number)
    return None

def check_loser(drawn_numbers, matrix_infos, n_lines, n_columns):

    n_matrices = len(matrix_infos)
    n_winners = 0

    for number in drawn_numbers:
        for matrix_info in matrix_infos:
            if not matrix_info.won:
                if update_and_check_matrix(matrix_info, number, n_lines, n_columns):
                    n_winners += 1
                    matrix_info.won = True
                if n_winners == n_matrices:
                    return get_sum_not_marked(matrix_info) * int(number)
    


file = open('input.txt', 'r')
lines = file.readlines()
file.close()
n_lines = 5
n_columns = 5

matrix_infos = []
i = 2
while i < len(lines):
    matrix = lines[i:i+n_lines]
    matrix_info = process_matrix(matrix, n_lines, n_columns)
    matrix_infos.append(matrix_info)
    i += n_lines + 1

drawn_numbers = lines[0].split(',')
#print("solution P1 = ", check_winner(drawn_numbers, matrix_infos, n_lines, n_columns))
print("solution P2 = ", check_loser(drawn_numbers, matrix_infos, n_lines, n_columns))








