from turtle import Turtle
from random import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# TODO: 2. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left
#  edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone
#  for our little turtle). Hint: generate a new car only every 6th time the game loop runs. STEP 4


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(choice(COLORS))
        n = randint(-250, 250)
        car.goto(300, n)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            if car.xcor() >= -300:
                new_x = car.xcor() - self.car_speed
                car.goto(new_x, car.ycor())
            else:
                car.hideturtle()

    def levelup(self):
        self.car_speed += MOVE_INCREMENT
