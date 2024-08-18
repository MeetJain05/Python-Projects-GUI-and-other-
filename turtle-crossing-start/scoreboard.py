from turtle import Turtle
FONT = ("Courier",20, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()

        self.game_level = 0
        self.penup()
        self.goto(-280,250)
        self.hideturtle()
        self.level_update()

    def level_update(self):
        self.game_level += 1
        self.clear()
        self.write(f'Level: {self.game_level}',align='Left',font = FONT)
    
    def game_over(self):

        over = Turtle()
        over.hideturtle()
        over.write('GAME OVER',align='center',font = FONT )
