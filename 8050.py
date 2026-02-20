import board
import time
import simpleio

# Pin na koji je spojen vanjski zvučnik
PIEZO_PIN = board.GPIO25

while True:
    simpleio.tone(PIEZO_PIN, 262, duration=0.5)
    time.sleep(0.5)
    simpleio.tone(PIEZO_PIN, 330, duration=0.5)
    time.sleep(0.5)