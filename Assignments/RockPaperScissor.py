from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Rock Paper Scissor")

list = ["Rock","Paper","Scissor"]
# computer_choice = choice(choices)

root.maxsize(width=800,height=550)
root.minsize(width=300,height=350)
txt  =  Label(root,text="Choose from the below option!")
txt.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

user_choice = "None"

def user_choice_b1():
    user_choice = "Rock"
    print(user_choice)
    computer_choice = random.choice(list)
    if computer_choice == "Paper":
        result_game= f"Your choice is {user_choice}. Computers choice was {computer_choice}. So Computer Wins!"
    elif computer_choice == "Scissor":
        result_game= f"Your choice is {user_choice}. Computers choice was {computer_choice}. So you win!"
    else:
        result_game= f"Your choice is {user_choice}. Computers choice was {computer_choice}. It's a draw!"
    result.config(text=result_game)
    

def user_choice_b2():
    user_choice = "Paper"
    print(user_choice)
    computer_choice = random.choice(list)
    if computer_choice == "Rock":
        result_game = f"Your choice is {user_choice}. Computers choice was {computer_choice}. So You Win!"
    elif computer_choice == "Scissor":
        result_game = f"Your choice is {user_choice}. Computers choice was {computer_choice}. So Computer Wins!"
    else:
        result_game = f"Your choice is {user_choice}. Computers choice was {computer_choice}. It's a draw!"
    result.config(text=result_game)

def user_choice_b3():
    user_choice = "Scissor"
    print(user_choice)
    computer_choice = random.choice(list)
    if computer_choice == "Paper":
        result_game= f"Your choice is {user_choice}. Computers choice was {computer_choice}. So You Win!"
    elif computer_choice == "Rock":
        result_game= f"Your choice is {user_choice}. Computers choice was {computer_choice}. So Computer Wins!"
    else:
        result_game= f"Your choice is {user_choice}. Computers choice was {computer_choice}. It's a draw!"
    result.config(text=result_game)
# def rock_paper_scissor_result():
      
  
      
    


b1 = Button(root,text="Rock",command=user_choice_b1)
b1.grid(row = 1, column = 0,padx=10,pady=10)
b2 = Button(root,text="Paper",command=user_choice_b2)
b2.grid(row = 1, column = 1 ,padx=10,pady=10)
b3 = Button(root,text="Scissor",command=user_choice_b3)
b3.grid(row = 1, column = 2 ,padx=10,pady=10)


result = Label(root,text=" ")
result.grid(row=3,column=0,columnspan=6, padx=10,pady=10)



root.mainloop()