from turtle import Turtle

class Score(Turtle):

        def __init__(self):
            super().__init__()
            self.penup()
            self.score=0
            self.hideturtle()
            self.setpos(-80, +190)
            self.write(f"Score : {self.score} ", font=("Cooper Black", 40, "italic"))

        def update_score(self):
            self.score += 1;
            self.clear()
            self.write(f"Score :{self.score} ", font=("Cooper Black", 40, "italic"))

