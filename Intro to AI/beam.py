from queue import PriorityQueue
from collections import deque

def beam_search(grid, start, destinations, rows, cols, beam_width=1000):
    visited = set()
    frontier = [(0, [start])]
    total_nodes_explored = 1

    while frontier:
        total_nodes_explored += len(frontier)
        next_frontier = []
        for _, path in frontier:
            current_node = path[-1]
            visited.add(current_node)
            if current_node in destinations:
                return len(path) - 1, path, total_nodes_explored

            neighbors = get_neighbors(current_node, rows, cols)
            for neighbor in neighbors:
                if neighbor not in visited and grid[neighbor[1]][neighbor[0]] != -1:
                    new_path = path + [neighbor]
                    next_frontier.append((len(new_path), new_path))

        next_frontier.sort(key=lambda x: x[0])
        frontier = next_frontier[:beam_width]

    return -1, [], total_nodes_explored

def get_neighbors(node, rows, cols):
    x, y = node
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < cols - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < rows - 1:
        neighbors.append((x, y + 1))
    return neighbors
