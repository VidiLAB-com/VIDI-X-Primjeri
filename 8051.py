import board
import time
import simpleio

# Pin na koji je spojen vanjski zvučnik
PIEZO_PIN = board.GPIO25
while True:
    for i in range(1000, 8000, 1000):
        simpleio.tone(PIEZO_PIN, i, duration=0.5)
        time.sleep(2)