from queue import PriorityQueue

def greedy_first_with_visualization(grid, start, destinations, rows, cols, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    total_nodes_explored = 1
    start_col, start_row = start

    for dest in destinations:
        priority_queue.put((heuristic((start_col, start_row), dest), (start_row, start_col), 0, [(start_col, start_row)]))

    while not priority_queue.empty():
        _, (current_row, current_col), distance, path = priority_queue.get()
        total_nodes_explored += 1
        if (current_col, current_row) in destinations:
            # print_grid_with_path(grid, path)
            # print("Total nodes explored:", total_nodes_explored)
            return distance, path, total_nodes_explored

        visited.add((current_col, current_row))

        neighbors_order = sorted([(0, -1), (-1, 0), (1, 0), (0, 1)], key=lambda x: heuristic((current_col + x[0], current_row + x[1]), destinations[0]))
        for dc, dr in neighbors_order:
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_col, new_row) not in visited and grid[new_row][new_col] != -1:
                new_path = path + [(new_col, new_row)]
                for dest in destinations:
                    priority_queue.put((heuristic((new_col, new_row), dest), (new_row, new_col), distance + 1, new_path))
                # print_grid_with_path(grid, new_path)
    return -1, [], total_nodes_explored



