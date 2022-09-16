import time
import board
import digitalio
import pwmio
from adafruit_motor import servo
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP16)
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP11)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
pwm_servo = pwmio.PWMOut(board.GP6, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
l = 0

servo1.angle=0
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
            time.sleep(.5)
            if i <= 3:
                led.value = True
                #print(i)
                led.value = False
                servo1.angle = 60*(4-i)
                time.sleep(0.05)
            if not button.value:
                    print("ABORT")
                    time.sleep(1)
                    abortcheck = 0
                    break



        if abortcheck == 0:
            led2.value = False
        else:
            led2.value = True
            print("LIFTOFF")

