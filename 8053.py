import board
import time
import simpleio

PIEZO_PIN = board.GPIO25

# Frekvencije nota
NOTE_C4 = 
NOTE_D4 = 
NOTE_E4 = 
NOTE_F4 = 
NOTE_G4 = 
NOTE_A4 = 
NOTE_B4 = 
NOTE_H4 = 
NOTE_C5 = 

trajanje = 0.27   
# mala pauza između nota
pauza = 0.15        

def ton(ton, taktovi):
    simpleio.tone(PIEZO_PIN, ton, duration=taktovi * trajanje)
    time.sleep(pauza)

while True:
    ton(NOTE_C4, 1)
    ton(NOTE_C4, 1)
    ton(NOTE_D4, 2)
    ton(NOTE_C4, 2)
    ton(NOTE_F4, 2)
    ton(NOTE_E4, 3)
    time.sleep(0.3)

    ton(NOTE_C4, 1)
    ton(NOTE_C4, 1)
    ton(NOTE_D4, 2)
    ton(NOTE_C4, 2)
    ton(NOTE_G4, 2)
    ton(NOTE_F4, 3)
    time.sleep(0.3)

    ton(NOTE_C4, 1)
    ton(NOTE_C4, 1)
    ton(NOTE_C5, 2)
    ton(NOTE_A4, 2)
    ton(NOTE_F4, 2)
    ton(NOTE_E4, 2)
    ton(NOTE_D4, 2)
    time.sleep(0.3)

    ton(NOTE_B4, 1)
    ton(NOTE_B4, 1)
    ton(NOTE_A4, 2)
    ton(NOTE_F4, 2)
    ton(NOTE_G4, 2)
    ton(NOTE_F4, 3)
    time.sleep(0.3)

    time.sleep(3)