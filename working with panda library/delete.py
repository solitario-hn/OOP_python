from tkinter import *
import pandas
#Constants
FONTNAME="SF Mono"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web=[entry_website.get()]
    em=[entry_email.get()]
    pas=[entry_pass.get()]
    
    data_dict={
        "website":[web],
        "Email":[em],
        "Password":[pas],
    }
    pass_file=pandas.DataFrame(data_dict)
    try:
        # Try to read existing file and append
        existing_data = pandas.read_csv("data.txt", index_col=0)  #index col ignores the index column .
        updated_data = pandas.concat([existing_data, pass_file], ignore_index=True)   #ignore index helps in dataframe to ignore the index value , and just create another line without creating duplicate indexes.
        updated_data.to_csv("data.txt")
    except FileNotFoundError:
        # File doesn't exist, create new one
        pass_file.to_csv("data.txt")
    
    # Clear the entries after saving
    entry_website.delete(0, END)
    entry_pass.delete(0, END)

# df1 = pandas.DataFrame({"name": ["Alice"], "age": [25]})  # index: [0]
# df2 = pandas.DataFrame({"name": ["Bob"], "age": [30]})    # index: [0]

# Without ignore_index:
#result = pandas.concat([df1, df2])
# Creates:  name   age
#       0   Alice  25
#       0   Bob    30    <- Duplicate index!

# With ignore_index=True:
#result = pandas.concat([df1, df2], ignore_index=True)
# Creates:  name   age
#       0   Alice  25
#       1   Bob    30    <- Clean sequential index


# # Without index_col:
# df = pandas.read_csv("data.txt")
# # Creates:  Unnamed: 0    website    Email    Password
# #           0             google     john@    pass123
# #           1             facebook   jane@    abc456

# # With index_col=0:
# df = pandas.read_csv("data.txt", index_col=0)  
# # Creates:  website    Email    Password
# #           google     john@    pass123
# #           facebook   jane@    abc456

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
entry_website=Entry(bg='white',width=35,highlightthickness=1,highlightcolor='black')
entry_website.grid(row=1,column=1,columnspan=2)
entry_website.focus()     #this will put the cursor into the webiste entry box aas soon aas the program is run

entry_email=Entry(bg='white',highlightthickness=1,highlightcolor='blue',width=35)
entry_email.grid(row=2,column=1,columnspan=2)
entry_email.insert(0,"kira890home@gmail.com")  #setting up a default value in the entry email using insert method 0 is in the index value at which the string passed would be added , one can use END(tkinter const.) to start the text after the very last of whatevr chaacter;s written



entry_pass=Entry(bg='white',highlightthickness=1,highlightcolor='red',width=21)
entry_pass.grid(row=3,column=1)

#Creating buttons
generate_pass=Button(text="Generate Password",bg='white',font=("Arial",12,"italic"),width=16,highlightthickness=1,padx=5,pady=5,height=1,highlightcolor='purple')
generate_pass.grid(row=3,column=2)

add_button=Button(text="Add",bg='white',font=("Arial",12,"italic"),width=39,highlightthickness=1,padx=5,pady=5,height=1,highlightcolor='purple',command=save)
add_button.grid(row=4,column=1,columnspan=2)






































window.mainloop()

