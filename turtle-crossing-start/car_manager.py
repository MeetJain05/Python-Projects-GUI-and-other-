import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.cars_list = []

    def create_cars(self):
        random_num = random.randint(1,6)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.cars_list.append(new_car)

    def move_cars(self,level):
        for car in self.cars_list:
            car.forward(STARTING_MOVE_DISTANCE + 10*(level - 1))

    
    
                





    
