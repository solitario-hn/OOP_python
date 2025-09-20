from turtle import Turtle
from turtle import Turtle , Screen
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PING PONG GAME")



paddle=Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1,stretch_wid=5)
paddle.penup()
paddle.goto(350,0)


time.sleep(0.1)
newy=paddle.ycor()+90
paddle.goto(x=350,y=newy)




screen.exitonclick()