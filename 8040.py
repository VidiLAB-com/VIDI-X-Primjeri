import time
import board
import pwmio

led = pwmio.PWMOut(board.STATUS, frequency=5000, duty_cycle=0)

for i in range(10):
    led.duty_cycle = 13107  # LED na 20% svjetline
    time.sleep(0.5)
    led.duty_cycle = 52428  # LED na 80% svjetline
    time.sleep(0.5)