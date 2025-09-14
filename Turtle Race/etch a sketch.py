from turtle import Screen,Turtle

tim=Turtle()
screen=Screen()

def tim_movesforward():
    tim.forward(50)
    
def tim_movesbackward():
    tim.backward(50)
    
def tim_anticlock():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
            
def tim_clock():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
    
screen.listen()                    #in order for allowing turtle to hear keys we press.     
screen.onkey(fun=tim_movesforward,key="w")          #we do not add paranthesis here , because adding () calls that fun and we only want to call that func when space key is pressed. 
                                                    #when we have a function as a paramter of another function we do not add paranthesis inside the paramter func.
                                                    #function which takes another func as an input is called an higher order function.
screen.onkey(fun=tim_movesbackward,key='s')
screen.onkey(fun=tim_anticlock,key='a')
screen.onkey(fun=tim_clock,key='d')
screen.onkey(fun=tim.reset,key='c')

screen.exitonclick()
