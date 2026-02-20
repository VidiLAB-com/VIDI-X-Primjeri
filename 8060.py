from adafruit_ili9341 import ILI9341 
from adafruit_display_text import label 
from adafruit_display_shapes.rect import Rect 
from adafruit_display_shapes.roundrect import RoundRect 
import adafruit_rgb_display.ili9341 as ili9341
import xpt2046_circuitpython 
import board 
import displayio 
import analogio 
import time 
import terminalio 
import digitalio 
import simpleio 

score = 0        # Broj bodova
level = 1        # Trenutna razina
questionText = ""  # Tekst pitanja
a = ""           # Odgovor A
b = ""           # Odgovor B
c = ""           # Odgovor C
d = ""           # Odgovor D

displayio.release_displays()

PIEZO_PIN = board.GPIO25

led = digitalio.DigitalInOut(board.STATUS)  
led.direction = digitalio.Direction.OUTPUT

touch = xpt2046_circuitpython.Touch(
    board.SPI(), 
    cs = digitalio.DigitalInOut(board.TOUCH_CS),
)

spi = board.SPI()  
tft_cs = board.LCD_CS
tft_dc = board.LCD_DC
tft_rst = None  

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

display = ILI9341(display_bus, width=320, height=240, rotation=180)

splash = displayio.Group()
display.root_group = splash
color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000 # Define black as the background color
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite) 