import cv2
import numpy as np
import time
import PoseModule as pm
import tkinter
from tkinter import *

tkWindow = Tk()
tkWindow.geometry('700x750')
tkWindow.title('Exercise DashBoard')
tkWindow.config(bg="black")

def Curl():
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
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
            # Right Arm
            # angle = detector.findAngle(img, 12, 14, 16)
            # Left Arm
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (220, 280), (0, 100))
            bar = np.interp(angle, (220, 280), (650, 100))
            # Check for count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Curl Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
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

def Squat():
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
            # Left Leg
            angle = detector.findAngle(img, 23, 25, 29)
            per = np.interp(angle, (100, 160), (100, 0))
            bar = np.interp(angle, (100, 160), (100, 650))
            # Check for the count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def LeftSideLegRise():
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
            # Left Leg
            angle = detector.findAngle(img, 24, 23, 29)
            per = np.interp(angle, (220, 245), (100, 0))
            bar = np.interp(angle, (220, 245), (100, 650))
            # Check for count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def RightSideLegRise():
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
            # Right Leg
            angle = detector.findAngle(img, 23, 24, 30)
            per = np.interp(angle, (105, 130), (0, 100))
            bar = np.interp(angle, (105, 130), (650, 100))
            # Check for count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Curl Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def SideLounges():
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
            # Both legs
            angle = detector.findAngle(img, 32, 0, 31)
            per = np.interp(angle, (310, 345), (100, 0))
            bar = np.interp(angle, (310, 345), (100, 650))
            # Check for count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def LFireHydrants():
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
            # Left Leg
            angle = detector.findAngle(img, 23, 25, 27)
            per = np.interp(angle, (90, 125), (0, 100))
            bar = np.interp(angle, (90, 125), (650, 100))
            # Check for count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def RFireHydrants():
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
            # Right Leg
            angle = detector.findAngle(img, 24, 26, 28)
            per = np.interp(angle, (220, 275), (100, 0))
            bar = np.interp(angle, (220, 275), (100, 650))
            # Check for count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def Stepup():
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
        # img = cv2.imread("AiTrainer/test.jpg")
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
            # Leg distance
            dis = detector.finddistance(img, 29, 30)
            per = np.interp(dis, (30, 120), (0, 100))
            bar = np.interp(dis, (30, 120), (650, 100))
            print(dis, per)
            # Check for Count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def YogicSquat():
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
            # Left Leg
            angle = detector.findAngle(img, 28, 26, 23)
            per = np.interp(angle, (220, 270), (0, 100))
            bar = np.interp(angle, (220, 270), (650, 100))
            # Right Side
            dist0 = detector.finddistance(img, 8, 13)
            # Left Side
            dist1 = detector.finddistance(img, 7, 14)
            # Check for count
            color = (0, 255, 0)
            if per == 100:
                color = (0, 0, 255)
                if ((dir == 0 and dist0 <= 165 and dist1 <= 165)):
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 0, 255)
                if ((dir == 1 and dist0 <= 165 and dist1 <= 165)):
                    count += 0.5
                    dir = 0
            print(count)
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def JackKnives():
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
            #Angle
            angle = detector.findAngle(img, 17, 23, 31)
            per = np.interp(angle, (180, 345), (0, 100))
            bar = np.interp(angle, (180, 345), (650, 100))
            # Check for count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def KneeCrunches():
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
            # Left Leg
            angle = detector.findAngle(img, 11, 23, 25)
            per = np.interp(angle, (285, 315), (0, 100))
            bar = np.interp(angle, (285, 315), (650, 100))
            # Check for count
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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def PushUps():
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
            # Body Pose
            angle = detector.findAngle(img, 16, 12, 30)
            angle1 = detector.findAngle(img, 12, 14, 16)
            angle2 = detector.findAngle(img, 12, 24, 30)
            per = np.interp(angle, (60, 70), (100, 0))
            bar = np.interp(angle, (60, 70), (100, 650))
            # Check for count
            color = (0, 255, 0)
            if ((per == 100 and angle1 < 165 and angle2>165)):
                color = (0, 0, 255)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if ((per == 0 and angle1 > 60 and angle2>165)):
                color = (0, 0, 255)
                if dir == 1:
                    count += 0.5
                    dir = 0
                    print(count)
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Curl Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def BasicPushUps():
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
            # Body Pose
            angle = detector.findAngle(img, 16, 12, 24)
            angle1 = detector.findAngle(img, 12, 14, 16)
            per = np.interp(angle, (90, 95), (0, 100))
            bar = np.interp(angle, (90, 95), (650, 100))
            # Check for count
            color = (0, 255, 0)
            if ((per == 100 and angle1 < 165)):
                color = (0, 0, 255)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if ((per == 0 and angle1 > 60)):
                color = (0, 0, 255)
                if dir == 1:
                    count += 0.5
                    dir = 0
            print(count)
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 2)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        color, 3)
            # Draw Count
            cv2.rectangle(img, (10, 550), (200, 720), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_TRIPLEX, 4,
                        (255, 255, 255), 10)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def FullPlank():
    import FullPlank as fp
    fp.select_img()

