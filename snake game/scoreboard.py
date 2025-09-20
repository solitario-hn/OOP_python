from turtle import Turtle
ALIGNMENT="center"       #we write these constant values at top so we can easily modify them later in our game if we wish to
FONT=("courier",12,"normal")     
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.penup()  #so path is not visible
        self.goto(0,270)   #so that the scoreboard is at the top of the game not anywhere centre
        self.color('white')
        self.hideturtle()
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)
        self.update_scoreboard()
    
    def update_scoreboard(self):       #since this line was repeating in each modifier we made it a sep modifier to make the code look more cleaner.
        self.clear()
        self.write(f"Score:{self.score} , HIGH SCORE:{self.high_score}",align=ALIGNMENT,font=FONT) 
            
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
        
    def reset(self):
        if self.score>self.high_score:
            with open("data.txt",mode="w+") as file:
               file.write(f"{self.score}")
               self.high_score=int(file.read())
        self.score=0
        self.update_scoreboard()
        
    

