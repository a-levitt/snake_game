from turtle import Turtle

ALIGMENT = "center"
FONT = ('Courier', 10, 'normal')

class ScoreBoard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.ht()
            self.penup()
            self.goto(0, -270)
            self.update_score()

        def update_score(self):
            self.write(f"Score: {self.score}", move=False, align=ALIGMENT, font=FONT)

        def game_over(self):
            #self.clear()
            self.goto(0,0)
            self.write("GAME OVER", align="center",
                             font=('Arial', 20, 'normal'))

        def increase_score(self):
            self.clear()
            self.score += 1
            self.update_score()