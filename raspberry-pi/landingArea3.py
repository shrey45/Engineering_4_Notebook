import time
import board
import digitalio
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import displayio
import terminalio
import math
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

displayio.release_displays()

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
led2 = digitalio.DigitalInOut(board.GP16)
led2.direction = digitalio.Direction.OUTPUT
mpu = adafruit_mpu6050.MPU6050(i2c)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP18)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

bestTri= [0,10000000,0, 0, 0, 0, 0, 0]

def tri(x1, y1, x2, y2, x3, y3):
  x1 = float(x1)
  x2 = float(x2)
  x3 = float(x3)
  y1 = float(y1)
  y2 = float(y2)  
  y3 = float(y3)
  #area = abs(x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))
  area = abs((x1*y2+x2*y3+x3*y1-y1*x2-y2*x3-y3*x1)/2)
  print(area)
  [Ccoorx, Ccoory] = (x1+x2+x3)/3,(y1+y2+y3)/3
  centroid = ((Ccoorx)**2 + (Ccoory)**2)**(0.5)

  splash = displayio.Group()
  g1line = Line(64,0,64,64, color=0xFFFF00)
  splash.append(g1line)
  g2line = Line(0,32,128,32, color=0xFFFF00)
  splash.append(g2line)
  circle = Circle(64, 32, 2, outline=0xFFFF00)
  splash.append(circle)
  triangle = Triangle(int(x1) + 64, -int(y1) + 32, int(x2) + 64, -int(y2) + 32, int(x3) + 64, -int(y3) + 32, outline=0xFFFF00)
  splash.append(triangle)
  display.show(splash)
  return [area, centroid]


points = [[-50,-17,-57,12,-22,-7],[28,-14,60,-7,54,18],[45,30,51,-1,18,6],[5,5,19,15,22,10]]

try:

  for i in range(len(points)):
    [xcoor1, ycoor1] = points[i][0],points[i][1]
    [xcoor2, ycoor2] = points[i][2],points[i][3]
    [xcoor3, ycoor3] = points[i][4],points[i][5]
    
    data = tri(xcoor1, ycoor1, xcoor2, ycoor2, xcoor3, ycoor3)
    if data[0] > 100 and data[1] < bestTri[1]:
      bestTri = [data[0], data[1], xcoor1, ycoor1, xcoor2, ycoor2, xcoor3, ycoor3]
  print(bestTri)
  print(f"The closest suitable landing area has vertices ({bestTri[2]},{bestTri[3]}), ({bestTri[4]},{bestTri[5]}), ({bestTri[6]},{bestTri[7]}). The area is {bestTri[0]} km2 and the centroid is {bestTri[1]} km away from base")

except:
  print("bro lock in")
while True:
  pass