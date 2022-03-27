from functools import partial
import tkinter.messagebox
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import os
import cv2
from cryptography.fernet import Fernet


with open('encryption/key.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)


def notfoundCataractFile():
    def goBack():
        found.destroy()
        predictorFile()

    def destroy():
        found.destroy()

    found = Tk()
    found.geometry('724x516')
    found.title(" Result Page")
    found.resizable(False, False)
    found.iconbitmap("imageData/icon.ico")

    bg = ImageTk.PhotoImage(Image.open("imageData/notfound.png"))
    label = Label(found, image=bg)
    label.pack()

    tryagain = ImageTk.PhotoImage(Image.open("imageData/tryagain.png"))
    tryagain1 = Button(found, image=tryagain, command=goBack, borderwidth=0, bd=0, highlightthickness=0).place(x=423,
                                                                                                               y=295)

    logout = ImageTk.PhotoImage(Image.open("imageData/logout.png"))
    logoutbtn = Button(found, image=logout, command=destroy, borderwidth=0, bd=0, highlightthickness=0).place(x=423,
                                                                                                              y=366)
    found.mainloop()


def foundCataractFile():
    def goBack():
        found.destroy()
        predictorFile()

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
    tryagain1 = Button(found, image=tryagain, command=goBack, borderwidth=0, bd=0, highlightthickness=0).place(x=423,
                                                                                                               y=295)

    logout = ImageTk.PhotoImage(Image.open("imageData/logout.png"))
    logoutbtn = Button(found, image=logout, command=destroy, borderwidth=0, bd=0, highlightthickness=0).place(x=423,
                                                                                                              y=366)

    found.mainloop()

def predictorFile():
    def ml_Model(imagePath):
        cascPath = "model/model.xml"
        pedsCascade = cv2.CascadeClassifier(cascPath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        catarat = pedsCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=2,
            minSize=(50, 50)
        )

        prediction = format(len(catarat))
        if prediction == "0":
            predictor.destroy()
            foundCataractFile()
        else:
            predictor.destroy()
            notfoundCataractFile()

        for (x, y, w, h) in catarat:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        status = cv2.imwrite('results/result.jpg', image)

    def open_file():
        file = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.jpg'), ('Image Files', '*.png')])
        if file:
            filepath = os.path.abspath(file.name)
            imagePath = filepath
            ml_Model(imagePath)

    def open_camera():
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            return_value, image = camera.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            if cv2.waitKey(1) & 0xFF == ord(' '):
                image = cv2.imwrite('results/cameraCapture.jpg', image)
                break

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image,
                        'Press "Spacebar" Key To Capture',
                        (50, 50),
                        font, 1,
                        (255, 255, 255),
                        2,
                        cv2.LINE_4)

            cv2.imshow('Cataract Detector', image)

        camera.release()
        cv2.destroyAllWindows()
        imagePath = os.path.abspath("results/cameraCapture.jpg")
        ml_Model(imagePath)

    predictor = Tk()
    predictor.geometry('724x516')
    predictor.title(" Prediction Page")
    predictor.resizable(False, False)
    predictor.iconbitmap("imageData/icon.ico")

    bg = ImageTk.PhotoImage(Image.open("imageData/predictionbg.png"))
    label = Label(predictor, image=bg)
    label.pack()

    cameraButton = ImageTk.PhotoImage(Image.open("imageData/camera.png"))
    uploadButton = ImageTk.PhotoImage(Image.open("imageData/gallery.png"))

    camera_Button1 = Button(predictor, text='Camera', image=cameraButton, borderwidth=0, bd=0, highlightthickness=0,
                            command=open_camera)
    camera_Button1.place(x=399, y=284)

    upload_Button1 = Button(predictor, text='Upload', image=uploadButton, borderwidth=0, bd=0, highlightthickness=0,
                            command=open_file)
    upload_Button1.place(x=399, y=347)

    predictor.mainloop()


