#! /usr/bin/env python
"""
Duckieking main file to follow a circle
"""
import rospy
from duckietown_msgs.msg import WheelsCmdStamped
import numpy as np
from sensor_msgs.msg import CompressedImage
import matplotlib.pyplot as plt
import cv2
import time
from utils import ht, ball_grid_detector
grid = 1

class ImageSub():
    """
    Subscriber class
    """
    _r = None
    def __init__(self):
        self._s = rospy.Subscriber('/duckieking/camera_node/image/compressed', CompressedImage, self.callback)
        rospy.loginfo('[INFO] Started Laser Subscriber Node ..')
        self.img = None
        self.threshold = 200

    def callback(self, msg):
        """
        Take image, detect circles, follow
        """
        np_arr = np.fromstring(msg.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        res_from_ht, circles, centers = ht(image_np, self.threshold)
        if not circles:
            self.threshold = max(5, self.threshold - 2)
        elif circles > 1:
            self.threshold = min(500, self.threshold + 1)
        else:
            pos = ball_grid_detector(image_np.shape, centers)
            print("Grid idx pos: {}".format(pos))
            grid = (pos - 1) % 3
                   
            if grid == 1:
                speed_p.move(0.5,0.5)
            elif grid == 0: 
                speed_p.move(0.2,0.5)
            elif grid == 2:
                speed_p.move(0.5,0.2)
            else:
                speed_p.stop() 
       # print("Circles length : {} Threshold : {}".format(circles,self.threshold))
        cv2.imshow('Ball',res_from_ht)
        cv2.waitKey(1)
        

class Publisher():
    """
    Publisher to duckie's wheels
    """
    def __init__(self):
        self._p = rospy.Publisher('duckieking/wheels_driver_node/wheels_cmd', WheelsCmdStamped, queue_size=1)
        self._s = WheelsCmdStamped()
        rospy.loginfo('[INFO] Started Publisher Node ..')

    def move(self, l_v, r_v):
      """
      Move by specified left and right velocities
      """
      self._s.vel_left = l_v
      self._s.vel_right = r_v
      self.publish_once_in_cmd_vel(self._s)

    def stop(self):
      """
      Stop duckie completely
      """
      self._s.vel_left = 0
      self._s.vel_right = 0
      self.publish_once_in_cmd_vel(self._s)


    def publish_once_in_cmd_vel(self, cmd):
        """
        Publish one msg to duckie's wheels
        """
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
        rospy.init_node('duckieking_follow_ball', anonymous=True)
        speed_p = Publisher()
        subscriber = ImageSub()
     
    except rospy.ROSInterruptException:
        pass
