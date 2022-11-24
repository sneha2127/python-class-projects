# Text To Speech Converter

# pip install pyttsx3

# import pyttsx3

# engine = pyttsx3.init()


# Set Property to female
# voice_list = engine.getProperty("voices")
# engine.setProperty('voice',voice_list[1].id)

# say(text): We can listen the voice of the text
# engine.say("Hello, world!")


# Download the mp3 file
# engine.save_to_file("Hello, world!", "demo.mp3")
# print("Done")

# engine.runAndWait()




# ----------------------------------------------

# Tkinter
from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Learning")

# Icon Change
root.iconbitmap("icon.ico")

# Text Widget
# text_area = Text(root)
# text_area.pack(pady=10)

# def getTextValue():
#     content = text_area.get(1.0,END)
#     print(content)


# btn = Button(root, text = "The Value", command=getTextValue)
# btn.pack()



# Exit Button

# btn_exit = Button(root,text = "Exit", command = root.quit)
# btn_exit.pack()


# Option menu
# option = StringVar()
# option.set("Select Gender")
# options = ["Male","Female","Other"]

# # option menu widget
# option_menu = OptionMenu(root,option,*options)
# option_menu.pack(pady=10)

# def getOptionValue():
#     option_value = option.get()
#     print(option_value)

# Button
# btn = Button(root,text = "Get Option Value", command = getOptionValue)
# btn.pack()



root.mainloop()