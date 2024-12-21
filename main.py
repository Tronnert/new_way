from move import move
from response_to_meshes import load_variables_objects, create_meshes
import time
import numpy as np
import math
# from math import sign
# from math import si

def get_world():
    return move([[0, 0, 0], [0, 0, 0], [0, 0, 0]], ["", "", ""])

def get_best_food(position, mandarines):
    return max(mandarines, key=lambda x: x["points"] / abs(position - x["c"]).sum(), default={"c": np.array([1, 0, 0])})["c"]

def calc(errors, fences, snakes, enemies, food, specialFood):
    # directions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    new_directions = []
    print("!calc")
    for snake in snakes:
        if snake["status"] != "dead":
            head_position = np.array(snake["geometry"][0])
            # print(head_position)
            best_food = get_best_food(head_position, food)
            # print(best_food, end=" ")
            # print(abs(best_food - head_position).sum())
            direction_to_best = best_food - head_position
            # print(direction_to_best)
            print(direction_to_best, end=" ")
            print(abs(direction_to_best).sum())
            # direction_to_best
            id_max_coord = np.argmax(abs(direction_to_best))
            new_direction = [0, 0, 0]
            new_direction[id_max_coord] = int(np.sign(direction_to_best[id_max_coord]))
            new_directions.append(new_direction.copy())
            # if abs(direction_to_best[0]) >= abs(direction_to_best[1]) and (direction_to_best[0]) >= abs(direction_to_best[2]):
            #     new_directions.append([int(np.sign(direction_to_best[0])), 0, 0])
            # elif abs(direction_to_best[1]) >= abs(direction_to_best[2]) and abs(direction_to_best[1]) >= abs(direction_to_best[0]):
            #     new_directions.append([0, int(np.sign(direction_to_best[1])), 0])
            # else:
            #     new_directions.append([0, 0, int(np.sign(direction_to_best[2]))])
        else:
            print("dead")
            new_directions.append([0, 0, 0])
    print(new_directions)
    print("!calc")
    return new_directions

def get_food_type(point, specialFood):
    if point in specialFood["golden"]:
        return "golden"
    elif point in specialFood["suspicious"]:
        return "suspicious"
    return "ordinary"

def make_food(food, specialFood):
    return [{"c": np.array(e["c"]), 
             "points": e["points"],
             "type": get_food_type(e["c"], specialFood)} for e in food]

def main():
    while True:
        turn, points, error, fences, snakes, enemies, food, specialFood, _ = get_world()
        snake_ids = [e["id"] for e in snakes]
        # print(snake_ids)
        food = make_food(food, specialFood)
        create_meshes(load_variables_objects(fences, snakes, enemies, food))
        directions = calc(error, fences, snakes, enemies, food, specialFood)
        tickRemainMs = move(directions, snake_ids)[-1]
        print(f"{turn=}")
        print(f"points: {points}\n")
        time.sleep(tickRemainMs * 10 ** -3)


if __name__ == "__main__":
    main()