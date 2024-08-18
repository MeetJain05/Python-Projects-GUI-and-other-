from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle_right = Paddle((350,0))

paddle_left = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_right.up,'Up')
screen.onkeypress(paddle_right.down,'Down')
screen.onkeypress(paddle_left.up,'w')
screen.onkeypress(paddle_left.down,'s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # ball collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_right) < 50 or ball.xcor() < -320 and ball.distance(paddle_left) < 50:
        ball.bounce_x()
    # right paddle misses
    if ball.xcor() > 380:  
        ball.reset()
        scoreboard.l_point()
        
    # left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()