from turtle import Turtle, Screen
import heroes

print (heroes.gen())
#=> Hooded

print (heroes.genarr(3))
#=> ['Askew-Tronics', 'Decepticon', 'Leopardon']

tim = Turtle()
tim.color('red')

print(tim)

screen = Screen()
screen.exitonclick()

