# Duckiequeen
Members:
- Bishoy Roufael
- Al-ameen Mawji
- Mohamed Dorrabb Khan Niazi

This project is based on the duckietown project and is part of 2020 JUB
Robotics Lab. 

# Problem we are solving and a solution
We are considering the object detecting and vision part of the duckie.
For simplicity we choose a ball as a target object that we want to detect and make the robot follow the ball.
We are using **Hough Transforms** algorithm to detect the circle. we are using
the implementation from *cv2* to detect the number of circular objects in the
camera setting. A pool ball can be used as a demo.

# Usage
The code is written in python script which can be run directly in a ROS
environment. cd into the source folder. run `chmod +x main.py` to be able to
run the py script as executable. Then directly run `./main.py`.

The algorithms used in the project are presented in the `utils.py` script. 



There are some video demos of the hough transform detection presented as well in the repo as `.avi` videos
