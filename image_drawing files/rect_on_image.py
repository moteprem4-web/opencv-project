import cv2

image=cv2.imread("ani.jpg")

if image is None:
    print("the image is not loaded")
else:
    print("the image is loaded")
    p1 = (1500, 1500)
    p2 = (2050, 2000)
    color=(0,255,200)
    thickness=4
    cv2.rectangle(image,p1,p2,color,thickness)
    resized = cv2.resize(image, (300, 300))
    cv2.imshow("rectangle on image",resized)
    cv2.imwrite("CAT.jpg ",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




