from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time #helps in delaying the motion we see on canvas  
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
#TODO 1:Creating the snake body
screen.tracer(0)       #using tracer to hide the turtle until it starts moving 
snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food=Food()
scoreboard=Scoreboard()
is_game_on=True
while is_game_on:
    screen.update()      #putting update outside for loop so turtle shows as soon as the body is created(todo 1 )happens before running into for loop.
    time.sleep(0.1)     #so the delay is not much
    snake.move()
    #To do game over whenever snake head touches the wall. 
    if snake.head.xcor()<-285 or snake.head.xcor()>285 or snake.head.ycor()<-285 or snake.head.ycor()>285:
        snake.reset()
        scoreboard.reset()
        
    #detecting when head hits any segment of the snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            snake.reset()
            scoreboard.reset()
    #to detect collision with the food and increasing snake body.
    if snake.head.distance(food)<15:
        food.refresh_food()
        scoreboard.increase_score()
        snake.extend()   
     
screen.exitonclick()  
