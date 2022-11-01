from re import sub
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


rospy.init_node("aaaaa")
bridge = CvBridge()
i=0

def callback(data):
    global i
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        print(e)

    i+=1
    print('img/'+str(i)+'.jpg')
    cv2.imwrite('img/'+str(i)+'.jpg', cv_image)
    


def start_node():
    
    rospy.Subscriber("/hsrb/head_rgbd_sensor/rgb/image_raw", Image, callback)
    rospy.sleep(0.5)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
