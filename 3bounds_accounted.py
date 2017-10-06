from microbit import *

# up, right, down, left
# direction is stored by the effect it has on position
DIRECTIONS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

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
        self.current_direction = DIRECTIONS[0]
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
        pass

    def update(self):
        """ This function will update the game state
            based on the direction the snake is going.
        """
        head = self.snake[-1]
        new_head = [x + y for (x, y) in zip(self.current_direction, head)]
        new_head = self.bounds_accounted(new_head)
        self.snake.append(new_head)
        self.snake = self.snake[1:]

    def draw(self):
        """ This makes the game appear on the LEDs. """
        display.clear()
        display.set_pixel(self.food[0], self.food[1], 5)
        for part in self.snake:
            display.set_pixel(part[0], part[1], 9)

    def bounds_accounted(self, co_ords):
        """ Takes some co-ordinates and wraps them if they
            are out of the bounds of our board
        """
        # make a copy of the list to work on
        new_co_ords = co_ords
        # idx stands for index
        for idx in range(len(co_ords)):
            if co_ords[idx] > 4 or co_ords[idx] < 0:
                # % is modulo operator, eg 8 % 5 == 3, -1 % 5 == 4
                new_co_ords[idx] = co_ords[idx] % 5
        return new_co_ords

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
