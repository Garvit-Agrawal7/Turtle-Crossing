import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

pickachu = Turtle()
pickachu.hideturtle()
player = Player()
car_manager = CarManager()
car_manager.hideturtle()
scoreboard = Scoreboard()

game_is_on = True


def game_over():
    global game_is_on
    if player.collision(car_manager.cars, player) is True:
        pickachu.penup()
        pickachu.write("Game Over", move=False, align='center', font=('algerian', 30, 'normal'))
        pickachu.goto(0, 0)
        game_is_on = False


n = 0
screen.listen()
screen.onkeypress(player.move, 'Up')
car_manager.spawn()
while game_is_on is True:
    n += 1
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    if n % 6 == 0:
        car_manager.spawn()
    game_over()
    scoreboard.next_level(player)
    if player.finish(player) is True:
        car_manager.levelup()
    player.finish(player)
screen.exitonclick()
