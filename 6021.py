import time
import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

crveno = 4
zuto = 2
zeleno = 5
pauza = 0.5

Led.value = True
time.sleep(crveno)
Led.value = False
time.sleep(pauza)
Led.value = True
time.sleep(zuto)
Led.value = False
time.sleep(pauza)
Led.value = True
time.sleep(zeleno)
Led.value = False
time.sleep(pauza)