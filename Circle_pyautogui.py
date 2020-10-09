import pyautogui
import math

# Circle Radius 
R = 150
# Circle Angle
angle = 360
# Number of Points
points = 6
# Center Position
X = 500
Y = 500

pyautogui.moveTo(X+R,Y)

for i in range(angle):
    if i%(360/points)==0:
        pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))