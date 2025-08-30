import cv2

image1=input("Enter the address of the image")

image=cv2.imread(image1,1)

if image is not None:
    success=cv2.imwrite("flower.jpg",image)
    if success:
        print("image is sucessfully saved")
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow("image demo",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("file is not saved")
else:
    print("image is not possible")


