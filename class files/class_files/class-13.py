from tkinter import *
import pyttsx3
from tkinter import messagebox
import random


speaker = pyttsx3.init()

root = Tk()
root.geometry("600x600")
root.title("Text to Speech Converter")


txt_lbl = Label(root, text = "Enter your text below")
txt_lbl.pack(pady=10)


text = Text(root)
text.pack(pady=10)


def listenVoice():
    content = text.get(1.0,END)
    speaker.say(content)
    speaker.runAndWait()


say_btn = Button(root,text="Listen the Voice",command=listenVoice)
say_btn.pack(pady=10)


def downloadVoice():
    content = text.get(1.0,END)
    characters = "ABCRTY980123"
    random_id = ""
    for i in range(5):
        r_ch = random.choice(characters)
        random_id += r_ch
    file_name = f"voice-{random_id}.mp3"
    speaker.save_to_file(content,file_name)
    speaker.runAndWait()
    messagebox.showinfo("Confirmation","Your file has been downloaded!")



download_btn = Button(root,text="Download the Voice",command=downloadVoice)
download_btn.pack(pady=10)







root.mainloop()