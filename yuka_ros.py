import cv2
import numpy as np

import rospy

from hsrb_interface import Robot

import ros_numpy

from sensor_msgs.msg import PointCloud2 , Image
import geometry_msgs.msg
from geometry_msgs.msg import PointStamped

import tf

robot = Robot()
base = robot.try_get('omni_base')
# tts = robot.try_get('default_tts')
# whole_body = robot.try_get('whole_body')
collision_world = robot.try_get("collision_world")

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

cv2.imwrite("ccc.jpg",opening)

def callback(pcl):
    for cnt in contours:
        print()
        _x,_y,width,height=cv2.boundingRect(cnt)
        cv2.rectangle((opening),(_x,_y),(_x+width,_y+height),color=(255,255,255),thickness=2)
        
        pc_np = ros_numpy.numpify(pcl)
        x, y, z, _  =pc_np[_x, _y]

        print(x,y,z)

        _point=PointStamped()

        _point.header.stamp = rospy.Time.now()
        _point.header.frame_id = "/head_tilt_link"
        _point.point.x = x
        _point.point.y = y
        _point.point.z = z

        now = rospy.Time.now()
        try:
            tf_base_map.waitForTransform(
                "/head_tilt_link", "/map", now, rospy.Duration(4.0))
            point = tf_base_map.transformPoint("/map", _point)

            print("tochuu")

            collision_world.add_box(
                x=point.point.x, y=point.point.y, z=point.point.z, pose=geometry.pose(x=1.0, z=0.15), frame_id='map')
            
            #print(_point)
            print(point)
        except:
            print("but")
        
#rospy.init_node("yuka")
tf_base_map = tf.TransformListener()
sub = rospy.Subscriber('/hsrb/head_rgbd_sensor/depth_registered/rectified_points', PointCloud2, callback) 
rospy.spin()