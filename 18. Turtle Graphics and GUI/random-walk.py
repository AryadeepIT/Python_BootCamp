import turtle as t
import random

tim = t.Turtle()
colors = ["blue", "dark green", "dark red", "blue violet", "rosy brown", "gold", "sea green"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
