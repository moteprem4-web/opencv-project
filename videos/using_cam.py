import cv2


cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read() #true or false return

    if not ret:
        print("couold not read frame")
        break
    cv2.imshow("webcam feed",frame)
   

    if cv2.waitKey(1) & 0xFF==  ord('q'):
            print("queting..")
            break
cap.release()
cv2.destroyAllWindows()
