import pathlib
import cv2
import numpy as np

def ball_grid_detector(frame_shape, circle_center):
    '''
    takes a frame and a center of a circle and determines in which 
    position of the grid the object is
    '''
    V = frame_shape[0]
    H = frame_shape[1]
    ww = H//3 
    vv = V//3
    x,y = circle_center[0]
    if x < ww:
        if y < vv:
            return 1
        elif y >= vv and y < vv*2:
            return 4
        else:
            return 7
    elif x >= ww and x < ww*2:
        if y < vv:
            return 2
        elif y >= vv and y < vv*2:
            return 5
        else:
            return 8
    else:
        if y < vv:
            return 3
        elif y >= vv and y < vv*2:
            return 6
        else:
            return 9

def ht(img, threshold):
    """
    Performs hough transform with specified threshold
    """
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,
                            param1=threshold,param2=30,minRadius=10,maxRadius=80)
    try:
        circles = np.uint16(np.around(circles))
        centers = []
        for i in circles[0,:]:
            centers.append((i[0],i[1]))
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    except:
        return cimg, 0, []

    return cimg, len(circles[0,:]), centers
