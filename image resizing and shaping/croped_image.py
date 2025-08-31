import cv2

image1 = cv2.imread("flower.jpg")

if image1 is   None:
    print("Error: Image not found. Check the file path")
else:
    cropped = image1[50:500, 50:300]
    cv2.imshow("Original", image1)
    cv2.imshow("Cropped", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
