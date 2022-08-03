import sys
import queue
import math
import heapq

def solution_1(matrix):
    
    lines = len(matrix)
    cols = len(matrix[0])
    distance_matrix = [[math.inf] * cols for _ in range(lines)]
    
    to_visit = []
    visited = set()
    
    distance_matrix[0][0] = 0
    heapq.heappush(to_visit, (0, (0,0)) )
   
    # O(n log n) ?
    while to_visit:
        
        # O(log n)
        # Gets the most close to the origin node
        node_dist_origin, (node_l, node_c) = heapq.heappop(to_visit)
        
        if (node_l, node_c) in visited:
            continue
         
        # O(1)
        visited.add((node_l, node_c))
        
        neighbor_offsets = [(1,0), (0,1), (0,-1), (-1,0)]
        
        # max 4 times -> O(log n)
        for offet_l, offet_c in neighbor_offsets:
            
            neigh_c = offet_c + node_c
            neigh_l = offet_l + node_l
            
            if neigh_c >= cols or neigh_c < 0:
                continue
            if neigh_l >= lines or neigh_l < 0:
                continue
            if (neigh_l, neigh_c) in visited:
                continue
            
            current_neigh_dist = distance_matrix[neigh_l][neigh_c]
            possible_new_dist = int(matrix[neigh_l][neigh_c]) + node_dist_origin
            
            if possible_new_dist < current_neigh_dist:
                distance_matrix[neigh_l][neigh_c] = possible_new_dist
                
                # O(log n)
                heapq.heappush(to_visit, (possible_new_dist, (neigh_l, neigh_c)))
            
    return distance_matrix[lines - 1][cols - 1]
    
def build_new_matrix(matrix):

    lines = len(matrix)
    cols = len(matrix[0])
    new_cols = cols * 5
    new_lines = lines * 5
    new_matrix = [[0] * new_cols for _ in range(new_lines)]
    
    for l in range(lines):
        for c in range(cols):
        
            number = int(matrix[l][c])
            
            for i in range(5):
            
                offset_l = l + (i*lines)
                
                new_matrix[offset_l][c] = number
                
                number += 1
                number = 1 if number == 10 else number
                
    for l in range(new_lines):
        for c in range(cols):
        
            number = int(new_matrix[l][c])
        
            for i in range(5):
            
                offet_c = c + (i*cols)
                
                new_matrix[l][offet_c] = number
                
                number += 1
                number = 1 if number == 10 else number
            
            
    return new_matrix

def print_matrix(matrix):
    print("PRINT MATRIX")
    lines = len(matrix)
    cols = len(matrix[0])

    for l in range(0, lines):
        for c in range(0, cols):
            print(matrix[l][c], end=" ")
        print()
        
def solution_2(matrix):
    new_matrix = build_new_matrix(matrix)
    return solution_1(new_matrix)
    

def main():
    if len(sys.argv) < 3:
        print("missing args")
        return
    question = int(sys.argv[2])
    filename = sys.argv[1]
    function = solution_1 if question == 1 else solution_2
    f = open(filename, "r")
    matrix = [line.strip() for line in f.readlines()]
    print(function(matrix))
    

main()
