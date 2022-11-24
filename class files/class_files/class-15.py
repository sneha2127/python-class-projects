from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Rock Paper Scissor")


txt  =  Label(root,text="Choose from the below option!")
txt.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def getResult(user_choice,comp_choice):
    
    if user_choice == comp_choice:
        result="Match Draw!"
        result_string = f"User choice = {user_choice}\nComputer choice = {comp_choice}\n{result}"
        result_lbl.config(text=result_string)

    elif user_choice == "rock":
        if comp_choice == "paper":
            result = "Computer Win!"
            result_string = f"User choice = {user_choice}\nComputer choice = {comp_choice}\n{result}"
            result_lbl.config(text=result_string)

        elif comp_choice == "scissor":
            result="You Win"
            result_string = f"User choice = {user_choice}\nComputer choice = {comp_choice}\n{result}"
            result_lbl.config(text=result_string)

    elif user_choice == "paper":
        if comp_choice == "scissor":
            result = "Computer Win!"
            result_string = f"User choice = {user_choice}\nComputer choice = {comp_choice}\n{result}"
            result_lbl.config(text=result_string)

        elif comp_choice == "rock":
            result="You Win"
            result_string = f"User choice = {user_choice}\nComputer choice = {comp_choice}\n{result}"
            result_lbl.config(text=result_string)



    elif user_choice == "scissor":
        if comp_choice == "rock":
            result = "Computer Win!"
            result_string = f"User choice = {user_choice}\nComputer choice = {comp_choice}\n{result}"
            result_lbl.config(text=result_string)

        elif comp_choice == "paper":
            result="You Win"
            result_string = f"User choice = {user_choice}\nComputer choice = {comp_choice}\n{result}"
            result_lbl.config(text=result_string)




def rockFun():

    user_choice = "rock"
    comp_choice = random.choice(["rock","paper","scissor"])
    getResult(user_choice,comp_choice)

def paperFun():

    user_choice = "paper"
    comp_choice = random.choice(["rock","paper","scissor"])
    getResult(user_choice,comp_choice)


def scissorFun():

    user_choice = "scissor"
    comp_choice = random.choice(["rock","paper","scissor"])
    getResult(user_choice,comp_choice)



b1 = Button(root,text="Rock",command=rockFun)
b1.grid(row = 1, column = 0,padx=10,pady=10 )
b2 = Button(root,text="Paper",command=paperFun)
b2.grid(row = 1, column = 1 ,padx=10,pady=10)
b3 = Button(root,text="Scissor",command=scissorFun)
b3.grid(row = 1, column = 2 ,padx=10,pady=10)


result_lbl = Label(root)
result_lbl.grid(row=2,column=0,columnspan=3, padx=10,pady=10)

root.mainloop()