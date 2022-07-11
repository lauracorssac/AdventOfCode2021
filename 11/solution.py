import sys
def get_file_input():
    if len(sys.argv) < 2:
        raise
    return sys.argv[1]

def get_question_input():
    if len(sys.argv) < 3:
        raise
    return sys.argv[2]

def q2(matrix):
    return

def q1(matrix):
    explosions = 0
    for step in range(1,11):
        
        for l in range(1, 11):
            for c in range(1,11):
            
                if matrix[l][c] == 9:
                    explosions += 1
                    
                    for la in range(l-1, l+2):
                        for ca in range(c-1, c+2):
                            matrix[la][ca]
            
                matrix[l][c] += 1
                
            
    
    return explosions
                
def print_matrix(matrix):
    for line in matrix:
        for col in line:
            print(col,end = " ")
        print()
    
    
def build_matrix(lines):
    matrix = []
    matrix.append([0] * 12)
    for line in lines:
        line = line.strip()
        line_array = [0]
        
        for col in line:
            line_array.append(col)
        
        line_array.append(0)
        matrix.append(line_array)
        
    matrix.append([0] * 12)
    return matrix
        
def main():

    file = get_file_input()
    f = open(file, "r")
    matrix = build_matrix(f)
    
    #question = int(get_question_input())
    #function = q1 if question == 1 else q2
    #total = parse_function(matrix)
    
    print(matrix)
    print_matrix(matrix)
    #print("The total points was = ", total)

main()
