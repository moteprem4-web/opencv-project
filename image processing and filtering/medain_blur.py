import cv2

image1=cv2.imread("trre.png")

clean=cv2.medianBlur(image1,9)

cv2.imshow("original image",image1)
cv2.imshow("cleanded_image",clean)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("cleaned.jpg",clean)




