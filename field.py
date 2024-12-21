import numpy as np

def field(fences, snakes, enemies, food):
    all_points = np.array([(1, *i) for i in fences] + [(1, *point) for snake in snakes for point in snake['geometry'][1:]] + [(1, *point) for enemy in enemies for point in enemy['geometry']] + [(3, *point['c']) for point in food])
    max_x = max(all_points, key=lambda x: x[1])[1]
    max_y = max(all_points, key=lambda x: x[2])[2]
    max_z = max(all_points, key=lambda x: x[3])[3]
    print((max_x, max_y, max_z))
    print()
    field = np.zeros((max_x, max_y, max_z))
    func_obj = np.vectorize(func)
    func_obj(all_points)
    return field
    

def func(x):
    print(x)
    field[*x[1:]] = x[0]
