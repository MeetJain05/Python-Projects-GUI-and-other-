import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars(scoreboard.game_level)
    if player.ycor() > 280:
        player.reset()
        scoreboard.level_update()
    #detect collision with car
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
    
