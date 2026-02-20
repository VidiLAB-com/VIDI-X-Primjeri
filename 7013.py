import board
import digitalio
import time

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

def treperenje(upaljeno, ugaseno):
    Led.value = True
    time.sleep(upaljeno)
    Led.value = False
    time.sleep(ugaseno)

    upaljeno = upaljeno + 1
    Led.value = True
    time.sleep(upaljeno)
    Led.value = False

    Ugaseno = ugaseno + 3
    time.sleep(ugaseno)

    upaljeno = upaljeno + ugaseno + 4
    Led.value = True
    time.sleep(upaljeno)
    
treperenje(1,2)
Led.value = False