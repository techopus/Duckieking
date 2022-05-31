# Duckieking
Members:
- Nitin Bhagat
- Maurice Yan Kayijamahe
- Mohamed Amine Kina

This project is based on the duckietown project where we detect the circle i.e. a round ball in our case and follow it as long as the duckieking can see it.

# Problem we are solving and a solution
We are considering the object detecting and vision part of the duckietown.
We take a ball as a target object which we want to detect and make the duckieking follow the ball.
We are using **Hough Transforms** algorithm specifically Circle Hough Transform (CHT) to detect the circle. we are using
the implementation from *cv2* to detect the number of circular objects in the
camera setting. So we have the function parameters as mathematical formula to detect the circle. Any round ball can be used as a demo. We have used a medium-sized plastic ball.

# RUN 
The code is written in python script which can be run directly in a ROS
environment. cd into the source folder. run `chmod +x main.py` to be able to
run the py script as executable. Then directly run `./main.py`.

`utils.py` script contains the algorithm(cht) that we are using for the detection.

P.S. you might also need to have duckietowns_msgs package for ROS message and services definitions in the directory with main.py.



There are some video demos of the hough transform detection presented as well in the repo as `.MOV` videos (Also link in case: https://drive.google.com/file/d/1tby0ArOWmqUBoEClwud2TsRSJ6CEXYj5/view?ts=629429ac)
