# Notepad

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Global Variable Creation
file_name = "Untitled"
open_file_path = ""


root = Tk()
root.geometry("600x600")
root.title(f"{file_name} - NotePad")
# root.iconbitmap("icon.ico")


# Function Creation
def newfile():
    global file_name
    file_name="untitled"
    global open_file_path
    open_file_path=""
    root.title(f"{file_name} - Notepad")
    text.delete(1.0,END)
    messagebox.showinfo("Confirmation","New file has been created!")



def openfile():
    filepath = filedialog.askopenfilename()
    global open_file_path
    open_file_path = filepath
    global file_name
    paths = filepath.split('/')
    file_name = paths[-1]
    root.title(f"{file_name}-Notepad")
    f = open(filepath,'r')
    content = f.read()
    f.close()
    text.delete(1.0,END)
    text.insert(END,content)


def saveFile():
    if open_file_path:
        content = text.get(1.0,END)
        with open(open_file_path,"w") as f:
            f.write(content)
        messagebox.showinfo("Confirmation","Your file has been saved!")
    else:
        save_as()


def save_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files",".txt"), ("All Files",".*")], title = "Save file")
    global open_file_path
    open_file_path = file_path

    content = text.get(1.0,END)
    with open(file_path,"w") as f:
        f.write(content)

    global file_name
    paths = file_path.split('/')
    file_name = paths[-1]

    root.title(f"{file_name}-Notepad")
    messagebox.showinfo("Confirmation","You file has been saved!")



# Cut Copy Paste
def cut_item():
    text.event_generate("<<Cut>>")
def copy_item():
    text.event_generate("<<Copy>>")
def paste_item():
    text.event_generate("<<Paste>>")
def delete_item():
    text.event_generate("<<Cut>>")


# Text Area
text = Text(root, undo=True)
text.pack()

#Adding the binding
# text.bind("<Control-Key-a>", select_all)


# Menu section

menubar = Menu(root)
root.config(menu=menubar) 

# File menu creation
file_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New File    Ctrl+N",command=newfile)
file_menu.add_separator()
file_menu.add_command(label="Open File    Ctrl+O",command=openfile)
file_menu.add_separator()
file_menu.add_command(label="Save File    Ctrl+S", command=saveFile)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.quit)


# Edit Menu Creation
edit_menu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="Cut", command = cut_item)
edit_menu.add_command(label="Copy", command = copy_item )
edit_menu.add_command(label="Paste", command= paste_item)
edit_menu.add_command(label="Delete",command= delete_item)

edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)
edit_menu.add_separator()

# edit_menu.add_command(label="Find All",command= find_all)
# edit_menu.add_command(label="Find Next",command= find_next)
# edit_menu.add_command(label="Replace",command= replace)
# edit_menu.add_command(label="Goto",command= go_to)
# 


root.mainloop()