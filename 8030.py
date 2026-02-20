import time
import board
import pwmio

led = pwmio.PWMOut(board.STATUS, frequency=5000, duty_cycle=0) 

while True:
    led.duty_cycle = 13107 
    time.sleep(2)
    led.duty_cycle = 53083  
    time.sleep(1)