#ImportingLibrary
import cv2
import numpy as np
import time
import Pose as pm
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import mediapipe as mp

#tkinter GUI
tkWindow = Tk()
tkWindow.geometry('700x750')
tkWindow.title('Exercise DashBoard')
tkWindow.config(bg= "black")

#Exercise Definition
#Counting by incrementation
def Type_of_Exercise():
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(1)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)
    detector = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        if len(lmList) != 0:
            #Based on conditions we set angle and distance for each exercise
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (220, 280), (0, 100))
            bar = np.interp(angle, (220, 280), (650, 100))
            # Check for Count(will differ for each exercise)
            color = (0, 255, 0)
            if per == 100:
                color = (0, 0, 255)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 0, 255)
                if dir == 1:
                    count += 0.5
                    dir = 0
            print(count)

            # Draw Accuracy Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)}%',(1100,75),cv2.FONT_HERSHEY_SIMPLEX,2,
                                 color, 3)
            # Draw Exercise Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX,4
                                                         (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        #Exit control
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.destroyAllWindows()

#GUI for Timer
#Exercise Definition
#Counting by Timer
win = Toplevel()
win.geometry("1920x1080+200+30")
win.title("Color Detection")
win.resizable(True, True)
w = 1280
h = 720
color = "Black"
frame_1 = Frame(win, width=1920, height=1080, bg=color).place(x=0, y=0)

#Timer Class
class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()
    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50),
                                       fg="yellow", bg="black")
        self.SetTime(self.nextTime)
        timeText.pack(fill=BOTH, expand=YES, pady=2, padx=2, side=LEFT)
    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)
    def SetTime(self, nextE):
        minutes = int(nextE / 60)
        seconds = int(nextE - minutes * 60.0)
        miliseconds = int((nextE - minutes * 60.0 - seconds) * 60)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliseconds))
    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1
    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
    def Exit(self):
        win.destroy()
        exit()
    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)
stopWatch = StopWatch(win)
stopWatch.place(x=650, y=0)

cap = cv2.VideoCapture(0)
label1 = Label(win, width=w, height=h)
label1.place(x=150, y=100)

#Video interface to GUI
def select_img():
    # Left Leg
    detector = pm.poseDetector()
    dir = 0
    pTime = 0
    per = 0
    bar = 0
    _, img = cap.read()
    img = cv2.resize(img, (w, h))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        #Based on the condition we set angle and distance
        # Left Leg
        angle = detector.findAngle(img, 24, 25, 27)
        per = np.interp(angle, (215, 250), (0, 100))
        bar = np.interp(angle, (215, 250), (650, 100))
        # Timer Control action
        color = (0, 255, 0)

        if per == 100:
            color = (0, 0, 255)
            if (dir == 0):
                stopWatch.Start()
                dir = 1
        if per == 0:
            color = (0, 0, 255)
            if (dir == 1):
                stopWatch.Stop()
                dir = 0

        # Draw Accuracy Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX,
                                    2,color, 3)

    image = Image.fromarray(img)
    iago = ImageTk.PhotoImage(image)
    label1.configure(image=iago)
    label1.image = iago
    win.after(15, select_img)
select_img()
win.mainloop()
if __name__ == '__main__':
    select_img()

#Packing Buttons to the GUI
button1 = tkinter.Button(tkWindow, text='Exercise Type’, bg='pink',
                                        command=Type_of_Exercise, width=20, height=2)
button1.pack(side=TOP)
#Same line of codes for all the exercise to interface with GUI


def main():
    cap = cv2.VideoCapture("File Path")
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
if __name__ == "__main__":
    main()
