#Ankit Kumar Biswal
# This code is for the Tracking of the object
# first we have imported the cv2

import cv2

# now we need a webcam to track the object
# for that we  need to write the required code to capture the frames

cap=cv2.VideoCapture(0)     #this tells it captures the external or internal camera

while True:
    timer=cv2.getTickCount()
    success, img =cap.read()   # this is going to read the frame

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)  # we get the frames per second
    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("Tracking",img)  # this is going to show the frame

    if cv2.waitKey(1) & 0xff == ord('q'): # when we click the 'Q' key it quits the video capture
        break