def registerFile():
    def createAccount():

        if name.get() == "":
            tkinter.messagebox.showinfo("Username Error", "The Username provided must not be empty.")
        elif password.get() == "" or len(password.get()) < 8 or (not any(str.isdigit(c) for c in password.get())):
            tkinter.messagebox.showinfo("Password Error",
            "The password provided must contains 8 characters minimum.\n\nThe password provided must contain at least one number.")
        elif email.get() == "" or "@" not in email.get() or "." not in email.get():
            tkinter.messagebox.showinfo("Email Error", "The Email provided must be a valid email address.")
        else:
            file = open("users/" + name.get() + ".xml", "wb")
            message = name.get() + password.get()
            encMessage = fernet.encrypt(message.encode())
            file.write(encMessage)
            file.close()
            register.destroy()
            loginFile()

    def gotosignin():
        register.destroy()
        loginFile()

    register = Tk()
    register.geometry('724x516')
    register.title(" Register Page")
    register.resizable(False, False)
    register.iconbitmap("imageData/icon.ico")

    bg = ImageTk.PhotoImage(Image.open("imageData/register.png"))
    label = Label(register, image=bg)
    label.pack()

    name = StringVar()
    nameEntry = Entry(register, textvariable=name, relief='flat', bg='#a1bce7').place(x=437, y=142, height=40,width=200)
    email = StringVar()
    emailEntry = Entry(register, textvariable=email, relief='flat', bg='#a1bce7').place(x=437, y=203, height=40,width=200)
    password = StringVar()
    passwordEntry = Entry(register, textvariable=password, relief='flat', show='*', bg='#a1bce7').place(x=437, y=263,height=40,width=200)
    signup = ImageTk.PhotoImage(Image.open("imageData/signup.png"))
    signupbtn = Button(register, image=signup, command=createAccount, borderwidth=0, bd=0, highlightthickness=0).place(x=425, y=328)
    haveAccount = ImageTk.PhotoImage(Image.open("imageData/haveAccount.png"))
    haveAccountbtn = Button(register, image=haveAccount, command=gotosignin, borderwidth=0, bd=0,highlightthickness=0).place(x=402, y=404)
    register.mainloop()

def loginFile():
    def validateLogin(username, password):

        try:
            file = open("users/" + username.get() + ".xml", "rb")
            data = file.readline()
            file.close()
            decMessage = fernet.decrypt(data).decode()
            if username.get() + password.get() == decMessage:
                login.destroy()
                predictorFile()
            else:
                tkinter.messagebox.showinfo("Wrong Password", "Please enter the correct password")
            return
        except:
            tkinter.messagebox.showinfo("User Not Found", "Please enter the correct username")

    def gotoregister():
        login.destroy()
        registerFile()

    login = Tk()
    login.geometry('724x516')
    login.title(" Login Page")
    login.resizable(False, False)
    login.iconbitmap("imageData/icon.ico")

    bg = ImageTk.PhotoImage(Image.open("imageData/loginbg.png"))
    label = Label(login, image=bg)
    label.pack()

    username = StringVar()
    usernameEntry = Entry(login, textvariable=username, relief='flat', bg='#a1bce7').place(x=440, y=180, height=40,width=200)
    password = StringVar()
    passwordEntry = Entry(login, textvariable=password, relief='flat', show='*', bg='#a1bce7').place(x=440, y=245,height=40,width=200)
    validateLogin = partial(validateLogin, username, password)
    signinbtn = ImageTk.PhotoImage(Image.open("imageData/signinbutton.png"))
    signinbtn1 = Button(login, image=signinbtn, command=validateLogin, borderwidth=0, bd=0, highlightthickness=0).place(x=433, y=318)
    donthaveAccount = ImageTk.PhotoImage(Image.open("imageData/donthaveAccount.png"))
    donthaveAccountbtn = Button(login, image=donthaveAccount, command=gotoregister, borderwidth=0, bd=0,highlightthickness=0).place(x=410, y=398)

    login.mainloop()


def gotocreateAccountWelcome():
    welcome.destroy()
    registerFile()

def gotoLoginWelcome():
    welcome.destroy()
    loginFile()

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