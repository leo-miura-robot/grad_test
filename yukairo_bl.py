import cv2
import numpy as np


input=cv2.imread("img/1.jpg")
blank=cv2.imread("img2/blank.jpg")
print(input.shape)
im_gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
print(im_gray.shape)
img_blur = cv2.blur(im_gray, (3, 3))
a=0



for i in range(480):
    a=i
    print("__________________________________")
    for j in range(640):
        b=j
        #print(im_gray[i][j])
        dif=img_blur[i][j]
        aaa=img_blur[i][j-1]
        bbb=img_blur[i-1][j]
        ans=dif-aaa
        ans2=dif-bbb
        #print(ans)
        if ans > 30 and ans < 150:
            print(ans)
            #cv2.circle(im_gray, (b, a), 1, (0, 0, 0), thickness=-1)
            cv2.circle(blank, (b, a), 3, (255, 255, 255), thickness=-1)
        else:
            pass
            #cv2.circle(blank, (b, a), 1, (255, 255, 255), thickness=-1)
        if ans2 > 50 and ans2 < 150:
            print(ans2)
            #cv2.circle(im_gray, (b, a), 1, (0, 0, 0), thickness=-1)
            cv2.circle(blank, (b, a), 3, (255, 255, 255), thickness=-1)
        else:
            pass
            #cv2.circle(blank, (b, a), 1, (255, 255, 255), thickness=-1)


kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(blank, cv2.MORPH_OPEN, kernel)
print(a)
cv2.imshow("aaa",im_gray)
cv2.imshow("bbb",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()