# import colorgram
#
# colors = colorgram.extract('damien-hirst-spot-painting.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)
# colors from hirst painting
import turtle

rgb_colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
              (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
              (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158),
              (235, 166, 171), (177, 204, 185), (49, 62, 84)]
import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
#setting coordinates
timmy.setheading(225)
timmy.penup() #penup will keep the penup everytime and dotfunction will pendown and make dots
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    turtle.colormode(255)
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.right(180)



my_screen = Screen()
my_screen.exitonclick()

# # using goto function
# from turtle import Turtle, Screen, colormode
# import random
#
# color_list = [(230, 238, 246), (235, 245, 240), (200, 157, 115), (43, 110, 146), (134, 172, 193), (226, 208, 113),
#               (134, 84, 67), (148, 65, 85), (198, 140, 153), (193, 83, 102), (182, 159, 51), (150, 178, 164),
#               (191, 98, 83), (68, 114, 94), (227, 170, 182), (36, 51, 68), (225, 177, 168), (45, 157, 186),
#               (60, 47, 41), (155, 205, 218), (49, 56, 94), (22, 90, 76), (129, 38, 59), (58, 44, 52), (33, 60, 53),
#               (97, 146, 125), (173, 203, 189), (178, 188, 212)]
#
# tim = Turtle()
# colormode(255)
# tim.speed(0)
# tim.penup()
# tim.hideturtle()
#
# for y in range(-250, 250, 50):
#     for x in range(-250, 250, 50):
#         tim.goto(x, y)
#         # odd size gives more circular shape to dot, even number fives more polygonal shape
#         tim.dot(21, random.choice(color_list))
#
# screen = Screen()
# screen.exitonclick()