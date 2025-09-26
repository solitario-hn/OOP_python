from tkinter import *
import json
import pyperclip #(helps us instantly copy or paste a text into our clipboard)
from random import choice , shuffle , randint
from tkinter import messagebox    # since messagebox is not a class it wasn't import when we typed * , only all classes got imported.
#Constants
FONTNAME="SF Mono"

#----------------------------ADDING A SEARCH OPTION-------------------------------------------------------
def search():
    to_search=entry_website.get()
    with open("data.json","r") as file:
        data=json.load(file)
    try:
        info_e=data[to_search]['Email']
        info_p=data[to_search]['Password']
    except KeyError:
        messagebox.showinfo(title="Not Found",message=f"Oops! Looks like {to_search} entry doesn't exist")
    else:
        messagebox.showinfo(title=to_search,message=f"Your Email:{info_e}\nYour Password:{info_p}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]
    password_list=password_letters+password_symbols+password_numbers   # the '+' operator in list joins the lists with adding one elemnt each at a time as oppose to append that adds whole elemnt passed as one elemnt.
    shuffle(password_list)

    password = "".join(password_list)    #this will join each elemnt in the list and return it in string format.
    entry_pass.insert(0,password)
    pyperclip.copy(password)    #this will copy our password onto our clipboard as soon as the password is generated
    messagebox.showinfo(title="PopUp",message="Password copied to clipboard")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_data=entry_website.get()
    email_data=entry_email.get()
    pass_data=entry_pass.get()
    new_dict={web_data:
        {"Email":email_data,
         "Password":pass_data}}
    res=True
    with open("data.json","r") as file:
        existing_data=json.load(file)
        for key in existing_data:
            if key==web_data:
                res=messagebox.askokcancel(title="Warning",message=f"Data with {web_data} already exists.\nClicking would rewrite the exisitng data")
                
    if res:
        if len(web_data)==0 or len(email_data)==0 or len(pass_data)==0:
            is_fine=messagebox.showwarning("Warning","You cannot leave empty entries.")
        else:
            is_ok=messagebox.askokcancel(title="Verification",message=f"The details you've entered:\nWebsite:{web_data}\nEmail:{email_data}\nPassword:{pass_data}\nIs it ok?")  #it returns a boolean(true or false value)
            if is_ok:
                try:
                    #Reading out the data from a data.json file.
                    with open("data.json", "r") as f:
                        data=json.load(f)
                        data.update(new_dict)   #this will update a new entry into the exisitng data instead of creating a completely new dict and just appending it like it happens in txt file.
                except FileNotFoundError:
                    #incase data.json file doesn't already exists
                    with open("data.json",'w') as f:
                        json.dump(new_dict, f,indent=4)   #indent-4 will make it easier to read new_dict=data we want to dump , f=where we want ot dump i.e. f(data.json) in this case.
                else:
                    #if the file already exists:
                    with open("data.json","w") as f:
                        json.dump(data,f,indent=4)         #dumping the updated data in the case when file already exists.
                finally:
                        entry_website.delete(0,END)
                        entry_pass.delete(0,END)
                        entry_website.focus()        #again putting the cursor back at the start.    
  
    

# ---------------------------- UI SETUP ------------------------------- #

#setting up the window 
window=Tk()
window.config(bg='white',padx=50,pady=50)
window.title("Password Manager")


#creating the canvas
canvas=Canvas(width=200,height=190,bg="white",highlightthickness=0)
image_gen=PhotoImage(file="logo.png")
canvas.create_image(100,95,image=image_gen)
canvas.grid(row=0,column=1)



#Creating the labels
website=Label(text="Website:",font=(FONTNAME,12,"bold"),bg='white',padx=5,pady=5)
website.grid(row=1,column=0)

email=Label(text="Email/Username:",font=(FONTNAME,12,"bold"),bg="white",padx=5,pady=5)
email.grid(row=2,column=0)

password=Label(text="Password:      ",font=(FONTNAME,12,"bold"),bg='white',padx=5,pady=5)
password.grid(row=3,column=0)


#Creating the Entries
entry_website=Entry(bg='white',width=21,highlightthickness=1,highlightcolor='violet')
entry_website.grid(row=1,column=1)
entry_website.focus()     #this will put the cursor into the webiste entry box aas soon aas the program is run

entry_email=Entry(bg='white',highlightthickness=1,highlightcolor='blue',width=40)
entry_email.grid(row=2,column=1,columnspan=3)
entry_email.insert(0,"kira890home@gmail.com")  #setting up a default value in the entry email using insert method 0 is in the index value at which the string passed would be added , one can use END(tkinter const.) to start the text after the very last of whatevr chaacter;s written



entry_pass=Entry(bg='white',highlightthickness=1,highlightcolor='red',width=21)
entry_pass.grid(row=3,column=1)

#Creating buttons
generate_pass=Button(text="Generate Password",bg='white',font=("Arial",12,"italic"),width=17,highlightthickness=1,padx=5,pady=5,height=1,highlightcolor='purple',command=generate_password)
generate_pass.grid(row=3,column=2)


add_button=Button(text="Add",bg='white',font=("Arial",12,"italic"),width=39,highlightthickness=1,padx=5,pady=5,height=1,highlightcolor='purple',command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text='Search',bg='white',font=("Arial",12,"italic"),width=16,highlightthickness=0,height=1,highlightcolor='purple',command=search)
search_button.grid(row=1,column=2,columnspan=2)






































window.mainloop()

