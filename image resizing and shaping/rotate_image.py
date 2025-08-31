import cv2

image=cv2.imread("tri.png")

if image is  None:
    print("image is not loaded")

else:
    (h,w)=image.shape[:2]
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,1,2)
    rotated=cv2.warpAffine(image,M,(w,h))

    cv2.imshow("original",image)
    cv2.imshow("rotated",rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()