from tkinter import *
from functools import partial
from PIL import ImageTk, Image
import os


def validateLogin(username, password):

    try:
        file = open("users/" + username.get() + ".txt", "r")
        data = file.readline()
        file.close()

        if username.get() + password.get() == data:
            print("Log: User Logged In")
            login.destroy()
            os.system('python Predictor.py')
        else:
            print("Log: Wrong Password")

        return

    except:
        print("Log: User Not Found")

def gotoregister():
    login.destroy()
    os.system('python Register.py')

login = Tk()
login.geometry('724x516')
login.title(" Login Page")
login.resizable(False, False)
login.iconbitmap("imageData/icon.ico")

bg = ImageTk.PhotoImage(Image.open("imageData/loginbg.png"))
label = Label(login, image=bg)
label.pack()

username = StringVar()
usernameEntry = Entry(login, textvariable=username, relief='flat',bg='#a1bce7').place(x=440, y=180, height=40, width=200)

password = StringVar()
passwordEntry = Entry(login, textvariable=password, relief='flat', show='*',bg='#a1bce7').place(x=440, y=245, height=40, width=200)

validateLogin = partial(validateLogin, username, password)

signinbtn = ImageTk.PhotoImage(Image.open("imageData/signinbutton.png"))
signinbtn1 = Button(login, image = signinbtn,command=validateLogin, borderwidth=0, bd=0,highlightthickness=0 ).place(x=433, y=318)

donthaveAccount = ImageTk.PhotoImage(Image.open("imageData/donthaveAccount.png"))
donthaveAccountbtn = Button(login, image = donthaveAccount,command=gotoregister, borderwidth=0, bd=0,highlightthickness=0 ).place(x=410, y=398)

login.mainloop()


