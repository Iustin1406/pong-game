import time
from turtle import Turtle, Screen

screen = Screen()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_speed = 4
        self.y_speed = 4
        self.center()
        self.penup()

    def center(self):
        self.penup()
        self.goto(0, 0)
        screen.update()
        time.sleep(0.5)

    def check_bounce(self):
        if self.ycor() <= -278 or self.ycor() >= 278:  # if the ball hit the upper or lower of the screen
            self.y_speed *= -1

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
        self.check_bounce()
