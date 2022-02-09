from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import os
import cv2

print("Log: Programme Initialized")
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
        os.system('python FoundCataract.py')
        print("Log: Cataract Stage Predicted - Healthy")
    else:
        print("Log: Cataract Stage Predicted - Cataract")


    for (x, y, w, h) in catarat:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    status = cv2.imwrite('results/result.jpg', image)


def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.jpg'),('Image Files', '*.png')])
   print("Log: Image Uploaded")
   if file:
      filepath = os.path.abspath(file.name)
      imagePath = filepath
      ml_Model(imagePath)

def open_camera():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    print("Log: Launched Camera")
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
    print("Log: Image Captured")
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

camera_Button1 = Button(predictor, text='Camera', image = cameraButton, borderwidth=0, bd=0,highlightthickness=0, command = open_camera )
camera_Button1.place(x=399, y=284)

upload_Button1 = Button(predictor, text='Upload', image = uploadButton, borderwidth=0, bd=0,highlightthickness=0, command = open_file )
upload_Button1.place(x=399, y=347)

predictor.mainloop()