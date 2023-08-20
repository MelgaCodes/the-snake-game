from the_module import *
import turtle
import random


turtle.colormode(255)
screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=620, height=520)
screen.bgcolor('ghost white')
set_up()
snake = Snake()
food = turtle.Turtle(shape='circle')
food.penup()
food.speed(0)
food.color(FOOD_COLOR)
raw_x = random.randint(-270, 270)
grilled_x = raw_x - raw_x % 20
raw_y = random.randint(-210, 140)
grilled_y = raw_y - raw_y % 20
food.goto(grilled_x, grilled_y)
food.turtlesize(0.5)
screen.update()


def head_north():
    if snake.head.heading() != 270:
        snake.head.setheading(90)


def head_south():
    if snake.head.heading() != 90:
        snake.head.setheading(270)


def head_east():
    if snake.head.heading() != 180:
        snake.head.setheading(0)


def head_west():
    if snake.head.heading() != 0:
        snake.head.setheading(180)


def food_relocate():
    raw_x = random.randint(-270, 270)
    grilled_x = raw_x - raw_x % 20
    raw_y = random.randint(-210, 140)
    grilled_y = raw_y - raw_y % 20
    food.goto(grilled_x, grilled_y)
    food.color(FOOD_COLOR)


def game_over():
    janitor = turtle.Turtle()
    janitor.goto(-125, -35)
    janitor.write("GAME OVER", font=('default', 30, "normal"))

screen.listen()
screen.onkey(fun=head_north, key='Up')
screen.onkey(fun=head_south, key='Down')
screen.onkey(fun=head_east, key='Right')
screen.onkey(fun=head_west, key='Left')

score = 0

def update_banner(banner_man):
    banner_man.penup()
    banner_man.hideturtle()
    banner_man.goto(-142, 175)
    banner_man.pencolor((random.randint(100, 220), random.randint(100, 220), random.randint(100, 220)))
    banner_man.write("SNAKE GAME", font=('segoe', 30, "italic"))


banner_man = turtle.Turtle()
update_banner(banner_man)


def update_score(score_keeper):
    score_keeper.penup()
    score_keeper.hideturtle()
    score_keeper.goto(190, 172)
    score_keeper.write(f"Score: {score}", font=('verdana', 12, "normal"))


score_keeper = turtle.Turtle()
update_score(score_keeper)
banner_control = 0

while True:
    snake.move_forward()
    screen.update()
    if snake.is_dead():
        for i in range(3):
            time.sleep(0.3)
            snake.head.color((5, 35, 20))
            for square in snake.body:
                square.color('ghost white')
            screen.update()
            time.sleep(0.3)
            snake.head.color('OrangeRed4')
            for square in snake.body:
                square.color(SNAKE_COLOR)
            screen.update()
        game_over()
        break
    if snake.head.distance(food) < 15:
        food_relocate()
        screen.update()
        snake.grow()
        score += 1
        score_keeper.clear()
        score_keeper = turtle.Turtle()
        update_score(score_keeper)
    if banner_control % 5 == 0:
        banner_man = turtle.Turtle()
        update_banner(banner_man)
    banner_control += 1

screen.exitonclick()
