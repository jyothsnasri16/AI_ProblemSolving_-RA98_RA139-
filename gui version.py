# Map Coloring using Backtracking

# Define the graph (adjacency list)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Store result
solution = {}

# Check if it's safe to assign a color
def is_safe(node, color):
    for neighbor in graph[node]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

# Backtracking function
def solve(node_list, index=0):
    if index == len(node_list):
        return True

    node = node_list[index]

    for color in colors:
        if is_safe(node, color):
            solution[node] = color

            if solve(node_list, index + 1):
                return True

            # Backtrack
            del solution[node]

    return False

# Run the solver
nodes = list(graph.keys())

if solve(nodes):
    print("Solution Found:")
    for node in solution:
        print(f"{node} -> {solution[node]}")
else:
    print("No solution exists.")