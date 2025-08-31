import cv2


image = cv2.imread("tri.png")

if image is None:
    print("Image can't load")
else:
    print("Image Loaded successfully")

  
    p1 = (100, 400)   # bottom-left corner
    p2 = (400, 100)   # top-right corner

    color = (0, 200, 255)   
    thickness = 4

    cv2.line(image, p1, p2, color, thickness)

    
    cv2.imshow("Line on Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
