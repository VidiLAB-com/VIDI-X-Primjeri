import board
import time
import simpleio

PIEZO_PIN = board.GPIO25
while True:
    for i in range(100, 800, 100):
        simpleio.tone(PIEZO_PIN, i, duration=0.5)
        time.sleep(2)
        print (i)