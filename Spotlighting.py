import turtle
from turtle import Turtle, Screen
import random

screen_obj = Screen()
turtle_obj = Turtle()
turtle.colormode(255)

turtle_obj.speed("fastest")
turtle_obj.penup()
turtle_obj.hideturtle()

list_color = ['#cf8d2e', '#371777', '#52325d', '#005670', '#48a9c5', '#222',
              '#6a67ce', '#2a5934', '#f67828', '#84754e', '#566127', '#d4c99e', '#464646', '#6b0f24',
              '#005be2', '#212a3e', '#ccc900', '#3949ab', '#2f6f7e', '#0b2d27', '#394956', 'dark blue', 'dark green',
              'gold', 'deep pink', 'indigo', 'yellow', 'chocolate', 'firebrick', 'dark slate gray', 'gray', '#2c9f45',
              '#00a4e4', '#ffc845', '#009f4d', '#b4a996', '#537b35', '#6a67ce', '#00b2a9', '#b3dcff']

turtle_obj.setheading(225)
turtle_obj.forward(300)
turtle_obj.setheading(0)
num_of_dots = 100

for dot in range(1, num_of_dots+1):
    turtle_obj.dot(20, random.choice(list_color))
    turtle_obj.forward(50)

    if dot % 10 == 0:
        turtle_obj.setheading(90)
        turtle_obj.forward(50)
        turtle_obj.setheading(180)
        turtle_obj.forward(500)
        turtle_obj.setheading(0)


screen_obj.exitonclick()
