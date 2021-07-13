import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2


webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    

while webcam.isOpened():

    status, frame = webcam.read()

    if not status:
        print("Could not read frame")
        exit()

    bbox, label, conf = cv.detect_common_objects(frame)

    print(bbox, label, conf)

    out = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Real-time object detection", out)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
q# release resources
webcam.release()
cv2.destroyAllWindows()        