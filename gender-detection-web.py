import cvlib as cv
import cv2
import numpy as np
import sys


webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open video file")
    exit()
    

while webcam.isOpened():

    status, frame = webcam.read()

    if not status:
        print("Could not read frame")
        exit()

    face, confidence = cv.detect_face(frame)

    print(face)
    print(confidence)

    for idx, f in enumerate(face):
        
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)

        face_crop = np.copy(frame[startY:endY, startX:endX])

        (label, confidence) = cv.detect_gender(face_crop)

        print(confidence)
        print(label)

        idx = np.argmax(confidence)
        label = label[idx]

        label = "{}: {:.2f}%".format(label, confidence[idx] * 100)

        Y = startY - 10 if startY - 10 > 10 else startY + 10

        cv2.putText(frame, label, (startX,Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0,255,0), 2)

    cv2.imshow("Real-time gender detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
webcam.release()
cv2.destroyAllWindows()      