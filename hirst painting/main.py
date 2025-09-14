# import colorgram   (extracting colors using colorgram package from a real life hirst paininting)
# colors=colorgram.extract('damien-hirst-currency-dot-painting.jpeg',30)
# color=[]
# for i in colors:     
#     # color.append(i.rgb)  #this will give out separate tules with r=,g=and b= #TODO 1:we need it in simple tuple format.
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     my_tuple=(r,g,b)
#     color.append(my_tuple)
    
# print(color)

import turtle as turtle_module
from turtle import Turtle,Screen
import random

turtle_module.colormode(255)      #so it can use rgb colors of variation 0-255
color_list=[(224, 162, 84), (33, 116, 153), (145, 73, 99), (46, 125, 86), (205, 131, 151),(123, 173, 199),(212, 83, 65), (169, 71, 53), (194, 87, 108), (211, 225, 235), (228, 199, 128), (130, 179, 151), (68, 157, 119), (156, 157, 62), (243, 166, 153), (36, 161, 174), (231, 166, 181), (12, 104, 71), (114, 41, 55), (153, 210, 192), (33, 61, 111), (107, 119, 172), (145, 208, 218), (32, 55, 79), (121, 40, 35), (179, 186, 214), (17, 90, 101)]
tim=Turtle()

tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def tim_moves_upleft():
    tim.dot(20,random.choice(color_list))
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    
def tim_moves_upright():
    tim.dot(20,random.choice(color_list))
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)

def tim_moves():
    for i in range(9):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)

for i in range(5):
    tim_moves()
    tim_moves_upleft()
    tim_moves()
    tim_moves_upright()
    
screen=Screen()
screen.exitonclick()     #creating screen object and using exit on click so screen doesn't just exits aburptly without us clicking.