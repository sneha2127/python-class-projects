
# Todo Application using Tkinter

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Todo App")


def showTask():
    f = open('todo_task.txt','r')
    tasks = f.readlines()
    f.close()
    for i in range(len(tasks)):
        task_box.insert(i+1,f"{i+1}. {tasks[i][:-1]}")


# Add Task

txt_lbl = Label(window,text = "Add New Task")
txt_lbl.pack(pady=10)


# Entry Field
task_ent = Entry(window)
task_ent.pack(pady=10)


def addTask():
    task = task_ent.get()
    f = open('todo_task.txt','a')
    f.write(f"{task}\n")
    f.close()
    messagebox.showinfo("Confirmation", "Your task has been added!")
    task_ent.delete(0,END)
    task_box.delete(0,END)
    showTask()


# Button 
add_btn = Button(window,text="Add Task", command=addTask)
add_btn.pack(pady=10)

# Showing the task

# 1. Task
# 2. Task

task_box = Listbox(window)

showTask()

task_box.pack()



# Delete Task

dlt_txt_lbl = Label(window,text="Enter the number of the task you wanna delete")
dlt_txt_lbl.pack(pady=10)


dlt_ent = Entry(window)
dlt_ent.pack(pady=10)

def deleteTask():
    f = open('todo_task.txt','r')
    tasks = f.readlines()
    f.close()

    dlt_num = dlt_ent.get()
    remove_task = tasks.pop(int(dlt_num)-1)

    f = open('todo_task.txt','w')
    for task in tasks:
        f.write(task)
    f.close()
    messagebox.showinfo("Confirmation", f"{remove_task} has been deleted!")
    dlt_ent.delete(0,END)
    task_box.delete(0,END)
    showTask()


dlt_btn = Button(window,text="Delete Task",command=deleteTask)
dlt_btn.pack(pady=10)




window.mainloop()