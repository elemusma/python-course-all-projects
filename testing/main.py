import tkinter as TK
from turtle import Turtle, Screen
import heroes


tim = Turtle()
tim.shape("turtle")
tim.color("red")


for  _ in range(4):
    tim.forward(100)
    tim.right(90)


print(tim)


screen = Screen()
screen.exitonclick()


print(heroes.gen())
print (heroes.genarr(3))