import time
import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

cekanje = 1

Led.value = True
time.sleep(cekanje)
Led.value = False
time.sleep(cekanje)
Led.value = True
time.sleep(cekanje)
Led.value = False
time.sleep(cekanje)