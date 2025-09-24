# import tkinter

# window=tkinter.Tk()
# window.title("My first GUI Program")
# window.minsize(width=500,height=300)   #the window screen for tkinter is usually resizable by itself according to the components you put into it, but you can put minsize so it doesn't shrinks much if you min components.
# window.config(padx=100,pady=100)
# #label
# my_label=tkinter.Label(text="A LABEL",font=("Arial",8,"bold"))
# my_label.grid(column=0,row=0)           #any component (in this case label) wouldnt' show up on screen unless we pack it using the pack funcion. we can give various arguments in pack as well to decide the position of the given component.

# my_label['text']="New text"   #since kw arguments are saved in form of dict we can tap into it's key like we do in dict nd then change it's value.
# my_label.config(text='what?')  #we can also use the config method .
# my_label.config(padx=20,pady=20)

# entry=tkinter.Entry(width=20)
# entry.grid(column=3,row=2)
# # entry.config(padx=20,pady=20) cannot add padding to a entry box.
# def button_clicked():
#     #Entry fnction
#     my_label.config(text=entry.get())

# button=tkinter.Button(text="Click me",command=button_clicked)
# button.grid(column=1,row=1)  #too pack and show the button on screen
# button.config(padx=20,pady=20)

# new_button=tkinter.Button(text='New button',command=button_clicked)
# new_button.grid(column=2,row=0)
# new_button.config(padx=20,pady=20)




#CREATING A MILE TO KILOMETER GUI BASED CONVERTER.
import tkinter



def calculate():
    num=float(entry.get())
    num=num* 1.609
    res= round(num,2)
    result.config(text=res)

#creating a scene
window=tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200,height=200)

#Creating labels
#supporting label
equals=tkinter.Label(text="equals to :",padx=20,pady=20,font=("Arial",10,"bold"))
equals.grid(row=1,column=0)

#miles label
miles=tkinter.Label(text="MILES",padx=20,pady=20)
miles.grid(column=2,row=0)

#km label
km=tkinter.Label(text='KILOMETRE',padx=20,pady=20)
km.grid(row=1,column=2)

#result label
result=tkinter.Label(text=0,padx=20,pady=20,font=("Arial",10,"bold"))
result.grid(row=1,column=1)

#entry
entry=tkinter.Entry(width=20)
entry.grid(row=0,column=1)


#button
calculate=tkinter.Button(padx=20,pady=20,text='Calculate',command=calculate)
calculate.grid(row=2,column=1)
























































window.mainloop()
