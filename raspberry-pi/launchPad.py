import time
import board
import digitalio
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP16)
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP11)
button.direction = digitalio.Direction.INPUT


if button.value == True:
    for i in range(10,0,-1):
        led.value = True
        print(i)
        time.sleep(.5)
        led.value = False
        time.sleep(.5)
    
    
while True:
    led2.value = True
