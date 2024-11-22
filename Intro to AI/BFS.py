from collections import deque

def bfs_with_visualization(grid, start, destinations, rows, cols):
    visited = set()
    total_nodes_explored = 1
    queue = deque([(start[1], start[0], 0, [(start[0], start[1])])])  

    while queue:
        current_row, current_col, distance, path = queue.popleft() 
        visited.add((current_col, current_row))
        total_nodes_explored += 1
        if (current_col, current_row) in destinations:
            # print("Total nodes explored:", total_nodes_explored)
            return distance, path, total_nodes_explored

        neighbors_order = [(0, -1), (-1, 0), (1, 0), (0, 1)]  # UP, LEFT, DOWN, RIGHT

        for dr, dc in neighbors_order:
            new_row, new_col = current_row + dr, current_col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and (new_col, new_row) not in visited and grid[new_row][new_col] != -1:
                new_path = path + [(new_col, new_row)]
                queue.append((new_row, new_col, distance + 1, new_path))
                visited.add((new_col, new_row))

    return -1, [] ,total_nodes_explored


