import numpy as np
from field import field
import time

def get_waves(head, n, fences, snakes, enemies):
    def wave_algorithm_3d(grid, start):
        n1, n2, n3 = grid.shape
        distances = -np.ones_like(grid, dtype=np.int32)  # Инициализируем массив расстояний
        distances[start] = 0
        
        queue = [start]  # Очередь для BFS

        directions = [
            (1, 0, 0), (-1, 0, 0),
            (0, 1, 0), (0, -1, 0),
            (0, 0, 1), (0, 0, -1)
        ]  # Возможные направления движения

        while queue:
            x, y, z = queue.pop(0)
            current_distance = distances[x, y, z]

            for dx, dy, dz in directions:
                nx, ny, nz = x + dx, y + dy, z + dz
                
                # Проверяем границы массива и отсутствиеstart = np.array(data['snakes'][1]['geometry'][0]) препятствий
                if 0 <= nx < n1 and 0 <= ny < n2 and 0 <= nz < n3:
                    if grid[nx, ny, nz] == 0 and distances[nx, ny, nz] == -1:
                        distances[nx, ny, nz] = current_distance + 1
                        queue.append((nx, ny, nz))
        return distances
    matrix = field(head, n, fences, snakes, enemies)
    return wave_algorithm_3d(matrix, (20, 20, 20))


if __name__ == "__main__":
    import json
    with open("example_response.json") as file:
        data = json.load(file)
    start = np.array(data['snakes'][1]['geometry'][0])
    print(get_waves(start, 20, data['fences'], data['snakes'], data['enemies']))