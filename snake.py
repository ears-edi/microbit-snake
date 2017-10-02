from random import randint
from microbit import *

# up, right, down, left
DIRECTIONS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

class Snake:
    def __init__(self):
        self.current_direction = DIRECTIONS[0]
        self.snake = [[2, 2]]
        self.food = [0, 2]
        self.end = False

    def handle_input(self):
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        if abs(x) > abs(y):
            if x < 0:
                self.current_direction = DIRECTIONS[3]
            else:
                self.current_direction = DIRECTIONS[1]
        else:
            if y < 0:
                self.current_direction = DIRECTIONS[0]
            else:
                self.current_direction = DIRECTIONS[2]

    def update(self):
        head = self.snake[-1]
        new_head = [x + y for (x, y) in zip(self.current_direction, head)]
        new_head = self.bounds_accounted(new_head)
        if new_head in self.snake:
            self.end = True
        self.snake.append(new_head)
        if new_head == self.food:
            self.food = self.gen_new_food()
        else:
            self.snake = self.snake[1:]

    def draw(self):
        display.clear()
        display.set_pixel(self.food[0], self.food[1], 5)
        for part in self.snake:
            display.set_pixel(part[0], part[1], 9)

    def bounds_accounted(self, co_ords):
        new_co_ords = co_ords
        for idx in range(len(co_ords)):
            if co_ords[idx] > 4 or co_ords[idx] < 0:
                new_co_ords[idx] = co_ords[idx] % 5
        return new_co_ords

    def gen_new_food(self):
        new_food = [randint(0, 4), randint(0, 4)]
        while new_food in self.snake:
            new_food = [randint(0, 4), randint(0, 4)]
        return new_food

game = Snake()

while True:
    game.handle_input()
    game.update()
    if game.end:
        display.show(Image.SAD)
        break
    game.draw()
    sleep(500)
