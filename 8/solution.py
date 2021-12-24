

def count_occurences(output_numbers):
    desired_lengths = [2, 4, 7, 3]
    return len(list(filter(lambda x: len(x) in desired_lengths, output_numbers)))

def problem_one(lines):
    output_numbers = list(map(lambda x: x.split(' | ')[1].strip().split(' '), lines))
    output_numbers_merged = [item for sublist in output_numbers for item in sublist]
    print("Problem 1 = ", count_occurences(output_numbers_merged))



def get_correspondents(ten_numbers ):
    possibilities = {}
    ten_numbers = sorted(ten_numbers, key=len)

    one = set(ten_numbers[0])
    possibilities['c'] = one
    possibilities['f'] = one

    seven = set(ten_numbers[1])
    diff = seven - one
    possibilities['a'] = diff

    four = set(ten_numbers[2])
    diff = four - one
    possibilities['b'] = diff
    possibilities['d'] = diff

    # 5 2 3
    a = [set(x) for x in ten_numbers[3:6]]
    intersection = set.intersection(*a)
    d1 = a[0] - intersection
    d2 = a[1] - intersection
    d3 = a[2] - intersection

    unique_1 = d1 - d2 - d3
    unique_2 = d2 - d1 - d3
    unique_3 = d3 - d2 - d1

    union = set.union(unique_1, unique_2, unique_3)
    b_changed = possibilities['b'] != union
    possibilities['b'] = possibilities['b'] & union
    possibilities['d'] = possibilities['d'] - possibilities['b'] if b_changed else possibilities['d']
    possibilities['e'] = union - possibilities['b'] if b_changed else union

    rest_intersection = intersection - possibilities['a']
    d_changed = rest_intersection != possibilities['d'] 
    possibilities['d'] = possibilities['d'] & rest_intersection if d_changed else possibilities['d'] 
    possibilities['g'] = rest_intersection - possibilities['d'] if d_changed else rest_intersection

    # 0 6 9
    a = [set(x) for x in ten_numbers[6:9]]
    ced = set.union(*a) - set.intersection(*a)
    c_changed = ced != possibilities['c']
    possibilities['c'] = ced &  possibilities['c']
    possibilities['f'] = possibilities['f'] - possibilities['c'] if c_changed else possibilities['f']

    return possibilities

def get_number(desired_set, number_segments):
    for key in number_segments:
        if number_segments[key] == desired_set:
            return key

def problem_two(lines, numbers_segments):
    total_sum = 0
    for line in lines:
        line_components = line.strip().split(' | ')
        ten_numbers = line_components[0].split(' ')
        output = line_components[1].split(' ')
        possibilities = get_correspondents(ten_numbers)
        possibilities_reversed = {list(possibilities[x])[0]: x for x in possibilities}
        
        #print(possibilities)
        #print(possibilities_reversed)
        
        line_output_number = ''
        for number in output:
            translated_number = ''
            #print(number)
            for letter in number:
                translated_number += possibilities_reversed[letter]
          
            translated_number = set(translated_number)
            #print(translated_number)
            line_output_number += get_number(translated_number, numbers_segments)

        line_output_number = int(line_output_number)
        total_sum += line_output_number
    return total_sum 
            
            
numbers_segments = {
    '0': {'a', 'b', 'c', 'e', 'f', 'g'},
    '1': {'c', 'f'},
    '2': {'a', 'c', 'd', 'e', 'g'},
    '3': {'a', 'c', 'd', 'f', 'g'},
    '4': {'b', 'c', 'd', 'f'},
    '5': {'a', 'b', 'd', 'f', 'g'},
    '6': {'a', 'b', 'd', 'e', 'f', 'g'},
    '7': {'a', 'c', 'f'},
    '8': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    '9': {'a', 'b', 'c', 'd', 'f', 'g'}
}

file = open('input.txt', 'r')
lines = file.readlines()
#problem_one(lines)
print("Problem 2 = ", problem_two(lines, numbers_segments))
