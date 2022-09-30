import time
import board
import digitalio
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import displayio
import terminalio
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

def angular_vel ():
    print(f"x = {mpu.gyro[0]}, y = { mpu.gyro[1]}, z = {mpu.gyro[2]}")
    time.sleep(1)


while True:
    if abs(mpu.acceleration[0]) >= 9 or abs(mpu.acceleration[1]) >= 9:
        led2.value = True
    else:
        led2.value = False
    print(f"x = {mpu.acceleration[0]}, y = { mpu.acceleration[1]}, z = {mpu.acceleration[2]}")
    time.sleep(.1)
    
# create the display group
    splash = displayio.Group()

# add title block to display group
    title = f"x = {mpu.gyro[0]}"
# the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)

    title1 = f"y = {mpu.gyro[1]}"
# the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title1, color=0xFFFF00, x=5, y=15)
    splash.append(text_area)

    title2 = f"z = {mpu.gyro[2]}"
# the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title2, color=0xFFFF00, x=5, y=25)
    splash.append(text_area)        

# you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
# Don't forget to round the angular velocity values to three decimal places

# send display group to screen
    display.show(splash)

