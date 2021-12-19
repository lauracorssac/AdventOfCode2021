

def split_coordinate(coordinate):
    components = coordinate.split(',')
    return (int(components[0]), int(components[1]))

def update_dic(dic, n_intersections, common_axis, common_axis_value, diff_axis_0, diff_axis_1):
    increment = -1 if diff_axis_0 > diff_axis_1 else 1
    
    for i in range(diff_axis_0, diff_axis_1 + increment, increment):
        
        x = common_axis_value if common_axis == 'x' else i
        y = common_axis_value if common_axis == 'y' else i
        covered_coordinate = "{x},{y}".format(x= x, y= y)
        
        if covered_coordinate in dic:
            if dic[covered_coordinate] == 1:
                n_intersections += 1
            dic[covered_coordinate] += 1
        else:
            dic[covered_coordinate] = 1
    return n_intersections


def get_number_intersections(lines):
    dic = {}
    n_intersections = 0
    for line in lines:
        components = line.split(' -> ')
        x0, y0 = split_coordinate(components[0])
        x1, y1 = split_coordinate(components[1])

        if x0 == x1:
            n_intersections = update_dic(dic, n_intersections, 'x', x0, y0, y1)
        elif y0 == y1:
            n_intersections = update_dic(dic, n_intersections, 'y', y0, x0, x1)
    
    return n_intersections




file = open('input.txt', 'r')
lines = file.readlines()
print("Problem 1 = ", get_number_intersections(lines))





    





