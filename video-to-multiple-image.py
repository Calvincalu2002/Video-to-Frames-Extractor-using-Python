#Break video into multiple images and store in a folder

import cv2


vidcap=cv2.VideoCapture("C:\\Users\\anton\\Downloads\\walk.mp4")
ret,image=vidcap.read() #for reading image
count=0
while True:
    if ret==True:
        #read frames is writen 
        cv2.imwrite("C:\\Users\\anton\\Desktop\\demo (1)\\frames\\no.ofimages%d.jpg"%count,image)
        #vidcap.set(cv2.CAP_PROP_POS_MSEC, (count**100))#video capturing speed
        ret,image=vidcap.read()#to avoid error read image again
        cv2.imshow("res", image)
        print(count)
        
        count+=1
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
           cv2.destroyAllWindows()

vidcap.release()
cv2.destroyAllWindows()