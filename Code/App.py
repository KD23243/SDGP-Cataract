from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import os
import cv2

def ml_Model(imagePath):
    cascPath = "model.xml"
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
        output.config(text="Normal",font=(25))
    else:
        output.config(text="Found Cataract",font=(25))

    output.pack()

    for (x, y, w, h) in catarat:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    status = cv2.imwrite('results/result.jpg', image)


def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.jpg'),('Image Files', '*.png')])
   if file:
      filepath = os.path.abspath(file.name)
      imagePath = filepath
      ml_Model(imagePath)

def open_camera():
    camera = cv2.VideoCapture(1)
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

root = Tk()
root.title(" Cataract Detector")
root.geometry("375x812")
root.resizable(False, False)
root.iconbitmap('imageData/icon.ico')


logoImg = ImageTk.PhotoImage(Image.open("imageData/mainLogo.png"))
label = Label(root, image=logoImg)
label.pack()

output = Label(root)

uploadButton = ImageTk.PhotoImage(Image.open("imageData/uploadButton.png"))
cameraButton = ImageTk.PhotoImage(Image.open("imageData/cameraButton.png"))

upload_Button1 = Button(root, text='Upload', image = uploadButton, borderwidth=0, command=open_file)
upload_Button1.place(x=10, y=650)


upload_Button2 = Button(root, text='Upload', image = cameraButton, borderwidth=0, command=open_camera)
upload_Button2.place(x=10, y=520)

root.mainloop()
#hello