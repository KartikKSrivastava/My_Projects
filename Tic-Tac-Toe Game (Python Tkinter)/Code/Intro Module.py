import tkinter
from tkinter import *
import os
root = tkinter.Tk()
root.title("Python Project")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

def myfun():
     os.system("python Timer.py")


img1 = PhotoImage(file="Logo.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Python Project: Tic-Tac-Toe",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command= myfun
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "To Start Game PRESS START\n  Project By:- \n \n Kartik Kumar Srivastava | Reg No: 11913804 | Roll No: 64 \n \n Tenzin Wangmo | Reg No: 11905121 | Roll No: 38",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

root.mainloop()
