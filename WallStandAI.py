import cv2
import numpy as np
from tkinter import*
from PIL import Image, ImageTk
import PoseModule as pm
import time

win = Toplevel()
win.geometry("1920x1080+200+30")
win.title("Color Detection")
win.resizable(True, True)
w = 1280
h = 720
color = "Black"
frame_1 = Frame(win, width=1920, height=1080, bg=color).place(x=0, y=0)

# logical part
class StopWatch(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="yellow", bg="black")
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
#cap = cv2.VideoCapture("C:/Users/DELL/OneDrive/Desktop/WallStand.mp4")
cap = cv2.VideoCapture(1)
label1 = Label(win, width=w, height=h)
label1.place(x=150, y=100)





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
        # Right Leg
        #angle = detector.findAngle(img, 23, 26, 28)
        # Left Leg
        angle = detector.findAngle(img, 24, 25, 27)
        per = np.interp(angle, (215, 250), (0, 100))
        bar = np.interp(angle, (215, 250), (650, 100))
        # print(angle, per)

        # Check for the Count

        color = (0, 255, 0)

        if per == 100:
            color = (0, 0, 255)
            if (dir == 0):
                stopWatch.Start()
                dir = 1
        if per == 0:
            color = (0, 0, 255)
            stopWatch.Stop()




        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                    color, 3)

    image = Image.fromarray(img)
    iago = ImageTk.PhotoImage(image)
    label1.configure(image=iago)
    label1.image = iago

    win.after(10, select_img)


select_img()
win.mainloop()

if __name__ == '__main__':
    select_img()