# AI Search Algorithms – Grid Pathfinding Visualiser

A Python-based pathfinding project demonstrating different Artificial Intelligence search algorithms on a 2D grid. The project allows users to find paths between a starting position and one or more destinations while navigating around obstacles.

It includes a command-line interface and a graphical interface built with Tkinter to visualise the search results.

## Features

- **Six Search Algorithms:** Implementations of BFS, DFS, Greedy Best-First Search, A*, IDDFS, and Beam Search.
- **Grid-Based Environment:** Navigate through a two-dimensional grid.
- **Multiple Destinations:** Define multiple possible goal positions.
- **Obstacles and Walls:** Add rectangular obstacles to the environment.
- **Graphical Visualisation:** Display the grid and animate the resulting path.
- **Path Information:** Display the selected algorithm and path length.
- **Exploration Tracking:** Report the number of explored nodes.

## Algorithms Implemented

| Algorithm | Description |
|---|---|
| BFS | Explores nodes level by level using a queue. |
| DFS | Explores one direction as far as possible before backtracking. |
| Greedy Best-First Search | Uses a heuristic to prioritise nodes closer to a destination. |
| A* Search | Combines path cost and heuristic distance to prioritise nodes. |
| IDDFS | Repeatedly performs depth-limited DFS with increasing depth limits. |
| Beam Search | Limits the number of candidate paths explored at each level. |

### Heuristics

The project uses two distance calculations:

- **Manhattan Distance:** Used by A* Search.
- **Euclidean Distance:** Used by Greedy Best-First Search.

## Technologies Used

- **Python** – Search algorithms and application logic.
- **Tkinter** – Graphical user interface.
- **Collections / Queue** – Queue and priority-queue operations.
- **Math** – Distance and heuristic calculations.

## Project Structure

```text
Intro to AI/
│
├── AStar.py       # A* search implementation
├── BFS.py         # Breadth-First Search
├── DFS.py         # Depth-First Search
├── Greedy.py      # Greedy Best-First Search
├── IDDFS.py       # Iterative Deepening DFS
├── beam.py        # Beam Search
├── Grid.py        # Grid loading and algorithm execution
├── GUI.py         # Tkinter graphical interface
│
└── README.md
```

## Installation

### Prerequisites

- Python 3 installed.
- Tkinter available in your Python installation.

No external Python packages are required by the main application.

### 1. Clone the repository

```bash
git clone https://github.com/Coldrop/Search-Algorithms.git
```

### 2. Navigate to the project folder

```bash
cd "Search-Algorithms/Intro to AI"
```

### 3. Run the command-line version

```bash
python Grid.py path/to/grid.txt bfs
```

Replace `path/to/grid.txt` with the path to your grid configuration file.

Supported methods:

```text
bfs
dfs
greedy
astar
iddfs
beam
```

### 4. Run the graphical interface

```bash
python GUI.py path/to/grid.txt
```

The GUI provides buttons for selecting the search algorithm and displays the resulting path on the grid.

## Grid Configuration

The application loads its grid environment from a text file.

The expected file format is:

```text
(rows,cols)
(start_x,start_y)
(destination_x,destination_y)|(destination_x,destination_y)
(wall_x,wall_y,width,height)
(wall_x,wall_y,width,height)
```

### Example

```text
(10,10)
(0,0)
(9,9)
(3,2,2,4)
(6,5,2,3)
```

This example defines:
- A grid with 10 rows and 10 columns.
- A starting position at `(0,0)`.
- A destination at `(9,9)`.
- Two rectangular obstacles.

Coordinates use the format `(x,y)`, where `x` represents the column and `y` represents the row.

Multiple destinations can be separated using `|`.

## Output

When an algorithm finds a destination, the application reports:

- The input grid file.
- The selected search algorithm.
- The reached destination node.
- The number of explored nodes.
- The sequence of movements required to reach the destination.

Movement directions are represented as:

```text
[right] [down] [left] [up]
```

If no destination is reachable, the application reports that no goal can be reached.

## Learning Objectives

This project explores fundamental Artificial Intelligence concepts, including:

- Uninformed search strategies.
- Informed and heuristic-based search.
- Graph traversal and pathfinding.
- Search efficiency and node exploration.
- Grid representation and obstacle handling.
- Visualisation of algorithm behaviour.

## Project Status

This project was developed as an educational implementation of classical AI search algorithms. It provides a practical environment for experimenting with and comparing different approaches to pathfinding.

## Author

**Sehajpreet Singh**

- GitHub: [@Coldrop](https://github.com/Coldrop)
- Repository: [Search-Algorithms](https://github.com/Coldrop/Search-Algorithms)
