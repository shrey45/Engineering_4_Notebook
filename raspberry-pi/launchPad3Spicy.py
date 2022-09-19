import time
import board
import digitalio
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP16)
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP11)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

print('ready')

abortcheck = 0

while True:
    if not button.value:
        abortcheck = 1
        for i in range(10,0,-1):
            led.value = True
            print(i)
            time.sleep(.5)
            led.value = False
            if not button.value:
                print("ABORT")
                time.sleep(1)
                abortcheck = 0
                break
            time.sleep(.5)
        if abortcheck == 0:
            led2.value = False
        else:
            led2.value = True
            print("LIFTOFF")

