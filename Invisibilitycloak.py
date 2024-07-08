"""
Invisibility Cloak
1) Choose the background against which you want to perform the invisibility trick(This is essential because you will be replacing the green screen with the background and if the background keeps changing the replacement will not be seamless).
2) Choose the HSV/RGB range which you want to replace i.e. act as the cloak.
3) Replace the value of the pixels in the above range with the original background.
4) Voila! You have created your very own digital invisibility cloak.

"""

import cv2 
import numpy as np 

initial_frame = cv2.imread(r"C:\Users\91987\Downloads\Master.jpg")
initial_frame = cv2.resize(initial_frame, (640, 480))

hh = 60
hl = 42
sh = 226
sl = 57
vh = 255
vl = 10

# def hueh(val):
#     global hh
#     hh = val
# def huel(val):
#     global hl
#     hl = val
# def sath(val):
#     global sh
#     sh = val
# def satl(val):
#     global sl
#     sl = val
# def valh(val):
#     global vh
#     vh = val
# def vall(val):
#     global vl
#     vl = val

# cv2.namedWindow("TrackBar")

# cv2.createTrackbar("HueHigh","TrackBar",0,180,hueh)
# cv2.createTrackbar("HueLow","TrackBar",0,180,huel)
# cv2.createTrackbar("SatHigh","TrackBar",0,255,sath)
# cv2.createTrackbar("SatLow","TrackBar",0,255,satl)
# cv2.createTrackbar("ValHigh","TrackBar",0,255,valh)
# cv2.createTrackbar("ValLow","TrackBar",0,255,vall)

# while True:
#     ignore,frame = cam.read()

#     #converting the frame to HSV
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
#     # Bounds
#     lowerbound = np.array([hl,sl,vl])
#     upperbound = np.array([hh,sh,vh])

#     # print(lowerbound,upperbound)
#     mymask = cv2.inRange(hsv,lowerbound,upperbound)

#     # pasting mask over the frame
#     myselection = cv2.bitwise_and(frame,frame,mask=mymask)

#     cv2.imshow("Frame",frame)
#     # cv2.imshow("HSV",hsv)
#     # cv2.imshow("Selection",mymask)
#     cv2.imshow("Track",myselection)

#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break

# cam.release()

cam = cv2.VideoCapture(1)
lowerbound = np.array([hl,sl,vl])
upperbound = np.array([hh,sh,vh])

while True :
    ignore,frame = cam.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 
    mymask = cv2.inRange(hsv,lowerbound,upperbound)
    invisible = cv2.bitwise_and(initial_frame,initial_frame,mask=mymask)
    inversemask = cv2.bitwise_not(mymask)
    background = cv2.bitwise_and(frame,frame,mask=inversemask)
    final = cv2.bitwise_or(invisible, background)
    #cv2.imshow("In",invisible)
    #cv2.imshow("Back",background)
    cv2.imshow("Original", frame)
    cv2.imshow("Final",final)
    print(frame.shape)
    print(initial_frame.shape)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()










