from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]   #using all caps since it's a constant in our python code.
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]   #creating this list with self so we can use it in further classes of loop since outside class it's not attached to our object we create (self)
        self.create_snake()
        self.head=self.segments[0]  #assigning teh first segment '1' as the head of others so it will follow other(using move method)
    
    def create_snake(self):
        for positions in STARTING_POSITIONS:
          #saving each segment as an object into the list so we can use it later on.
            self.add_segment(positions=positions)
    
    def move(self):
            #using a for loop with range function in order to get a result here 3rd segment follows - 2 follows 1- and 1 is headed wheere user asks its to - that way segments don't break.
        for seg in range(len(self.segments)-1,0,-1):   #raneg func works like c lang and doesn't take keyword arguemnts.
            pos=seg-1
            new_x=self.segments[pos].xcor()
            new_y=self.segments[pos].ycor()    #finding out x,y cordinates of the previous segment.
            self.segments[seg].goto(x=new_x,y=new_y)  #3rd no. segment follows 2nd no. segment.
        
        self.head.forward(MOVE_DISTANCE)   #only the 1st segment rest other segments are following it using our for loop.
    
    def add_segment(self,positions):   #creating a add segment since we have to put penup each time we create a new segment.
            new_segment=Turtle("square")
            new_segment.color("red")
            new_segment.penup() 
            new_segment.goto(positions)
            self.segments.append(new_segment) 
               
    def extend(self):    #to add a new segment to snake everytime it eats food.
        x_cor=self.segments[-1].xcor()   #using -1 slicing to attach new segment to the last segment 
        y_cor=self.segments[-1].ycor()
        self.add_segment(positions=(x_cor,y_cor))
     
     
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]  
       
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)                  #adding a if condition to everything since in real snake game you're not allowed to change your head direction once you're headed in one.
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        
        
            