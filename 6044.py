import time
import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

upaljeno = 1
ugaseno = 9

Led.value = True
time.sleep(upaljeno)
Led.value = False
time.sleep(ugaseno)
Led.value = True
time.sleep(upaljeno)
Led.value = False
time.sleep(ugaseno)
Led.value = True
time.sleep(upaljeno)
Led.value = False
time.sleep(ugaseno)