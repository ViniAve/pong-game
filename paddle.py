from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
