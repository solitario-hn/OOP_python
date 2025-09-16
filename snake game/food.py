#creating a new class food that'll dictates food behaviour and it's appearance on the screen.
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()   #created a super classs(class inheritance) turtle from food and now decidicng food.
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)   #to make the food smaller 10x10 dimesion snake=20x20
        self.penup()
        self.speed("fastest")
        self.refresh_food()
        
    #creating a new method refresh tht will add more food after eating
    def refresh_food(self):
        x_pos=random.randint(-280,280)
        y_pos=random.randint(-280,280)
        self.goto(x=x_pos,y=y_pos)   
        