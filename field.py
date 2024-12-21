import numpy as np

def field(head, n, fences, snakes, enemies):
    def func(x):
        matrix[*list(map(lambda x: x - 1, x[1:]))] = 1
    # n = 20
    all_points = np.array([(1, *i) for i in fences] + [(1, *point) for snake in snakes for point in snake['geometry'][1:]] + [(1, *point) for enemy in enemies for point in enemy['geometry']] )#+ [(3, *point['c']) for point in food])
    all_points = all_points[(abs(all_points[:,1] - head[0]) <= n) & (abs(all_points[:,2] - head[1]) <= n) & (abs(all_points[:,3] - head[2]) <= n) ]
    # max_x = max(all_points, key=lambda x: x[1])[1]
    # max_y = max(all_points, key=lambda x: x[2])[2]
    # max_z = max(all_points, key=lambda x: x[3])[3]
    all_points[:,1:] += -head + np.array([n, n, n])
    print(all_points)
    matrix = np.zeros((2 * n + 1, 2 * n + 1, 2 * n + 1))
    np.apply_along_axis(func, 1, all_points)
    #print(matrix)
    return matrix
    