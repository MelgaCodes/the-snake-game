import time
import turtle
from time import sleep


SNAKE_COLOR = 'red3'
SNAKE_SIZE = 0.9
FOOD_COLOR = 'gold'


class Snake:
    alive = True
    head = turtle.Turtle(shape="square")
    head.color('OrangeRed4')
    head.turtlesize(SNAKE_SIZE)
    head.penup()
    body = [turtle.Turtle(shape="square"), turtle.Turtle(shape="square")]
    previous_position = head.position()
    for square in body:
        square.penup()
        square.turtlesize(SNAKE_SIZE)
        square.color(SNAKE_COLOR)
        current_position = (previous_position[0] - 20, previous_position[1])
        square.goto(current_position)
        previous_position = current_position

    def move_forward(self):
        sleep(0.1)
        self.head.speed(0)
        previous_position = self.head.position()
        self.head.forward(20)
        for square in self.body:
            square.speed(0)
            square.penup()
            current_position = square.position()
            square.goto(previous_position)
            previous_position = current_position

    def grow(self):
        new_body_part = turtle.Turtle(shape='square')
        new_body_part.penup()
        new_body_part.turtlesize(SNAKE_SIZE)
        new_body_part.color(SNAKE_COLOR)
        self.body.append(new_body_part)

    def is_dead(self):
        for part in self.body:
            if self.head.position() == part.position():
                return True
            if self.head.xcor() > 260 or self.head.xcor() < -280 or self.head.ycor() > 150 or self.head.ycor() < -230:
                return True
        return False



def set_up():
    janitor = turtle.Turtle()
    janitor.speed(0)
    janitor.hideturtle()
    janitor.penup()
    janitor.goto(290, 250)
    janitor.color((5, 35, 20))
    janitor.pendown()
    janitor.pensize(40)
    janitor.goto(290, -250)
    janitor.goto(-310, -250)
    janitor.goto(-310, 250)
    janitor.goto(290, 250)
    janitor.pensize(20)
    janitor.goto(290, 160)
    janitor.goto(-300, 160)
