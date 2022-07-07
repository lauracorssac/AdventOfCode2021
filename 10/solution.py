import sys, os

opening = ['{','[', '(', '<']
closing = {
'}' : 0,
']': 1,
')': 2,
'>': 3
}

points = {
')': 3,
']': 57,
'}': 1197,
'>': 25137
}

points_q2 = {
'(': 1,
'[': 2,
'{': 3,
'<': 4
}

def get_file_input():
    if len(sys.argv) < 2:
        raise
    return sys.argv[1]

def get_question_input():
    if len(sys.argv) < 3:
        raise
    return sys.argv[2]

def get_score_for_line_q1(line):
    
    stack = []
    
    for char in line:
        
        if char in opening:
            stack.append(char)
            continue
        
        if char in closing:
            last_opening = stack.pop()
            if last_opening != opening[closing[char]]:
                # mismatch
                return points[char]
        else:
            # invalid char
            return 0
    
    # correct or incomplete
    return 0
        
def get_score_for_line_q2(line):

    stack = []
    
    for char in line:
        
        if char in opening:
            stack.append(char)
            continue
        
        if char in closing:
            last_opening = stack.pop()
            if last_opening != opening[closing[char]]:
                # mismatch
                return 0
        else:
            # invalid char
            
            return 0
    
    points = 0
    for remaining in stack[::-1]:
        points *= 5
        points += points_q2[remaining]
    return points
    
            
def parse_lines_q1(lines):
    
    total_points = 0
    
    for line in lines:
        print(total_points)
        total_points += get_score_for_line_q1(line.strip())
   
    return total_points
    
def parse_lines_q2(lines):
    
    total_points = []
    
    for line in lines:
        total = get_score_for_line_q2(line.strip())
        if total > 0:
            total_points.append(total)
    
    total_points.sort()
   
    return total_points[len(total_points) // 2]

        
def main():

    file = get_file_input()
    f = open(file, "r")
    question = int(get_question_input())
    parse_function = parse_lines_q1 if question == 1 else parse_lines_q2
    total = parse_function(f)
    
    print("The total points was = ", total)

main()

