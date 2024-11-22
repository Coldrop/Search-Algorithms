def dfs_with_visualization(grid, start, destinations, rows, cols):
    visited = set()
    stack = [(start[1], start[0], 0, [(start[0], start[1])])]  
    total_nodes_explored = 1
    visited.add(start)

    while stack:
        current_row, current_col, distance, path = stack[-1]  
        total_nodes_explored += 1
        if (current_col, current_row) in destinations:
            # print_grid_with_path(grid, path)
            # print("Total nodes explored:", total_nodes_explored)
            return distance, path, total_nodes_explored

        neighbors_order = [(0, -1), (-1, 0), (1, 0), (0, 1)]  # UP, LEFT, DOWN, RIGHT
        found_next_step = False

        for dr, dc in neighbors_order:
            new_row, new_col = current_row + dr, current_col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and (new_col, new_row) not in visited and grid[new_row][new_col] != -1:
                new_path = path + [(new_col, new_row)]
                stack.append((new_row, new_col, distance + 1, new_path))
                visited.add((new_col, new_row))
                
                #print_grid_with_path(grid, new_path)
                
                found_next_step = True
                break  # Found a valid move, no need to check other directions
        if not found_next_step:
            current_row, current_col, distance, path = stack.pop()  
    return -1, [], total_nodes_explored


def print_grid_with_path(grid, path):
    if not path:
        return

    for i in range(1, len(path)):
        prev_col, prev_row = path[i - 1]
        col, row = path[i]
        if col > prev_col:
            print("[right]", end=' ')
        elif col < prev_col:
            print("[left]", end=' ')
        elif row > prev_row:
            print("[down]", end=' ')
        elif row < prev_row:
            print("[up]", end=' ')
    print()
