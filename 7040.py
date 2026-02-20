import digitalio
import board
import displayio
import time
import xpt2046_circuitpython
import adafruit_rgb_display.ili9341 as ili9341
#  Oslobodite sve resurse koji se trenutno koriste za zaslon
displayio.release_displays()

# Postavite zaslon
display = ili9341.ILI9341(
    board.SPI(),
    cs=digitalio.DigitalInOut(board.LCD_CS),
    dc=digitalio.DigitalInOut(board.LCD_DC),
    rotation=0
)

# Ispunite zaslon bojom
display.fill(0x000000)

# Izradite dodirni kontroler
touch = xpt2046_circuitpython.Touch(
    board.SPI(), 
    cs = digitalio.DigitalInOut(board.TOUCH_CS)
)

while(True):
    # Dobite koordinate za ovaj dodir
    x, y = touch.get_coordinates()
    # Provjerite jesu li kooordinate valjane
    if x is not None and y is not None:
        display.fill_rectangle(x, y, 3, 3, 0x0000FF)
        print("Dodir na:", x, y)
    
    time.sleep(0.1)