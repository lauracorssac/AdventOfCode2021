def split_coordinate(coordinate):
    components = coordinate.split(',')
    return (int(components[0]), int(components[1]))

def get_increment(axis0, axis1):
    if axis0 == axis1:
        return 0
    if axis0 > axis1:
        return -1
    return 1

def update_dic(dic, n_intersections, x0, x1, y0, y1):
    increment_x = get_increment(x0, x1)
    increment_y = get_increment(y0, y1)

    inc_x = increment_x if increment_x != 0 else 1
    inc_y = increment_y if increment_y != 0 else 1
    
    x = x0
    y = y0

    while x in range(x0, x1 + increment_x, inc_x) or y in range(y0, y1 + increment_y, inc_y):

        covered_coordinate = "{x},{y}".format(x= x, y= y)
    
        if covered_coordinate in dic:
            if dic[covered_coordinate] == 1:
                n_intersections += 1
            dic[covered_coordinate] += 1
        else:
            dic[covered_coordinate] = 1

        x += increment_x
        y += increment_y
    return n_intersections

def get_number_intersections(lines, problem_code):
    dic = {}
    n_intersections = 0
    for line in lines:
        components = line.split(' -> ')
        x0, y0 = split_coordinate(components[0])
        x1, y1 = split_coordinate(components[1])

        if x0 != x1 and y0 != y1 and not (problem_code == 'p2' and (abs(x0 - x1) == abs(y0 - y1))):
            continue

        n_intersections = update_dic(dic, n_intersections, x0, x1, y0, y1)
       
    return n_intersections

file = open('input.txt', 'r')
lines = file.readlines()
print("Problem 1 = ", get_number_intersections(lines , 'p1'))
print("Problem 2 = ", get_number_intersections(lines , 'p2'))
