import cv2

image=cv2.imread("flower.jpg")

if image is  not None:
    print("the image is loaded")
    resizing=cv2.resize(image,(300,300))
    cv2.imshow("this is image",image)
    cv2.imshow("resized",resizing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


else:
    print("the image is not loaded")