import queue
import sys

MIN_TEMPLATE_LENGTH = 2

def get_number_gets(initial_chars, steps):
    number_gets = 0
    for i in range(1, steps + 1):
        number_gets += (len(initial_chars) - 1) * pow(2, i - 1)
    return number_gets
    

def make_pairs_dic(pairs_lines):
    
    pairs_dic = {}
    
    for line in pairs_lines:
        components = line.strip().split(" -> ")
        pairs_dic[components[0]] = components[1]
    
    return pairs_dic
    
def insert_char_on_dic(dic, char):
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1
        
def get_difference_max_min(char_dic):

    min_occurence = float("inf")
    max_occurence = -float("inf")
    
    for char, occurence in char_dic.items():
        if occurence < min_occurence:
            min_occurence = occurence
        if occurence > max_occurence:
            max_occurence = occurence
    
    return max_occurence - min_occurence


def solution_1(file, steps):
    initial_chars = file.readline().strip()
    file.readline()
    pairs_dic = make_pairs_dic(file)
    final_number_gets = get_number_gets(initial_chars, steps)
    
    if len(initial_chars) < MIN_TEMPLATE_LENGTH:
        raise
    
    char_counter = {}
    
    pairs_queue = queue.Queue()
    
    for char in initial_chars:
        insert_char_on_dic(char_counter, char)

    pairs_gotten = 0
    for ind, char in enumerate(initial_chars[:-1]):
        pairs_queue.put(char + initial_chars[ind + 1])
            
    while pairs_gotten < final_number_gets:
        pair = pairs_queue.get()
        new_letter = pairs_dic[pair]
        pairs_queue.put(pair[0]+new_letter)
        pairs_queue.put(new_letter+pair[1])
        insert_char_on_dic(char_counter, new_letter)
        pairs_gotten += 1
    
    return get_difference_max_min(char_counter)
    
        
def main():

    if len(sys.argv) < 4:
        print("arguments missing!")
    
    filename = sys.argv[1]
    steps = int(sys.argv[3])
    f = open(filename, "r")
    question = solution_1 if int(sys.argv[2]) == 1 else solution_2
    print("Final Result =", question(f, steps))
    
    

main()
