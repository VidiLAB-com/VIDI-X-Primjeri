import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

broj_1 = 3
broj_2 = 6

if broj_1 > 2 or broj_2 < 8:
    Led.value = True
else:
    Led.value = False