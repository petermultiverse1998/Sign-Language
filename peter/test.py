import numpy as np
import cv2

def resize(img):
    (height,width) = img.shape[:2]
    res = cv2.resize(img,(int(width*2.1),int(height*2.1)),interpolation = cv2.INTER_CUBIC)
    #cv2.imwrite(res,'result.png')
    return res

########### MAIN ############
cap = cv2.VideoCapture('perfect.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
if cap.isOpened()==False :
    print("Error opening video  file")

while cap.isOpened():
    ret,frame = cap.read()
    if ret==True:
        fgmask = fgbg.apply(frame)
        cv2.imshow('fgmask',fgmask)
        if cv2.waitKey(25) & 0xFF == 27:
            break
        elif cv2.waitKey(25) & 0xFF == ord('s'):
            cv2.imwrite('peter.png',frame)
    else:
        break
    
cap.release()
cv2.destroyAllWindows()