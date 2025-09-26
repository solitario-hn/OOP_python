from turtle import Screen,Turtle
import random

is_race_on=False

screen=Screen()
screen.setup(width=1000,height=500)
screen.title("The Turtle Race")
screen.bgcolor('black')


colors=["SpringGreen","blue","VioletRed2","tomato3","orange","green"]
name=["Bablu","Nidhi","Hemant","Anaya","Hem","Hemu"]
# Show the user who is playing after creating all turtles
players_list = ", ".join(name)
user_bet = screen.textinput(title="Make your bet!", 
                           prompt=f"Players: {players_list}\n\nWho do you think will win the race? Enter the name: ")
y_pos=[-200,-150,-100,-50,0,50]
all_turtles=[]

for i in range(6):
   
    new_turtle=Turtle(shape="turtle")
    new_turtle.name=name[i]
    col=colors[i]
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-490,y=y_pos[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor()>480:
            is_race_on=False
            winning_color=turtles.pencolor()
            winner_name=turtles.name
            if winner_name.lower()==user_bet.lower():
                print(f"You've won.{winner_name} won the game.")
            else:
                print(f"You've lost.{winner_name} won the game.")
        random_distance=random.randint(0,10)
        turtles.forward(random_distance)






















screen.exitonclick()