import pathlib
import cv2
import numpy as np
#output_1617983094.avi  output_1617983281.avi  output_1617983359.avi

def ball_grid_detector(frame, circle_center):
    '''
    takes a frame and a center of a circle and determines in which 
    position of the grid the object is
    '''
    assert frame != None and circle_center != None, "[Error] recieved None.."
    V = frame.shape[0]
    H = frame.shape[1]
    ww = H//3 
    vv = V//3
    x,y = circle_center
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
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,
                            param1=threshold,param2=30,minRadius=10,maxRadius=80)
    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    except:
        return cimg, 0

    return cimg, len(circles[0,:])


# cap = cv2.VideoCapture('output_1617983359.avi')

# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         frame = ht(frame)
#         cv2.imshow('Tennis', frame)
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()
