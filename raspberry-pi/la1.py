import math

def tri(x1, y1, x2, y2, x3, y3):
  x1 = float(x1)
  x2 = float(x2)
  x3 = float(x3)
  y1 = float(y1)
  y2 = float(y2)  
  y3 = float(y3)
  area = abs(x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y3-y2))
  return area

while True:

  [xcoor1, ycoor1] = input("Enter coordinate 1: ").split(",")
  [xcoor2, ycoor2] = input("Enter coordinate 2: ").split(",")
  [xcoor3, ycoor3] = input("Enter coordinate 3: ").split(",")
  tri(xcoor1, ycoor1, xcoor2, ycoor2, xcoor3, ycoor3)
  
