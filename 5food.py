from random import randint
from microbit import *

class Snake:
    """ This class contains the functions that operate
        on our game as well as the state of the game.
        It's a handy way to link the two.
    """

    def __init__(self):
        """ Special function that runs when you create
            a "Snake", ie. when you run
                game = Snake()
            init stands for "Initialisation"
        """
        self.current_direction = "up"
        # snake is a list of the pixels that the snake is at
        self.snake = [[2, 2]]
        # food is the co-ords of the current food
        self.food = [0, 2]
        # whether or not to end the game, used after update
        self.end = False

    def handle_input(self):
        """ We'll use this function to take input from the
            user to control which direction the snake is going
            in.
        """
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        # abs is the absolute function eg -1 => 1, 1 => 1
        if abs(x) > abs(y):
            if x < 0:
                self.current_direction = "left"
            else:
                self.current_direction = "right"
        else:
            if y < 0:
                self.current_direction = "up"
            else:
                self.current_direction = "down"

    def update(self):
        """ This function will update the game state
            based on the direction the snake is going.
        """
        # copy the old head
        new_head = list(self.snake[-1])
        if self.current_direction == "up":
            new_head[1] -= 1
        elif self.current_direction == "down":
            new_head[1] += 1
        elif self.current_direction == "left":
            new_head[0] -= 1
        elif self.current_direction == "right":
            new_head[0] += 1

        # make sure co-ords within bounds
        if new_head[0] < 0:
            new_head[0] = 4
        elif new_head[0] > 4:
            new_head[0] = 0
        if new_head[1] < 0:
            new_head[1] = 4
        elif new_head[1] > 4:
            new_head[1] = 0

        self.snake.append(new_head)
        if new_head == self.food:
            self.food = self.gen_new_food()
        else:
            self.snake = self.snake[1:]

    def draw(self):
        """ This makes the game appear on the LEDs. """
        display.clear()
        display.set_pixel(self.food[0], self.food[1], 5)
        for part in self.snake:
            display.set_pixel(part[0], part[1], 9)

    def gen_new_food(self):
        """ Move food to a new position after it has
            been eaten.
        """
        new_food = [randint(0, 4), randint(0, 4)]
        # make sure we're not generating the food in the snake
        while new_food in self.snake:
            new_food = [randint(0, 4), randint(0, 4)]
        return new_food

# game is an "instance" of Snake
game = Snake()

# this is called our "game loop" and is where everything
# happens
while True:
    game.handle_input()
    game.update()
    game.draw()
    # this makes our micro:bit do nothing for 500ms
    sleep(500)
