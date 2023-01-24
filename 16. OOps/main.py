from turtle import Turtle, Screen

timmy = Turtle()  # timmy - object, Turtle - class
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvwidth)
my_screen.exitonclick()
