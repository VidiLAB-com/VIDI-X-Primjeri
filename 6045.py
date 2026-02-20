import time
import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

upaljeno = 1
ugaseno = 9

Led.value = True
time.sleep(upaljeno)
Led.value = False
time.sleep(ugaseno)

upaljeno = upaljeno + 1 #Sada je vrijednost upaljeno = 2
ugaseno = ugaseno - 1 #Sada je vrijednost ugaseno = 8

Led.value = True
time.sleep(upaljeno)
Led.value = False
time.sleep(ugaseno)

upaljeno = upaljeno + 1 #Sada je vrijednost upaljeno = 3
ugaseno = ugaseno - 1 #Sada je vrijednost ugaseno = 7

Led.value = True
time.sleep(upaljeno)
Led.value = False
time.sleep(ugaseno)

upaljeno = upaljeno + 1 #Sada je vrijednost upaljeno = 4
ugaseno = ugaseno - 1 #Sada je vrijednost ugaseno = 6

Led.value = True
time.sleep(upaljeno)
Led.value = False
time.sleep(ugaseno)

upaljeno = upaljeno + 1 #Sada je vrijednost upaljeno = 5
ugaseno = ugaseno - 1 #Sada je vrijednost ugaseno = 5