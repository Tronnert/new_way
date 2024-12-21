import numpy as np

from pathfinding3d.core.diagonal_movement import DiagonalMovement
from pathfinding3d.core.grid import Grid
from pathfinding3d.finder.a_star import AStarFinder
import time

import json
from field import field

with open("example_response.json") as file:
    data = json.load(file)

now = time.time()
# Create a 3D numpy array with 0s as obstacles and 1s as walkable paths
matrix = field(data['fences'], data['snakes'], data['enemies'], data['food'])
# mark the center of the grid as an obstacle

# Create a grid object from the numpy array
grid = Grid(matrix=matrix)

# Mark the start and end points
start = grid.node(0, 0, 0)
end = grid.node(9, 9, 9)

# Create an instance of the A* finder with diagonal movement allowed
finder = AStarFinder()
path, runs = finder.find_path(start, end, grid)

# Path will be a list with all the waypoints as nodes
# Convert it to a list of coordinate tuples
path = [p.identifier for p in path]

print("operations:", runs, "path length:", len(path))
print("path:", path)
print("Execution time:", time.time() - now)

# grid.visualize(
#   path=path,  # optionally visualize the path
#   start=start,
#   end=end,
#   visualize_weight=True,  # weights above 1 (default) will be visualized
#   save_html=True,  # save visualization to html file
#   save_to="path_visualization.html",  # specify the path to save the html file
#   always_show=True,  # always show the visualization in the browser
# )
