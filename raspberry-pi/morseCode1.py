import time
import board
import digitalio
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier
list=[]
message = input("Enter message: ")
message=message.upper()
final = ""
for letter in message:
    list.append(letter)
    if letter == " ":
        final = final + "/" + " "

    else:
        final = final + MORSE_CODE[letter] + " " 
print (final)

for character in final:
    if character == ".":
        led.value = True
        time.sleep(dot_time)
    if character == "-":
        led.value = True
        time.sleep(dash_time)
    if character == "/":
        led.value = True
        time.sleep(between_words)
    if character == "":
        led.value = True
        time.sleep(between_letters)
    led.value = False
    time.sleep(between_taps)

