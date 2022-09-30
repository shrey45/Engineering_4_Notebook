from stringprep import c22_specials


def add_numbers(num1, num2):
  total = num1 + num2
  return total

def coordinates():
  c1 = c1.split(",")
  try:
    x1 = float(c1[0])
  except:
    print("DUDE")
    coordinates()
  try:
    y1 = float(c1[1])
  except:
    print("DUDE")
    coordinates()
  print(f"x1 = {x1}")
  print(f"y1 = {y1}")
  c2 = c2.split(",")
  try:
    x2 = float(c2[0])
  except:
    print("DUDE")
    coordinates()
  try:
    y2 = float(c2[1])
  except:
    print("DUDE")
    coordinates()
  print(f"x2 = {x2}")
  print(f"y2 = {y2}")
  c3 = c3.split(",")
  try:
    x3 = float(c3[0])
  except:
    print("DUDE")
    coordinates()
  try:
    y3 = float(c3[1])
  except:
    print("DUDE")
    coordinates()
  print(f"x3 = {x3}")
  print(f"y3 = {y3}")

#def distance():
 # sqrt

while True:
    c1 = input('Enter coordinates:')
    c2 = input('Enter coordinates:')
    c3 = input('Enter coordinates:')

    coordinates()
 

