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
        # current direction is a string with up, down, left or right
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
        ## STEP 3 - handling iput.
        ## Your code goes here
        ## 1. Get the X and Y values from the accelerometer
        ## 2. Assign the direction ("up", "down" etc.) based on the X and Y.

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

        if new_head in self.snake:
            self.end = True
        self.snake.append(new_head)
        if new_head == self.food:

            ## STEP 4 - generate a new food.
            ## Your code goes here
            ## 1. Generate two random numbers ran_num1 and ran_num2 between 0 and 4 using randint(start, end).
            ## 2. Create a new food using [ran_num1, nan_num2]
            ## 2. Check whether new food is in snake using while.
            ## 3. If it is generate two random numbers again and create new food again.

            ## After you are done delete the next line.
            pass
        else:
            self.snake = self.snake[1:]

    def draw(self):
        """ This makes the game appear on the LEDs. """
        display.clear()
        display.set_pixel(self.food[0], self.food[1], 5)
        for part in self.snake:
            display.set_pixel(part[0], part[1], 9)

# game is an "instance" of Snake
game = Snake()

# this is called our "game loop" and is where everything
# happens
while True:
    game.handle_input()
    game.update()
    if game.end:
        display.show(Image.SAD)
        break
    game.draw()
    # this makes our micro:bit do nothing for 500ms
    sleep(500)
