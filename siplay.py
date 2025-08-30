import cv2

image=cv2.imread("a.webp")

if image is not  None:
    cv2.imshow("demo inage",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image is not displayed")