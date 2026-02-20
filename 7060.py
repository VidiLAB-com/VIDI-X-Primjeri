import time
import board
import digitalio

# Postavite tipku
switch = digitalio.DigitalInOut(board.BTN_A)  
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP  

# Postavite LED lampicu
led = digitalio.DigitalInOut(board.STATUS)  
led.direction = digitalio.Direction.OUTPUT

while True:
    if not switch.value:  
        led.value = True  
    else:
        led.value = False 