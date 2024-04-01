from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "p")
screen.onkeypress(r_paddle.move_down, ";")

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 385:
        ball.reset_position()
        score.left_score()

    if ball.xcor() < -385:
        ball.reset_position()
        score.right_score()

    if score.l_score == 11 or score.r_score == 11:
        score.results()
        break

screen.exitonclick()
