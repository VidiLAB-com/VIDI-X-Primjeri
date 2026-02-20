import time
import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

upaljeno = 1
ugaseno = 1
brojac = 1

while brojac < 3:
    Led.value = True
    time.sleep(upaljeno)
    Led.value = False
    time.sleep(ugaseno)
    
    brojac = brojac + 1