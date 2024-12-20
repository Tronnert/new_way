import numpy
import random

def generate_world(n1, n2, n3, simple, golden, suspicious, obstacles):
    world = numpy.zeros((n1, n2, n3))
    for i in range(obstacles):
        cell = [random.randint(0, n1 - 1), random.randint(0, n2 - 1), random.randint(0, n3 - 1)]
        while world[*cell] != 0:
            cell = [random.randint(0, n1 - 1), random.randint(0, n2 - 1), random.randint(0, n3 - 1)]
        world[*cell] = 1
    for i in range(simple):
        cell = [random.randint(0, n1 - 1), random.randint(0, n2 - 1 - 1), random.randint(0, n3 - 1)]
        while world[*cell] != 0:
            cell = [random.randint(0, n1 - 1), random.randint(0, n2 - 1), random.randint(0, n3 - 1)]
        world[*cell] = 2
    for i in range(golden):
        cell = [random.randint(0, n1 - 1), random.randint(0, n2 - 1), random.randint(0, n3 - 1)]
        while world[*cell] != 0:
            cell = [random.randint(0, n1 - 1), random.randint(0, n2 - 1), random.randint(0, n3 - 1)]
        world[*cell] = 3
    for i in range(suspicious):
        cell = [random.randint(0, n1 - 1), random.randint(0, n2 - 1), random.randint(0, n3 - 1)]
        while world[*cell] != 0:
            cell = [random.randint(0, n1 - 1), random.randint(0, n2 - 1), random.randint(0, n3 - 1)]
        world[*cell] = 4
    return world