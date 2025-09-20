from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PING PONG GAME")


#TODO 1:CREATING PADDLE AND MAKING IT MOVE THROUGH ARROWS
screen.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")          #since we cannot use same keys for both paddles we will use different keys for each paddles.
ball=Ball()
score=Scoreboard()

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(ball.velocity)
    ball.move()
    #detecting collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
    #     #needs to bounce back in this case.
        ball.bounce()
        
    # if ball.distance(r_paddle)<10 or ball.distance(l_paddle)<10:
    #     ball.ball_hit()      distance method is not working because distance measures the distance between the centre of the turtle and object.
    
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.hit()

    if ball.xcor()>380:
        ball.reset()
        score.l_scored()
        
    if ball.xcor()<-380:   
        ball.reset()
        score.r_scored()
        



screen.exitonclick()
