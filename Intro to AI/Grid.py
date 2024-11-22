import sys
from BFS import bfs_with_visualization
from DFS import dfs_with_visualization
from Greedy import greedy_first_with_visualization
from AStar import a_star_with_visualization
from IDDFS import iddfs_with_visualization
from beam import beam_search

import math

class GridGraph:
    def __init__(self, file_path):
        self.file_path = file_path
        self.grid, self.rows, self.cols, self.start, self.destinations = self.read_grid_from_file(file_path)
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        
    def read_grid_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            rows, cols = map(int, lines[0].strip()[1:-1].split(','))
            grid = [[0] * cols for _ in range(rows)]
            start = tuple(map(int, lines[1].strip()[1:-1].split(',')))
            destinations = [tuple(map(int, dest.strip()[1:-1].split(','))) for dest in lines[2].strip().split('|')]
            walls = [tuple(map(int, wall.strip()[1:-1].split(','))) for wall in lines[3:]]

            for x, y, w, h in walls:
                for i in range(x, x + w):
                    for j in range(y, y + h):
                        grid[j][i] = -1  # Mark wall cells with -1

            for dest in destinations:
                grid[dest[1]][dest[0]] = 1  # Mark destination cells with 1

            grid[start[1]][start[0]] = 2  # Mark start cell with 2
            self.start = start
            
        #     print("Destinations:", destinations)
        # print("Start", start)
        return grid, rows, cols, start, destinations
    
    def find_shortest_path_bfs(self):
        
        distance, path, total_nodes_explored = bfs_with_visualization(self.grid, self.start, self.destinations, self.rows, self.cols)     
        self.print_path("bfs", distance, path, total_nodes_explored)
        return distance, path
        

    def find_shortest_path_dfs(self):
        distance, path, total_nodes_explored = dfs_with_visualization(self.grid, self.start, self.destinations, self.rows, self.cols)
        self.print_path("dfs", distance, path, total_nodes_explored)
        return distance, path

    def find_shortest_path_greedy(self):
        distance, path, total_nodes_explored = greedy_first_with_visualization(self.grid, self.start, self.destinations, self.rows, self.cols, heuristic=euclidean_distance)
        self.print_path("greedy", distance, path, total_nodes_explored)
        return distance, path
    
    def find_shortest_path_astar(self):
        distance, path, total_nodes_explored = a_star_with_visualization(self.grid, self.start, self.destinations, self.rows, self.cols, heuristic=manhattan_distance)
        self.print_path("astar", distance, path, total_nodes_explored)
        return distance, path


    def find_shortest_path_iddfs(self):
            distance, path, total_nodes_explored = iddfs_with_visualization(self.grid, self.start, self.destinations, self.rows, self.cols)
            self.print_path("iddfs", distance, path, total_nodes_explored)
            return distance, path  
    
    
    def find_shortest_path_beam(self):
        distance, path, total_nodes_explored = beam_search(self.grid, self.start, self.destinations, self.rows, self.cols)
        self.print_path("beam", distance, path, total_nodes_explored)
        return distance, path

       

    def print_path(self, method, cost_or_distance, path, total_nodes_explored):
        if cost_or_distance != -1:
            goal = path[-1]  # Get the last node in the path (goal node)
            print(f"{self.file_path} {method}")
            print(f" <Node {goal}> {total_nodes_explored}")
            # print("path:")
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
            # print(f"Total nodes explored: {total_nodes_explored}")
        else:
            print(f"{self.file_path} {method}")
            print(f"No goal is reachable; {len(self.visited)}")

def euclidean_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def manhattan_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x2 - x1) + abs(y2 - y1)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Grid.py <filename> <method>")
        sys.exit(1)

    file_path = sys.argv[1]
    method = sys.argv[2]

    grid_graph = GridGraph(file_path)

    if method == "bfs":
        grid_graph.find_shortest_path_bfs() 
    elif method == "dfs":
        grid_graph.find_shortest_path_dfs()
    elif method == "greedy":
        grid_graph.find_shortest_path_greedy()
    elif method == "astar":
        grid_graph.find_shortest_path_astar()
    elif method == "iddfs":
        grid_graph.find_shortest_path_iddfs() 
    elif method == "beam":
        grid_graph.find_shortest_path_beam()
    
    else:
        print("Invalid method. Use 'bfs', 'dfs', 'greedy', 'astar','iddfs', or 'beam'.")
