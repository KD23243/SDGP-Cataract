from tkinter import *
from PIL import ImageTk, Image
import os

def goBack():
    found.destroy()
    os.system('python Predictor.py')

def destroy():
    found.destroy()

found = Tk()
found.geometry('724x516')
found.title(" Result Page")
found.resizable(False, False)
found.iconbitmap("imageData/icon.ico")

bg = ImageTk.PhotoImage(Image.open("imageData/found.png"))
label = Label(found, image=bg)
label.pack()

tryagain = ImageTk.PhotoImage(Image.open("imageData/tryagain.png"))
tryagain1 = Button(found, image = tryagain,command=goBack, borderwidth=0, bd=0,highlightthickness=0 ).place(x=423, y=295)

logout = ImageTk.PhotoImage(Image.open("imageData/logout.png"))
logoutbtn = Button(found, image = logout,command=destroy, borderwidth=0, bd=0,highlightthickness=0 ).place(x=423, y=366)

found.mainloop()

//asdasd