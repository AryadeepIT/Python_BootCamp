import colorgram
import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

rgb_colors = []
colors = colorgram.extract('img/hirst-painting.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# print(rgb_colors)

t.colormode(255)
color_list = [(58, 106, 148), (224, 200, 111), (134, 85, 59), (222, 139, 64), (234, 225, 203), (195, 145, 171), (144, 178, 203), (223, 233, 229), (138, 82, 106), (208, 91, 70), (236, 222, 231), (68, 105, 90), (134, 182, 136), (186, 80, 121), (65, 155, 91), (50, 155, 193), (128, 134, 76), (183, 192, 201), (213, 177, 190), (23, 68, 111), (20, 60, 94), (116, 125, 146), (173, 204, 184), (229, 174, 163), (154, 205, 215), (71, 64, 53), (101, 50, 62), (163, 36, 29), (66, 61, 54)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()