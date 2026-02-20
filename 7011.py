import board
import digitalio
import time

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

# Funkcija za Slovo A
def slovoA():
    Led.value = True
    time.sleep(1)
    Led.value = False
    time.sleep(1)
    Led.value = True
    time.sleep(2)
    Led.value = False
    time.sleep(2)

#Slovo S
Led.value = True
time.sleep(1)
Led.value = False
time.sleep(1)
Led.value = True
time.sleep(1)
Led.value = False
time.sleep(1)
Led.value = True
time.sleep(1)
Led.value = False
time.sleep(2)

#Slovo A - pozivamo funkciju
slovoA()

#Slovo R
Led.value = True
time.sleep(1)
Led.value = False
time.sleep(1)
Led.value = True
time.sleep(2)
Led.value = False
time.sleep(1)
Led.value = True
time.sleep(1)
Led.value = False
time.sleep(2)

#Slovo A
slovoA()