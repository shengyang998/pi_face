print("Importing OpenCV")
import cv2
print("OpenCV Imported")
import numpy as np
import myfunctions as myf

print("Opening Video Capture")
cap = cv2.VideoCapture(-1)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
cap.set(cv2.CAP_PROP_FPS, 0.1)
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1) # Flip camera vertically

    #cv2.imshow('frame', frame)

    rgb_frame = frame[:, :, ::-1]
    face_locations = myf.face_r.face_locations(rgb_frame)
    face = myf.face_r.face_encodings(rgb_frame, face_locations)
    myf.is_face_in_white_list(face)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

print("Releasing Video Capture")
cap.release()
print("Video Capture Released")
cv2.destroyAllWindows()

