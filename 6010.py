import time
import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

Led.value = True
time.sleep(1)
Led.value = False
time.sleep(1)