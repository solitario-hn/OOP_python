import turtle 
import pandas
screen=turtle.Screen()
screen.title("US states Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer=turtle.Turtle()

# def get_mouse_click_coor(x,y):
#     print (x,y)                     this function prints out the coordinates of the points whereneve we click the mouse on.
# turtle.onscreenclick(get_mouse_click_coor) 
# turtle.mainloop()             #this keeps the screen open till we've exit it manually so screen doesn't exits on clicks like it does on screen.exitonclick()\
    
#TODO 1:Creating a text input pop up box for the user to type the answer into

us_states=pandas.read_csv("50_states.csv")
x_pos=us_states['x'].to_list()       #fetching all x and y position from the csv file.
y_pos=us_states["y"].to_list()
state_name=us_states['state'].str.lower().to_list()      #converting fetched state names to lower to avoid lag incase user inputs it into diff caps.
states_correct=0
corrected_ans=[]

answer_state=screen.textinput(title="US STATES GAME", prompt=f"Name a US state :").lower()
while len(corrected_ans)<50:
    answer_state=screen.textinput(title="US STATES GAME", prompt=f"{states_correct}/50 States Correct ,Name another: ").lower()
    if answer_state=="exit":
        missing_states=[state for state in state_name if state not in corrected_ans]
        dict={
            "states_to_learn":missing_states
        }
        states_to_learn=pandas.DataFrame(dict)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in state_name:
        index=state_name.index(answer_state)
        writer.penup()
        writer.goto(x_pos[index],y_pos[index])
        writer.write(f"{answer_state}",font=("Arial",6,"normal"))
        if answer_state not in corrected_ans:
            corrected_ans.append(answer_state)
            states_correct+=1
        else:
            pass
    else:
        pass


turtle.mainloop() 

