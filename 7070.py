import time
import board
import digitalio

# Postavite tipku A
switchA = digitalio.DigitalInOut(board.BTN_A)
switchA.direction = digitalio.Direction.INPUT
switchA.pull = digitalio.Pull.UP

# Postavite tipku B
switchB = digitalio.DigitalInOut(board.BTN_B)
switchB.direction = digitalio.Direction.INPUT
switchB.pull = digitalio.Pull.UP

# Postavite LED lampicu
led = digitalio.DigitalInOut(board.STATUS)
led.direction = digitalio.Direction.OUTPUT

while True:
    if not switchA.value or not switchB.value:
        led.value = True
    else:
        led.value = False
    time.sleep(0.1)