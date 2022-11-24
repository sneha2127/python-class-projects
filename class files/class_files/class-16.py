# Option menu concept:
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.geometry("500x500")

# option = StringVar()
# option.set("Select Gender")
# options = ["Male","Female"]

# # option menu widget
# optionMenu = OptionMenu(root,option,*options)
# optionMenu.pack(pady=10)

# def getValue():
#     value = option.get()
#     print(value)


# button = Button(root,text="Gender Value",command=getValue)
# button.pack(pady=10)



# file_open


# def open_file():
#     filepath = filedialog.askopenfilename(title="Open Your File")
#     if os.path.exists(filepath):
#         f = open(filepath,'r')
#         content = f.read()
#         print(content)
#         f.close()
#     else:
#         print("Please select correct file!")

# opn_button = Button(root,text="Open File",command=open_file)
# opn_button.pack(pady=10)



# File Save: 
# def save_file():
#     content = textArea.get(1.0,END)
#     filepath = filedialog.asksaveasfilename(title="Save your file", defaultextension=".txt", filetypes=[("Text Files",".txt"), ("HTML Files",".html"), ("All Files",".*")])
#     if os.path.exists(filepath):
#         f = open(filepath,'w')
#         f.write(content)
#         f.close()
#         messagebox.showinfo("Confirmation","Your file has been saved successfully")
#     else:
#         messagebox.showerror("Error","Please save with correct file name")


# textArea = Text(root)
# textArea.pack(pady=10)


# sv_button = Button(root,text="Save File",command=save_file)
# sv_button.pack(pady=10)


# scale creation

# scale = Scale(root,from_=0,to=100)
# scale.pack(pady=10)


# scale_h = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
# scale_h.pack(pady=10)

root.mainloop()
