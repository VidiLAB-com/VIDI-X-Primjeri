import board
import displayio
import time
import terminalio
import digitalio
from adafruit_ili9341 import ILI9341
from adafruit_display_text import label
import xpt2046_circuitpython

led = digitalio.DigitalInOut(board.STATUS)
led.direction = digitalio.Direction.OUTPUT

# Oslobodite sve resurse koji se trenutno koriste za zaslon
displayio.release_displays()

# Definiraj SPI sabirnicu i pinove zaslona
spi = board.SPI() 
tft_cs = board.LCD_CS
tft_dc = board.LCD_DC
tft_rst = None  

# Izradite sabirnicu zaslona
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

# Definirajte parametre zaslona
display = ILI9341(display_bus, width=320, height=240, rotation=180)

# Napravite grupu za prikaz
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Izradite dodirni kontroler
touch = xpt2046_circuitpython.Touch(
    board.SPI(), 
    cs = digitalio.DigitalInOut(board.TOUCH_CS),
)
def displayText(text, color):
    text_group = displayio.Group(scale=2, x=5, y=20)
    text_area = label.Label(terminalio.FONT, text=text, color=color)
    text_group.append(text_area)
    splash.append(text_group)

def clearScreen():
    while len(splash) > 0:
        splash.pop()

while True:
    x, y = touch.get_coordinates()

    if x is not None and y is not None:
        displayText("Dodirnuto", 0xFFFF00)
        led.value = True
    else:
        clearScreen()
        led.value = False

    time.sleep(0.1)