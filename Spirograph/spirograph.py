import turtle as t 
from turtle import Screen 
import random 
tim=t.Turtle()

# tim.shape("arrow")
# for i in range(26):
#     tim.pendown()
#     tim.color("black")
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)


#TODO 2: Creating diff shapes using turtle
# for i in sides:
#     tim_color=random.choice(colors)
#     tim.color(tim_color)
#     for x in range(i):
#         tim.right(360/i)
#         tim.forward(100)



#TODO 3:Creating a Random walk
# t.colormode(255) #we need to use the actual turtle module(changed alias to t ) to use this colormode
# direction=[0,90,180,270]

# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     tuple=(r,g,b)
#     return tuple


# tim.shape("turtle")
# tim.pensize(10)
# tim.speed(10)
# for i in range(250):
#     color=random_color()
#     tim.pencolor(color)
#     position=random.choice(direction)
#     tim.setheading(position)
#     tim.forward(30)


t.colormode(255) #we need to use the actual turtle module(changed alias to t ) to use this colormode


#TODO 4: Creating a spirograph.
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tuple=(r,g,b)
    return tuple


tim.shape("arrow")
tim.speed("fastest")


def spirograph(size_of_the_gap):
    for  i in range(int(360/size_of_the_gap)):            #using maths so that the arrow stops once it has fully titled till 360(i.e. made a complete circle)
        color=random_color()
        tim.pencolor(color)
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_the_gap)         #set heading sets it or titlts it acc to the direction 0=east , 90=west etc and heading returns it's current heading and size of gap adds number into it.


spirograph(2)

#TODO 1 : creating screen object from Screen class to use exit on click feature so screen doesn't exists until we click.
screen=Screen()
screen.exitonclick()
    # tim.right(120)
    # tim.forward(100)