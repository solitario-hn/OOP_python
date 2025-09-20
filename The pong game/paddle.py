from turtle import Turtle 
X_POS=350
Y_POS=0
UP=90
DOWN=270
MOVE_DISTANCE=10


class Paddle(Turtle):
    def __init__(self,positions:tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(positions)
    
        # def up(self):            this method is not working since now our object is in shape of rectange and we only want to move it along it's y cor.
    #     self.setheading(UP)
    
    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
       
    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)
        
    


