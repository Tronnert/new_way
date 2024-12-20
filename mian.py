from move import move
import time

def get_world():
    return move([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def calc(error, fences, snakes, enemies, food, specialFood):
    directions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return directions

def main():
    while True:
        error, fences, snakes, enemies, food, specialFood = get_world()
        directions = calc(error, fences, snakes, enemies, food, specialFood)
        tickRemainMs = move(directions)[-1]
        time.sleep(tickRemainMs * 10 ** -3)


if __name__ == "__main__":
    main()