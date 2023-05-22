from turtle import Turtle
from player import Player
FONT = ("Courier", 24, "normal")
player = Player()
player.hideturtle()

# TODO: 5. Create a scoreboard that keeps track of which level the user is on.
#  Every time the turtle player does a successful crossing, the level should increase.
#  When the turtle hits a car, GAME OVER should be displayed in the centre. STEP 7


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.hideturtle()

    def next_level(self, character):
        if player.finish(character) is True:
            self.score += 1
            self.clear()
            self.penup()
            self.goto(-250, 250)
            self.write(f"Level: {self.score}", move=False, align='left', font=FONT)
            return True
        else:
            self.clear()
            self.penup()
            self.goto(-250, 250)
            self.write(f"Level: {self.score}", move=False, align='left', font=FONT)
