import board
import digitalio
import time
led1 = digitalio.DigitalInOut(board.GP16) #GP16 is the green led
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP15) #GP 15 is the red led
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP11)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP


print('Ready')

while True:
    if not button.value:
        print ('ok')
        for x in range(10, 0, -1): #this says (the starting number, the ending number, the number to count by)
            print(x)
            led2.value = True
            time.sleep (.2)
            led2.value = False
            time.sleep (.8)
        print ("Liftoff!")
        led1.value = True
