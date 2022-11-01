import cv2
import numpy as np

import rospy

from hsrb_interface import Robot

input=cv2.imread("img/1.jpg")
bb=cv2.imread("img2/blank.jpg")
print(input.shape)
im_gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
blank = cv2.cvtColor(bb,cv2.COLOR_BGR2GRAY)
print(im_gray.shape)
img_blur = cv2.blur(input, (3, 3))
a=0



for i in range(480):
    a=i
    print("__________________________________")
    if i < 5 :
        continue

    for j in range(640):
        b=j
        if j < 5 :
            continue

        for k in range(3):
            #print(im_gray[i][j])
            dif=input[i][j][1]
            aaa=input[i][j-1][k]
            bbb=input[i-1][j][k]
            ans=dif-aaa
            ans2=dif-bbb
            #print(ans)
            if ans > 30 and ans < 200:
                print(ans)
                cv2.circle(blank, (b, a), 2, (255, 255, 255), thickness=-1)
            else:
                pass
            if ans2 > 30 and ans2 < 200:
                print(ans2)
                cv2.circle(blank, (b, a), 2, (255, 255, 255), thickness=-1)
            else:
                pass

kernel = np.ones((6,6),np.uint8)
opening = cv2.morphologyEx(blank, cv2.MORPH_OPEN, kernel)

contours=cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[0]
print(contours)

area_thresh = 30
contours = list(filter(lambda x: cv2.contourArea(x) > area_thresh, contours))

for cnt in contours:
    print()
    x,y,width,height=cv2.boundingRect(cnt)
    cv2.rectangle((opening),(x,y),(x+width,y+height),color=(255,255,255),thickness=2)
    


print(a)
cv2.imshow("aaa",im_gray)
cv2.imshow("bbb",opening)
cv2.imshow("ccc",blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
