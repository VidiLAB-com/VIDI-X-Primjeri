import board
import time
import simpleio

PIEZO_PIN = board.GPIO25

NOTE_C4 = 
NOTE_D4 = 
NOTE_E4 = 
NOTE_F4 = 
NOTE_G4 = 
NOTE_A4 = 
NOTE_B4 = 
NOTE_H4 = 
NOTE_C5 = 

trajanje = 

# glavna petlja
while True:
    simpleio.tone(PIEZO_PIN, NOTE_C4, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_C4, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_D4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_C4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_F4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_E4, duration = 4 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_C4, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_C4, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_D4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_C4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_G4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_F4, duration = 4 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_C4, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_C4, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_C5, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_A4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_F4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_E4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_D4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_B4, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_B4, duration = trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_A4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_F4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_G4, duration = 2 * trajanje)
    simpleio.tone(PIEZO_PIN, NOTE_F4, duration = 4 * trajanje)
    time.sleep(3)
