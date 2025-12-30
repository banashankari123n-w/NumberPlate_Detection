import tkinter as ttk
from tkinter import *
import cv2
import os
from PIL import Image, ImageTk
##from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
import shutil
import os


class App:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)

        # Open the video source
        self.cap = cv2.VideoCapture(video_source)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 850)

        # Create a canvas that can fit the video source
        self.canvas = ttk.Canvas(window, width=1600,  # self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                                 height=850)  # self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.place(x=0, y=0)

        # Use PIL (Pillow) to convert the OpenCV image to a Tkinter image
        self.photo = None
        self.update()

        import warnings
        warnings.filterwarnings('ignore')
        window.geometry("1600x850")

        def live():
            os.system("python detect.py")

        def vid():
            global File

            # C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change
            # it according to the image location you have
            File = askopenfilename(initialdir='sample', title='Select image for analysis ',
                                   filetypes=[('image files', '*.*')])
            print(File)
            from det_vid import Start1
            Start1(File)

        def img():
            global File

            # C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change it according to the image location you have  
            File = askopenfilename(initialdir='sample', title='Select image for analysis ',
                                   filetypes=[('image files', '*.*')])

            dst = "testpicture"
            print(File)
            print(os.path.split(File)[-1])
            if os.path.split(File)[-1].split('.') == 'h (1)':
                print('dfdffffffffffffff')
            shutil.copy(File, dst)
            load1 = Image.open(File)
            im1 = load1.resize((500, 500), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(im1)
            img = Label(image=render, height="500", width="500")
            img.image = render
            img.place(x=250, y=220)
            from det_img import Start
            Start(File)
            ##            cv2.imshow("result","output\\result.jpg")
            ##            img = cv2.imread("output\\result.jpg", cv2.IMREAD_ANYCOLOR)
            load11 = Image.open("output\\result.jpg")
            im11 = load11.resize((500, 500), Image.ANTIALIAS)
            render1 = ImageTk.PhotoImage(im11)
            img1 = Label(image=render1, height="500", width="500")
            img1.image = render1
            img1.place(x=850, y=220)

        def exitwin():
            window.destroy()

        # label = Label(window, text="Choose The Image to Detect the Violations", fg="white", bg="black",
        #               font=("elephant", 25, "bold underline"))
        label = Label(window, text="NUMBER PLATE DETECTION AND VALIDATION", fg="white", bg="black",
                                    font=("elephant", 25, "bold"))
        label.place(x=300, y=50)

        # label=Button(window,text="LIVE",fg="white",bg="black",font=("elephant",16,"bold underline"),command=live)
        # label.place(x=300,y=150)

        # label=Button(window,text="VIDEO",fg="white",bg="black",font=("elephant",16,"bold underline"),command=vid)
        # label.place(x=550,y=150)

        label = Button(window, text="UPLOAD", fg="white", bg="black", font=("elephant", 16, "bold"),
                       command=img)
        label.place(x=550, y=150)
        label = Button(window, text="EXIT", fg="white", bg="black", font=("elephant", 16, "bold"),
                       command=exitwin)
        label.place(x=950, y=150)

        window.mainloop()

        # Start the video playback loop
        self.window.mainloop()

    def update(self):
        # Get a frame from the video source
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, (1600, 850),
                           interpolation=cv2.INTER_LINEAR)
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=ttk.NW)

        # Repeat after 15 milliseconds
        self.window.after(15, self.update)


# Create a window and pass it to the Application object
App(ttk.Tk(), "Display", "vid.mp4")
