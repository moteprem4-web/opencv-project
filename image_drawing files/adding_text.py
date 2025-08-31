import cv2

image=cv2.imread("ani.jpg")

if image is None:
    print("the image is not loaded")
else:
    print("the image is loaded")
    cv2.putText(image,"hello python programmerS",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,250,0),2)
    cv2.imshow("rectangle on image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





