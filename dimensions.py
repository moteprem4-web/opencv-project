import cv2

image=cv2.imread("a.webp")

if image is not None:
    h,w,c=image.shape
    print(f"image loaded \n height{h}\n width{w}\n channel{c}")
else:
    print("could not load image")