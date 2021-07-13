import cvlib as cv
import sys
import cv2
import os 


image = cv2.imread('arjun.jpg')

faces, confidences = cv.detect_face(image)

print(faces)
print(confidences)

for face,conf in zip(faces,confidences):

    (startX,startY) = face[0],face[1]
    (endX,endY) = face[2],face[3]

    cv2.rectangle(image, (startX,startY), (endX,endY), (0,255,0), 2)

cv2.imshow("face_detection", image)
cv2.waitKey()

# save output
cv2.imwrite("face_detection.jpg", image)

# release resources
cv2.destroyAllWindows()