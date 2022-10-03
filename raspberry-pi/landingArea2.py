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
  splash = displayio.Group()
  g1line = Line(64,0,64,64, color=0xFFFF00)
  splash.append(g1line)
  display.show(splash)
  g2line = Line(0,32,128,32, color=0xFFFF00)
  splash.append(g2line)
  display.show(splash)
  circle = Circle(64, 32, 1, outline=0xFFFF00)
  splash.append(circle)
  triangle = Triangle(x1, y1, x2, y2, x3, y3, outline=0xFFFF00)
  splash.append(triangle)
  display.show(splash)
  return area

while True:

  try:

    [xcoor1, ycoor1] = input("Enter coordinate 1: ").split(",")
    [xcoor2, ycoor2] = input("Enter coordinate 2: ").split(",")
    [xcoor3, ycoor3] = input("Enter coordinate 3: ").split(",")
    area = tri(xcoor1, ycoor1, xcoor2, ycoor2, xcoor3, ycoor3)
    print(f"The area of a triangle with coordinates ({xcoor1},{ycoor1}), ({xcoor2},{ycoor2}), ({xcoor3},{ycoor3}) is {area}")
    




  except:
    print("bro lock in")