import cv2
fd=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#video read using web cam
vid=cv2.VideoCapture(0)
#mai loop to AND show image until we break the loop
while True:
    flag,img=vid.read()
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #th,img=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
    #if flag is true than only show image
    if flag:
        faces=fd.detectMultiScale(img,1.1,5)
        for x,y,w,h in faces:
        #draw rectangle on img
            cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,0),thickness=3)
        cv2.imshow("webimage",img)
        key=cv2.waitKey(1)
        if key==ord("q"):
            break
    else:
        break
cv2.destroyAllWindows()

vid.release()
