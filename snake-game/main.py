from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

    # Detect Collision with wall.
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect Collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
           scoreboard.reset()
           snake.reset()

screen.exitonclick()
