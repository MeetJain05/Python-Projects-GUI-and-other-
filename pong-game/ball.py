from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        
    def move(self):
        
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
        #bouncing from walls
    def bounce_y(self):
            self.y_move *= -1
        
        #bouncing from paddles
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.95

    def reset(self):
        self.move_speed = 0.05
        self.y_move *= -1
        self.x_move *= -1
        self.goto(0,0)