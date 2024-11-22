def iddfs_with_visualization(grid, start, destinations, rows, cols):
    total_nodes_explored = 0
    for depth_limit in range(1, rows * cols):  # Limit depth to maximum number of nodes
        distance, path, nodes_explored = dfs_with_limit(grid, start, destinations, rows, cols, depth_limit)
        total_nodes_explored += nodes_explored
        if distance != -1:
            # print(f"{len(destinations)} {depth_limit}")
            return distance, path, total_nodes_explored

    return -1, [], total_nodes_explored

def dfs_with_limit(grid, start, destinations, rows, cols, depth_limit):
    visited = set()
    stack = [(start[1], start[0], 0, [(start[0], start[1])])]
    total_nodes_explored = 1
    visited.add(start)

    while stack:
        current_row, current_col, distance, path = stack[-1]
        total_nodes_explored += 1
        if (current_col, current_row) in destinations:
            return distance, path, total_nodes_explored

        if distance < depth_limit:
            neighbors_order = [(0, -1), (-1, 0), (1, 0), (0, 1)]  # UP, LEFT, DOWN, RIGHT
            found_next_step = False

            for dr, dc in neighbors_order:
                new_row, new_col = current_row + dr, current_col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and (new_col, new_row) not in visited and grid[new_row][new_col] != -1:
                    new_path = path + [(new_col, new_row)]
                    stack.append((new_row, new_col, distance + 1, new_path))
                    visited.add((new_col, new_row))

                    found_next_step = True
                    break  # Found a valid move, no need to check other directions

            if not found_next_step:
                stack.pop()
        else:
            stack.pop()

    return -1, [], total_nodes_explored
