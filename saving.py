import cv2

image=cv2.imread("a.webp")
if image is not None:
    success=cv2.imwrite("a.webp",image)
    if success:
        print("image is saved")
    else:
        print(" image is not saved")
else:
    print("Error: could not load image")