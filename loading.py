import cv2

image=cv2.imread("a.webp")

if image is None:
    print("image is not possible ")
else:
    print("image loading successfully")
