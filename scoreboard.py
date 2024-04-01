from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-120, 220)
        self.write(self.l_score, False, "center", ("Courier", 50, "bold"))
        self.goto(120, 220)
        self.write(self.r_score, False, "center", ("Courier", 50, "bold"))

    def left_score(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.clear()
        self.r_score += 1
        self.update_score()

    def results(self):
        if self.l_score == 11:
            self.goto(0, 0)
            self.write("Left Wins", False, "center", ("Courier", 50, "bold"))
        elif self.r_score == 11:
            self.goto(0, 0)
            self.write("Right Wins", False, "center", ("Courier", 50, "bold"))
