import cv2

image=cv2.imread("a.webp")


blured=cv2.GaussianBlur(image,(7,7),3)
cv2.imshow("original image",image)
cv2.imshow("blured image",blured)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("_Image.jpg",blured)
