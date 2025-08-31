import cv2

image1=cv2.imread("flip.jpg")

if image1 is None:
    print("the image can't load")

else:
    flipped_hor=cv2.flip(image1,1)
    flipped_ver=cv2.flip(image1,0)
    flipped_both=cv2.flip(image1,-1)
    cv2.imshow("original",image1)

    cv2.imshow("Flipped horizontal",flipped_hor)
    
    cv2.imshow("Flipped vertical",flipped_ver)
    
    cv2.imshow("Flipped both",flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

