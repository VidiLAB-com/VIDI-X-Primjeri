import board
import digitalio
import time

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

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

#Slovo A
Led.value = True
time.sleep(1)
Led.value = False
time.sleep(1)
Led.value = True
time.sleep(2)
Led.value = False
time.sleep(2)

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
Led.value = True
time.sleep(1)
Led.value = False
time.sleep(1)
Led.value = True
time.sleep(2)
Led.value = False
time.sleep(2)