def ElbowPlank():
    import ElbowPlank as eb
    eb.select_img()

def WallStand():
    import WallStandAI as ws
    ws.select_img()

def Exit():
    tkWindow.destroy()
    exit()
button1 = tkinter.Button(tkWindow, text='Curl', bg='pink', command=Curl, width=20, height=2)
button1.pack(side=TOP)
button2 = tkinter.Button(tkWindow, text='Squat', bg='pink', command=Squat,width=20, height=2)
button2.pack(side=TOP)
button3 = tkinter.Button(tkWindow, text='Left Side LegRise', bg='pink', command=LeftSideLegRise,width=20, height=2)
button3.pack(side=TOP)
button4 = tkinter.Button(tkWindow, text='SideLounges', bg='pink', command=SideLounges,width=20, height=2)
button4.pack(side=TOP)
button5 = tkinter.Button(tkWindow, text='Wallstand', bg='pink', command=WallStand,width=20, height=2)
button5.pack(side=TOP)
button6 = tkinter.Button(tkWindow, text='Left Side Fire Hydrants', bg='pink', command=LFireHydrants,width=20, height=2)
button6.pack(side=TOP)
button7 = tkinter.Button(tkWindow, text='Right Side Fire Hydrants', bg='pink', command=RFireHydrants,width=20, height=2)
button7.pack(side=TOP)
button8 = tkinter.Button(tkWindow, text='Step Up', bg='pink', command=Stepup,width=20, height=2)
button8.pack(side=TOP)
button9 = tkinter.Button(tkWindow, text='Yogic Squat', bg='pink', command=YogicSquat,width=20, height=2)
button9.pack(side=TOP)
button10 = tkinter.Button(tkWindow, text='Jack Knives', bg='pink', command=JackKnives,width=20, height=2)
button10.pack(side=TOP)
button11 = tkinter.Button(tkWindow, text='Knee Crunches', bg='pink', command=KneeCrunches,width=20, height=2)
button11.pack(side=TOP)
button12 = tkinter.Button(tkWindow, text='Push-Ups', bg='pink', command=PushUps,width=20, height=2)
button12.pack(side=TOP)
button13 = tkinter.Button(tkWindow, text='Basic Push-Up', bg='pink', command=BasicPushUps,width=20, height=2)
button13.pack(side=TOP)
button14 = tkinter.Button(tkWindow, text='Right Side LegRise', bg='pink', command=RightSideLegRise,width=20, height=2)
button14.pack(side=TOP)
button15 = tkinter.Button(tkWindow, text='Full Plank', bg='pink', command=FullPlank,width=20, height=2)
button15.pack(side=TOP)
button16 = tkinter.Button(tkWindow, text='Elbow Plank', bg='pink', command=ElbowPlank,width=20, height=2)
button16.pack(side=TOP)
button17 = tkinter.Button(tkWindow, text='Exit', bg='pink', command=Exit,width=20, height=2)
button17.pack(side=RIGHT)
tkWindow.mainloop()

