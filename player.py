from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
# TODO: 1. Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the
#  turtle north. STEP 3

# TODO: 3. Detect when the turtle player collides with a car and stop the game if this happens. STEP 5

# TODO: 4. Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
#  When this happens, return the turtle to the starting position and increase the speed of the cars.
#  Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. STEP 6


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    @staticmethod
    def collision(x, player):
        for car in x:
            if car.distance(player) < 20:
                return True

    def finish(self, player):
        if player.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.penup()
            self.shape('turtle')
            return True
