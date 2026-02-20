import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

broj = 3

if broj > 2:
    Led.value = True
else:
    Led.value = False