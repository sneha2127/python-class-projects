# Tkinter Start

from tkinter import *
from tkinter import colorchooser

window = Tk()

# geometry("widthxheight")
window.geometry("500x500")


# title("title")
window.title("First Software")


# Widget: 2 steps
# 1. define the widget object from the respective widget class
# 2. We need to pack the widget into the window

# Label Widget
# text_lbl = Label(window,text="This is my first software!")
# text_lbl.pack(pady=10)


# Button Function
# def showValue():
#     # print("Hello, world!")
#     text_lbl.config(text="Good, Morning")


# Button Widget
# btn_obj = Button(window,text="Click Me", command=showValue)
# btn_obj.pack(pady = 10)


# text_lbl = Label(window)
# text_lbl.pack(pady=10)


# Entry Widget

# text_lbl = Label(window,text="Enter your name")
# text_lbl.pack(pady=10)


# entry_name = Entry(window)
# entry_name.pack(pady=10)

# def greetUser():
#     user_name = entry_name.get()
#     greet_lbl.config(text=f"Hello, {user_name}!")

# btn_obj = Button(window,text="Greet Me", command=greetUser)
# btn_obj.pack(pady = 10)


# greet_lbl = Label(window)
# greet_lbl.pack(pady=10)



# List Box:

# lb = Listbox(window,width=50, height=20)

# lb.insert(1,"Python")
# lb.insert(2,"C++")
# lb.insert(3,"Java")

# lb.pack(pady=10)

# lb.delete(0)


# Color Choose
def changeBg():
    color = colorchooser.askcolor()
    # window.config(bg=color[1])
    btn_obj.config(bg=color[1],fg="white")


btn_obj = Button(window, text = "Choose a color", command=changeBg)
btn_obj.pack(pady=10)



window.mainloop()


