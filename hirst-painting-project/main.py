from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for  _ in range(4):
    tim.forward(100)
    tim.right(90)

print(tim)

screen = Screen()
screen.exitonclick()

import heroes

print(heroes.gen(3))