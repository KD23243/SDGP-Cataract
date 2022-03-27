from tkinter import *
from PIL import ImageTk, Image
import os

def gotocreateAccountWelcome():
    welcome.destroy()
    os.system('python Register.py')

def gotoLoginWelcome():
    welcome.destroy()
    os.system('python Login.py')

welcome = Tk()
welcome.geometry('724x516')
welcome.title(" Welcome Page")
welcome.resizable(False, False)
welcome.iconbitmap("imageData/icon.ico")

bg = ImageTk.PhotoImage(Image.open("imageData/welcome.png"))
label = Label(welcome, image=bg)
label.pack()


createAccountWelcome = ImageTk.PhotoImage(Image.open("imageData/createAccountWelcome.png"))
createAccountWelcomebtn = Button(welcome, image = createAccountWelcome,command=gotocreateAccountWelcome, borderwidth=0, bd=0,highlightthickness=0 ).place(x=375, y=358)

loginWelcome = ImageTk.PhotoImage(Image.open("imageData/loginWelcome.png"))
loginWelcomebtn = Button(welcome, image = loginWelcome,command=gotoLoginWelcome, borderwidth=0, bd=0,highlightthickness=0 ).place(x=375, y=417)


welcome.mainloop()