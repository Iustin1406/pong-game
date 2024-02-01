import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    if ball.xcor() <= -345 and l_paddle.distance(ball) <= 50:
        ball.x_speed *= -1

    if ball.xcor() >= 345 and r_paddle.distance(ball) <= 50:
        ball.x_speed *= -1

    if ball.xcor() <= -378:  # point for the right side
        ball.x_speed *= -1
        scoreboard.r_score += 1
        scoreboard.update_score()
        ball.center()

    if ball.xcor() >= 378:  # point for the left side
        ball.x_speed *= -1
        scoreboard.l_score += 1
        scoreboard.update_score()
        ball.center()

screen.exitonclick()
