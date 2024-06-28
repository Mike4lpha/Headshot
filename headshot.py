import cv2
import time
import mediapipe as mp
import FaceMeshModule as fmm

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
pTime = 0
detector = fmm.FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img,draw=False)
    # if len(faces)!= 0:
        # print(faces[0][151])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    if len(faces)!= 0:
     x=faces[0][151][0]
     y=faces[0][151][1]
    cv2.circle(img,(x,y),7,(0,0,255),-1)
    cv2.line(img,(x,0),(x,720),(255,255,255),3)
    cv2.line(img,(0,y),(1280,y),(255,255,255),3)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
   
