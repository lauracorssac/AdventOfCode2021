import sys, os

def get_file_input():
    if len(sys.argv) < 2:
        raise
    return sys.argv[1]

def get_question_input():
    if len(sys.argv) < 3:
        raise
    return sys.argv[2]
    
def add_neighbor1(graph, key, value):

    if key in graph:
        graph[key].add(value)
    else:
        graph[key] = set([value])
        
def add_neighbor2(graph, key, value):

    if key in graph:
        graph[key]["neighbors"].add(value)
    else:
        graph[key] = {"neighbors": set([value]), "visited_times": 0}

def build_graph(lines, add_neighbor):

    graph = {}

    for line in lines:
        line = line.strip()
        line_comp = line.split('-')
        
        add_neighbor(graph, line_comp[0], line_comp[1])
        add_neighbor(graph, line_comp[1], line_comp[0])
        
    return graph
    
def rec_solution1(graph, current_node, alread_visited):

    if current_node == "end":
        return 1
        
    total_paths = 0
    for neighbor in graph[current_node]:
        if neighbor not in alread_visited:
            if not current_node.isupper():
                total_paths += rec_solution1(graph, neighbor, alread_visited + [current_node])
            else:
                total_paths += rec_solution1(graph, neighbor, alread_visited)
    return total_paths
    
def rec_solution2(graph, current_node, path, paths, small_repeated):
    path += current_node + '-'
    if current_node == "end":
        paths.append(path)
        return 1

    total_paths = 0
    graph[current_node]["visited_times"] += 1
    
    for neighbor in graph[current_node]["neighbors"]:
        if neighbor.isupper():
            total_paths += rec_solution2(graph, neighbor, path, paths, small_repeated)
        elif graph[neighbor]["visited_times"] < 1:
            total_paths += rec_solution2(graph, neighbor, path, paths, small_repeated)
        elif graph[neighbor]["visited_times"] == 1 and not small_repeated:
            total_paths += rec_solution2(graph, neighbor, path, paths, True)
    
    graph[current_node]["visited_times"] -= 1
    return total_paths

def solution1(f):
    graph = build_graph(f, add_neighbor1)
    return rec_solution1(graph, "start", [])
    

def solution2(f):
    graph = build_graph(f, add_neighbor2)
    graph["start"]["visited_times"] = 1000
    paths = []
    total = rec_solution2(graph, "start", '', paths, False)
    for index, path in enumerate(paths):
        print(index, path)
    return total
    
def main():

    file = get_file_input()
    f = open(file, "r")
    question = int(get_question_input())
    parse_function = solution1 if question == 1 else solution2

    total = parse_function(f)
    
    print("The total points was = ", total)

main()
