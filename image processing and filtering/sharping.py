import cv2
import numpy as np 


image1=cv2.imread("image_for_sharped.png")

sharpen_kernel=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharped=cv2.filter2D(image1,-1,sharpen_kernel)
cv2.imshow("original image",image1)
cv2.imshow("Sharped image",sharped)
cv2.imwrite("sharped.jpg",sharped)
cv2.waitKey(0)
cv2.destroyAlWindows()




