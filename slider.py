from turtle import Turtle

class Slider(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setpos(0, -230)
        self.turtlesize(stretch_wid=1, stretch_len=10)
        self.fillcolor('navy')

    def go_right(self):
        if self.xcor() < 400:
            new_x = self.xcor() + 100
            self.setx(new_x)

    def go_left(self):
        if self.xcor() > -400:
            new_x = self.xcor() - 100
            self.setx(new_x)