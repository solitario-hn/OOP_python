BACKGROUND_COLOR = "#B1DDC6"
TEXTCOLOR="#581845"
FONTNAME="Allura"
COLOR="#44314A"
from tkinter import *
import pandas
import random 

#---------------------------------READING DATA FROM THE FILE --------------------------------------------------------

current_card={} 
to_learn={} 
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient='records')       #orient records will rearrange the dict [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},...] in this format so it makes it easy to tap into values.
else:
    to_learn=data.to_dict(orient="records")

def flip_card():
    
    canvas.itemconfig(image_creation,image=back_image)
    canvas.itemconfig(text1,text="English",fill="brown")
    canvas.itemconfig(text_french,text=current_card["English"],fill="brown")
   
    
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)            #this will stop the counting as soon as the next card is tick button clicked.
    current_card=random.choice(to_learn)
    canvas.itemconfig(image_creation,image=front_image)
    canvas.itemconfig(text1,text="French",fill=TEXTCOLOR)
    canvas.itemconfig(text_french,text=current_card["French"],fill=TEXTCOLOR)
    flip_timer=window.after(2000,flip_card)
    
    
def remove():
        to_learn.remove(current_card)
        data=pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv",index=False)
        next_card()
                 
#------------------------------------SETTING UP THE UI--------------------------------------------
window=Tk()
window.title("Flash French Learner")
window.config(bg=BACKGROUND_COLOR,width=800,height=526,padx=50,pady=50)


flip_timer=window.after(2000,flip_card) #placement of this method really matters since it calls flipcard function.
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_image=PhotoImage(file="images/card_front.png")
back_image=PhotoImage(file="images/card_back.png")
image_creation=canvas.create_image(400,263,image=front_image)
text1=canvas.create_text(400,150,text="Let's Learn",fill=TEXTCOLOR,font=(FONTNAME,40,"italic")) 
text_french=canvas.create_text(400,263,text="words",fill=TEXTCOLOR,font=(FONTNAME,60,"bold")) 
canvas.grid(row=0,column=0,columnspan=2)



#Buttons
tick_image = PhotoImage(file="images/right.png")
right = Button(image=tick_image, highlightthickness=2,highlightcolor=COLOR,highlightbackground=COLOR,command=remove)
right.grid(row=1,column=0)

cross_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=cross_image, highlightthickness=2,highlightcolor=COLOR,highlightbackground=COLOR,command=next_card)
wrong.grid(row=1,column=1)

next_card()
# start_button=Button(text="Start", highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR,command=start,width=5)
# start_button.grid(row=2,column=0,columnspan=2)
































window.mainloop()