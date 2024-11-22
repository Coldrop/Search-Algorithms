import tkinter as tk
import sys
from Grid import GridGraph
import tkinter.messagebox as messagebox

class GridGUI:
    def __init__(self, master, file_path):
        self.master = master
        self.file_path = file_path
        self.grid_graph = GridGraph(file_path)
        self.rows, self.cols = self.grid_graph.rows, self.grid_graph.cols
        self.canvas_size = 500
        self.cell_size = self.canvas_size // max(self.rows, self.cols)
        self.canvas = tk.Canvas(self.master, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()
        self.draw_grid()
        self.start = None
        self.destinations = []
        
        button_font = ("Arial", 12)  # Font for buttons
        button_padx = 10  # Padding for buttons
        self.bfs_button = tk.Button(self.master, text="BFS", command=self.run_bfs, font=button_font, padx=button_padx)
        self.bfs_button.pack(side=tk.LEFT)
        self.dfs_button = tk.Button(self.master, text="DFS", command=self.run_dfs, font=button_font, padx=button_padx)
        self.dfs_button.pack(side=tk.LEFT)
        self.greedy_button = tk.Button(self.master, text="Greedy", command=self.run_greedy, font=button_font, padx=button_padx)
        self.greedy_button.pack(side=tk.LEFT)
        self.astar_button = tk.Button(self.master, text="A*", command=self.run_astar, font=button_font, padx=button_padx)
        self.astar_button.pack(side=tk.LEFT)
        self.astar_button = tk.Button(self.master, text="IDDFS", command=self.run_IDDFS, font=button_font, padx=button_padx)
        self.astar_button.pack(side=tk.LEFT)
        self.astar_button = tk.Button(self.master, text="Beam", command=self.run_Beam, font=button_font, padx=button_padx)
        self.astar_button.pack(side=tk.LEFT)
        

        # Add labels for algorithm selection and shortest path length
        self.algorithm_label = tk.Label(self.master, text="Selected Algorithm: ")
        self.algorithm_label.pack()
        self.shortest_path_label = tk.Label(self.master, text="Shortest Path Length: ")
        self.shortest_path_label.pack()

        self.master.title("Grid Graph Pathfinding Visualizer")
    
    def animate_path(self, path, distance, algorithm):
        def animation_loop(path_iter):
            try:
                current_point = next(path_iter)
                self.visualize_path_point(current_point)
                self.master.after(100, animation_loop, path_iter)  # Schedule the next iteration
            except StopIteration:
                if path:  # Check if a path was found
                    self.algorithm_label.config(text=f"Selected Algorithm: {algorithm}")
                    self.shortest_path_label.config(text=f"Shortest Path Length: {distance}")
                else:
                    self.algorithm_label.config(text=f"Selected Algorithm: {algorithm}")
                    self.shortest_path_label.config(text="Shortest Path Length: No path found")

        path_iter = iter(path)
        animation_loop(path_iter)

    
    def visualize_path_point(self, point):
        # Clear the previous visualization
        self.canvas.delete("path")

        # Visualize the current point in the path
        x0, y0 = point[0] * self.cell_size, point[1] * self.cell_size
        x1, y1 = x0 + self.cell_size, y0 + self.cell_size
        self.canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", outline="gray", tags="path")

        # Update the canvas
        self.canvas.update()
    def run_bfs(self):
            distance, path = self.grid_graph.find_shortest_path_bfs()
            if path:
                self.animate_path(path, distance, "bfs")
            else:
                self.algorithm_label.config(text="Selected Algorithm: bfs")
                self.shortest_path_label.config(text="Shortest Path Length: No path found")


    def run_dfs(self):
        distance, path = self.grid_graph.find_shortest_path_dfs()
        if path:
            self.animate_path(path, distance, "dfs")
        else:
            self.algorithm_label.config(text="Selected Algorithm: dfs")
            self.shortest_path_label.config(text="Shortest Path Length: No path found")

    def run_greedy(self):
        distance, path = self.grid_graph.find_shortest_path_greedy()
        if path:
            self.animate_path(path, distance, "Greedy")
        else:
            self.algorithm_label.config(text="Selected Algorithm: greedy")
            self.shortest_path_label.config(text="Shortest Path Length: No path found")

    def run_astar(self):
        distance, path = self.grid_graph.find_shortest_path_astar()
        if path:
            self.animate_path(path, distance, "Astar")
        else:
            self.algorithm_label.config(text="Selected Algorithm: astar")
            self.shortest_path_label.config(text="Shortest Path Length: No path found")
            
    def run_IDDFS(self):
        distance, path = self.grid_graph.find_shortest_path_iddfs()
        if path:
            self.animate_path(path, distance, "IDDFS")
        else:
            self.algorithm_label.config(text="Selected Algorithm: iddfs")
            self.shortest_path_label.config(text="Shortest Path Length: No path found")
    
    def run_Beam(self):
        distance, path = self.grid_graph.find_shortest_path_beam()
        if path:
            self.animate_path(path, distance, "Beam")
        else:
            self.algorithm_label.config(text="Selected Algorithm: Beam")
            self.shortest_path_label.config(text="Shortest Path Length: No path found")                

    import tkinter.messagebox as messagebox

    def run_algorithm(self, algorithm):
        if algorithm == "bfs":
            result = self.grid_graph.find_shortest_path_bfs()
        elif algorithm == "dfs":
            result = self.grid_graph.find_shortest_path_dfs()
        elif algorithm == "greedy":
            result = self.grid_graph.find_shortest_path_greedy()
        elif algorithm == "astar":
            result = self.grid_graph.find_shortest_path_astar()
        elif algorithm == "iddfs":
            result = self.grid_graph.find_shortest_path_iddfs()
        elif algorithm == "Beam":
            result = self.grid_graph.find_shortest_path_beam()        

        if result is None:
            # No path found, show pop-up error message
            messagebox.showerror("Error", "No path found")
            self.algorithm_label.config(text=f"Selected Algorithm: {algorithm}")
            self.shortest_path_label.config(text="Shortest Path Length: No path found")
        else:
            distance, path = result
            self.update_grid_with_path(path)
            self.algorithm_label.config(text=f"Selected Algorithm: {algorithm}")
            self.shortest_path_label.config(text=f"Shortest Path Length: {distance}")





    def update_grid_with_path(self, path):
        self.canvas.delete("path")
        for row_idx, row in enumerate(self.grid_graph.grid):
            for col_idx, cell in enumerate(row):
                x0, y0 = col_idx * self.cell_size, row_idx * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                color = "white" if cell == 0 else "red" if cell == 1 else "green" if cell == 2 else "black"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")
                if (col_idx, row_idx) in path:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", outline="gray", tags="path")



    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                color = "white" if self.grid_graph.grid[i][j] == 0 else "red" if self.grid_graph.grid[i][j] == 1 else "green" if self.grid_graph.grid[i][j] == 2 else "black"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python GUI.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]

    root = tk.Tk()
    root.title("Grid Graph Visualization")
    gui = GridGUI(root, file_path)
    root.mainloop()
