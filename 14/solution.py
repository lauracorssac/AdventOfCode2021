import queue
import sys
import time

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
    
# an effitient alternative for solution 1
# space = pairs_dic + step_pairs + char_counter_dic
# O(26*26) + O(26*26) + O(1)
# the maximum number of pairs possible is 26*26 since there is only 26 letters in the alphabet

# if we couldnt assume that only capital letters were used...
# space = pairs_dic + step_pairs + char_counter_dic
# O(x) + O(x) + O(n)  where x is the number of rules and n the number of letters
# O(n^2) + O(n^2) + O(n) = O(n^2)

# time = O(n) + O(m) where n is the initial word size and m is the number of steps

def solution_2(file, steps):
    initial_chars = file.readline().strip()
    file.readline()
    pairs_dic = make_pairs_dic(file)
    
    if len(initial_chars) < MIN_TEMPLATE_LENGTH:
        raise
        
    char_counter = {}
    step_pairs = {}
    
    for ind, char in enumerate(initial_chars[:-1]):
        insert_char_on_dic(char_counter, char)
        insert_char_on_dic(step_pairs, char + initial_chars[ind + 1])
    insert_char_on_dic(char_counter, initial_chars[-1])
    
    
    for _ in range(steps):
        
        next_step_pairs = {}
        
        for pair, occurences in step_pairs.items():
            new_letter = pairs_dic[pair]
            new_pair_0 = pair[0] + new_letter
            new_pair_1 = new_letter + pair[1]
            
            char_counter[new_letter] = char_counter.get(new_letter, 0) + occurences
            next_step_pairs[new_pair_0] = next_step_pairs.get(new_pair_0, 0) + occurences
            next_step_pairs[new_pair_1] = next_step_pairs.get(new_pair_1, 0) + occurences
            
        step_pairs = next_step_pairs
        
    return get_difference_max_min(char_counter)
            
        
# inefficient solution. Only works for small number of steps
# space complex = char_counter + pairs_queue
# O(n) + O(final_number_gets)
# O(n) + O( (n-1) * 2^x - (n-1) )
# O(n) + O( n * 2^x ) =  O( n * 2^x )

# time = O( n * 2^x )

def solution_1(file, steps):
    initial_chars = file.readline().strip()
    file.readline()
    pairs_dic = make_pairs_dic(file)
    final_number_gets = get_number_gets(initial_chars, steps)
    print("final number gets = ", final_number_gets)
    time.sleep(5)
    
    if len(initial_chars) < MIN_TEMPLATE_LENGTH:
        raise
    
    char_counter = {}
    
    pairs_queue = queue.Queue()
    
    for char in initial_chars:
        insert_char_on_dic(char_counter, char)

    pairs_put = 0
    pairs_gotten = 0
    for ind, char in enumerate(initial_chars[:-1]):
        pairs_queue.put(char + initial_chars[ind + 1])
        pairs_put += 1
            
    while pairs_gotten < final_number_gets:
        pair = pairs_queue.get()
        pairs_gotten += 1
        print("getting", pairs_gotten)
        new_letter = pairs_dic[pair]
        insert_char_on_dic(char_counter, new_letter)
        
        if pairs_put < final_number_gets:
            pairs_queue.put(pair[0]+new_letter)
            pairs_queue.put(new_letter+pair[1])
            pairs_put += 2
            
    
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
