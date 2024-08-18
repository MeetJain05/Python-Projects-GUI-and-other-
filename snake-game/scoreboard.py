from turtle import Turtle
ALIGHNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        
        with open('highscore.txt') as file:
            self.highscore = int(file.read())

        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.highscore}', font=FONT, align=ALIGHNMENT)

    def increase_score(self):

        self.score += 1
        self.updatescoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', mode = 'w') as file:
                file.write(str(self.highscore))

        self.score = 0
        self.updatescoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER')