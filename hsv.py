'''
HSV(Hue, saturation and Value)
Hue: corresponds to the color component(base pigment),hence just by selecting a range of Hue you can select any color(0-360)
Saturation: is the amount od colour (depth of the pigment)(dominance of Hue) (0-100%)
value: is basically the brightness of the colour .(0-100%)
'''

import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar('LH',"Tracking", 0,255, nothing)#lower hue
cv2.createTrackbar('LS',"Tracking", 0,255, nothing)#lower saturation
cv2.createTrackbar('LV',"Tracking", 0,255, nothing)# lower value

cv2.createTrackbar('UH',"Tracking", 255,255, nothing)#uper Hue
cv2.createTrackbar('US',"Tracking", 255,255, nothing)# upper Saturatiom
cv2.createTrackbar('UV',"Tracking", 255,255, nothing)# Upper Value

while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()