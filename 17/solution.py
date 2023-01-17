

def get_highest_y(initial_y_speed):
    
    y_position = 0
    
    for i in range(initial_y_speed, 0, -1):
        y_position += i
    
    return y_position

print(get_highest_y(132 - 1))
