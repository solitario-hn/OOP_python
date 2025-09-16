from turtle import Turtle
ALIGNMENT="center"       #we write these constant values at top so we can easily modify them later in our game if we wish to
FONT=("Arial",12,"normal")     
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()  #so path is not visible
        self.goto(0,270)   #so that the scoreboard is at the top of the game not anywhere centre
        self.color('white')
        self.hideturtle()
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)
        self.update_scoreboard()
    
    def update_scoreboard(self):       #since this line was repeating in each modifier we made it a sep modifier to make the code look more cleaner.
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT) 
            
    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! Bye." , align=ALIGNMENT,font=FONT)
