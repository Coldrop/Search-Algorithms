from queue import PriorityQueue

def a_star_with_visualization(grid, start, destinations, rows, cols, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    total_nodes_explored = 1
    start_x, start_y = start
    closest_destination = min(destinations, key=lambda dest: heuristic((start_x, start_y), dest))
    priority_queue.put((0, (start_x, start_y), 0, [(start_x, start_y)]))

    while not priority_queue.empty():
        _, (current_x, current_y), distance, path = priority_queue.get()
        total_nodes_explored += 1
        if (current_x, current_y) in destinations:
            # print_grid_with_path(grid, path)
            return distance, path, total_nodes_explored
        visited.add((current_x, current_y))

        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            new_x, new_y = current_x + dx, current_y + dy
            if 0 <= new_x < cols and 0 <= new_y < rows and (new_x, new_y) not in visited and grid[new_y][new_x] != -1:
                new_path = path + [(new_x, new_y)]
                priority_queue.put((heuristic((new_x, new_y), closest_destination) + distance + 1, (new_x, new_y), distance + 1, new_path))
                # print_grid_with_path(grid, path)    
    return -1, [], total_nodes_explored

