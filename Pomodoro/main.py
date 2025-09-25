from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None #creating variable timer in advance in order to access it later as global var inside the functions.

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_lab.config(text="Timer")
    canvas.itemconfig(text_gen,text="00:00")
    tick_mark.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    #so timer starts only when the start button is clicked.
    
    work_min_sec=WORK_MIN*60
    break_min_sec=SHORT_BREAK_MIN*60         #*60 converts it into minutes 
    longbreak_min_sec=LONG_BREAK_MIN*60
    global reps
    reps+=1
    if reps%8==0:
        timer_lab.config(text="NAP TIME",fg=RED)
        countdown(longbreak_min_sec)
    elif reps%2==0:
        timer_lab.config(text="Short Break",fg="pink")
        countdown(break_min_sec)
    else:
        timer_lab.config(text="WORK!!",fg=GREEN)
        countdown(work_min_sec)

        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min=math.floor(count/60)   #returns the non fraction part (largest integer <=x)
    count_sec=count%60   #returns remainder.

    if count_sec<10 :
        count_sec="0"+str(count_sec)          #we're here using dynamic typing to change the type of a var to fit the need at tht time.  
    if count_min==0:
        count_min="00"
    canvas.itemconfig(text_gen,text=f"{count_min}:{count_sec}")   #we use item.config in canvas to change any config. first arg is to tap into the text/image/whatever we wish to change into . and 2nd arg is change.
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1) #delays the display on the screen by ms (1st arg), object , 3rd arg is automactically taken as the parameter for the 2nd function called inside.
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        tick_mark.config(text=mark)
  #every single time a count down completes a tick mark goes there.


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=150,pady=100,bg=YELLOW)

#Creating a canvas canvas works diff than a window its a canvas stack over the window where we can stack multiple components but it's no the  main window itself.
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)   #choosing the canvas size acc to our size of img so it'll fit perfectly.
tomato_image=PhotoImage(file="tomato.png")        #a photoimage class in tkinter which helps us retirieve an image from a file
canvas.create_image(100,112,image=tomato_image)    #giving x and y coordinates as centre of window to place image evenly out.
text_gen=canvas.create_text(100,140,text="00:00",fill="pink",font=(FONT_NAME,35,"bold"))  #to use item config we need to firt store create text into a separate variable.
canvas.grid(row=1,column=1)


#creating labels and buttons on the window
timer_lab=Label()
timer_lab.config(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW,padx=20,pady=20)
timer_lab.grid(column=1,row=0)

tick_mark=Label()
tick_mark.config(fg="darkgreen",bg=YELLOW,padx=20,pady=20)
tick_mark.grid(row=3,column=1)

start=Button(text="Start",bg="white",highlightbackground="black",highlightthickness=2,command=start_timer)
start.grid(row=2,column=0)


reset=Button(text="Reset",bg="white",highlightbackground="black",highlightthickness=2,command=reset_timer)
reset.grid(row=2,column=2)


























































window.mainloop()