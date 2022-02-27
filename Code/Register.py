from tkinter import *
from PIL import ImageTk, Image
import os

def createAccount():

    if name.get() == "":
        print("Log: No username")
    else:
        file = open("users/" + name.get() + ".txt", "w")
        file.write(name.get() + password.get())
        file.close()
        register.destroy()
        os.system('python Login.py')
        return

def gotosignin():
    register.destroy()
    os.system('python Login.py')

register = Tk()
register.geometry('724x516')
register.title(" Register Page")
register.resizable(False, False)
register.iconbitmap("imageData/icon.ico")

bg = ImageTk.PhotoImage(Image.open("imageData/register.png"))
label = Label(register, image=bg)
label.pack()

name = StringVar()
nameEntry = Entry(register, textvariable=name, relief='flat',bg='#a1bce7').place(x=437, y=142, height=40, width=200)

email = StringVar()
emailEntry = Entry(register, textvariable=email, relief='flat',bg='#a1bce7').place(x=437, y=203, height=40, width=200)

password = StringVar()
passwordEntry = Entry(register, textvariable=password, relief='flat', show='*',bg='#a1bce7').place(x=437, y=263, height=40, width=200)


signup = ImageTk.PhotoImage(Image.open("imageData/signup.png"))
signupbtn = Button(register, image = signup,command=createAccount, borderwidth=0, bd=0,highlightthickness=0 ).place(x=425, y=328)

haveAccount = ImageTk.PhotoImage(Image.open("imageData/haveAccount.png"))
haveAccountbtn = Button(register, image = haveAccount,command=gotosignin, borderwidth=0, bd=0,highlightthickness=0 ).place(x=402, y=404)


register.mainloop()


