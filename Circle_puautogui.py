# import math
# import pyautogui
# def circle(radius = 5, accuracy = 360, xpos=0, ypos=0, speed = 5):
#     angle = 360/accuracy
#     CurAngle = 0
#     x = []
#     y = []
#     sped = speed/accuracy
#     for i in range(accuracy):
#         x.append(xpos + radius*math.sin(math.radians(CurAngle)))
#         y.append(ypos + radius*math.cos(math.radians(CurAngle)))
#         CurAngle += angle
#     for i in x:
#         i = int(i)
#         pyautogui.moveTo(x[i], y[i], duration = sped)
# circle(xpos=200,ypos=200)

import pyautogui
import math

pyautogui.alert('OK?')
# Radius 
R = 150
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = pyautogui.position(x/2,y/2)
# offsetting by radius 
pyautogui.moveTo(X+R,Y)

for i in range(360):
    # setting pace with a modulus 
    if i%6==0:
       pyautogui.click(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))