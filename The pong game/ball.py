from turtle import Turtle
X_POS=0
Y_POS=0
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(x=X_POS,y=Y_POS)
        self.x_move=10
        self.y_move=10
        self.velocity=0.1
        
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)        
        
    def bounce(self):
        self.y_move*=-1      #reverses vertically
        
    def hit(self):
        self.x_move*=-1      #reverses horizontally
        self.velocity*=0.9

    def reset(self):
        self.goto(x=X_POS,y=Y_POS)
        self.velocity=0.1
        self.x_move*=-1
      
        