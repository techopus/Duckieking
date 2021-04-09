#! /usr/bin/env python

import rospy
from duckietown_msgs.msg import WheelsCmdStamped
import numpy as np
from sensor_msgs.msg import CompressedImage
import matplotlib.pyplot as plt
import cv2
import time


def ht(img):
    #img = cv2.medianBlur(img,5)
    
    #cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1, 50,
                                param1=200,param2=18,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x,y,r) in circles:
            cv2.circle(img, (x,y), r, (36,255,12), 3)

    #for i in circles[0,:]:
    #    # draw the outer circle
    #    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    #    # draw the center of the circle
    #    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    
    return img

class LaserSubscriber():
    _r = None
    def __init__(self):
        self._s = rospy.Subscriber('/duckiequeen/camera_node/image/compressed', CompressedImage, self.callback)
        rospy.loginfo('[INFO] Started Laser Subscriber Node ..')
        self.img = None
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(f'output_{int(time.time())}.avi', self.fourcc, 20.0, (640, 480))

    def callback(self, msg):
        np_arr = np.fromstring(msg.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        #hsv = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)
        self.out.write(image_np)
        #image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        #res_from_ht = ht(image_np)
        cv2.imshow('Tennis Ball', image_np)
        cv2.waitKey(1)
        

class Publisher():
    def __init__(self):
        self._p = rospy.Publisher('duckiequeen/wheels_driver_node/wheels_cmd', WheelsCmdStamped, queue_size=1)
        self._s = WheelsCmdStamped()
        rospy.loginfo('[INFO] Started Publisher Node ..')

    def MoveStraight(self, l_v, r_v):
      self._s.vel_left = l_v
      self._s.vel_right = r_v
      self.publish_once_in_cmd_vel(self._s)

    def Stop(self):
      self._s.vel_left = 0
      self._s.vel_right = 0
      self.publish_once_in_cmd_vel(self._s)


    def publish_once_in_cmd_vel(self, cmd):
        while True:
            connections = self._p.get_num_connections()
            if connections > 0:
                self._p.publish(cmd)
                break
            else:
                rospy.Rate(1).sleep()


# Test
if __name__ == '__main__':
    try:
        rospy.init_node('our_shitty_duckiequeen', anonymous=True)
        bullshit = LaserSubscriber()
        speed_publisher = Publisher()
        speed_publisher.MoveStraight(0.0,0.0)

       # rospy.sleep(5) # Move for five seconds
       # speed_publisher.MoveStraight(0.0,0.0)
        rospy.spin()
        # speed_publisher.StopRobot()
    except rospy.ROSInterruptException:
        pass


