from turtle import Turtle,Screen
import time #helps in delaying the motion we see on canvas
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
#TODO 1:Creating the snake body
screen.tracer(0)       #using tracer to hide the turtle until it starts moving 
starting_positions=[(0,0),(-20,0),(-40,0)]
segments=[]

for positions in starting_positions:
    new_segment=Turtle("square")
    new_segment.color("red")
    new_segment.penup()
    new_segment.goto(positions)
    segments.append(new_segment)              #saving each segment as an object into the list so we can use it later on.



is_game_on=True
while is_game_on:
    screen.update()      #putting update outside for loop so turtle shows as soon as the body is created(todo 1 )happens before running into for loop.
    time.sleep(0.1)     #so the delay is not much
    
    #using a for loop with range function in order to get a result hwere 3rd segment follows - 2 follows 1- and 1 is headed wheere user asks its to - that way segments don't break.
    for seg in range(len(segments)-1,0,-1):   #raneg func works like c lang and doesn't take keyword arguemnts.
        new_x=segments[seg-1].xcor()
        new_y=segments[seg-1].ycor()    #finding out x,y cordinates of the previous segment.
        segments[seg].goto(new_x,new_y)  #3rd no. segment follows 2nd no. segment.
        
    segments[0].forward(20)   #only the 1st segment rest other segments are following it using our for loop.
    segments[0].right(90)
        
        
    
screen.exitonclick()