import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

Led.value = True
Led.value = False
