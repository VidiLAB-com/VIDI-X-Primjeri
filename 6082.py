import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GPIO2)
led.direction = digitalio.Direction.OUTPUT

brojac = 1

while brojac <= 5:
    if brojac <= 3:
        led.value = True
    else:
        led.value = False

    time.sleep(2)
    brojac = brojac + 1
    print(brojac)