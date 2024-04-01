from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.08
        self.x_bounce()
        self.goto(0, 0)
