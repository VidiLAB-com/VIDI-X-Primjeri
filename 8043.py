import time
import board
import pwmio

led = pwmio.PWMOut(board.STATUS, frequency=5000, duty_cycle=0)

while True:
    for i in range(0, 65535, 50): # Postupno pojavljivanje
        led.duty_cycle = i
        time.sleep(0.001)
    for i in range(65535, 0, -50): #Postupno nestajanje
        led.duty_cycle = i
        time.sleep(0.001)