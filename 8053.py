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
    simpleio.tone(PIEZO_PIN, NOTE_C4, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_C4, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_D4, trajanje= 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_C4, trajanje= 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_F4, trajanje= 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_E4, trajanje= 4 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_C4, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_C4, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_D4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_C4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_G4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_F4, trajanje = 4 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_C4, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_C4, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_C5, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_A4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_F4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_E4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_D4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_B4, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_B4, trajanje = trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_A4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_F4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_G4, trajanje = 2 * trajanje) 
    simpleio.tone(PIEZO_PIN, NOTE_F4, trajanje = 4 * trajanje) 
    time.sleep(3) 