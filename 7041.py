import board
import displayio
import digitalio
import time
import terminalio
from adafruit_display_text import label
from adafruit_ili9341 import ILI9341
import xpt2046_circuitpython


displayio.release_displays()

# SPI i zaslon
spi = board.SPI()
display_bus = displayio.FourWire(
spi,
command=board.LCD_DC,
chip_select=board.LCD_CS
)

display = ILI9341(display_bus, width=320, height=240, rotation=0)

group = displayio.Group()
display.root_group = group

# Pozadina
bg_bitmap = displayio.Bitmap(320, 240, 1)
bg_palette = displayio.Palette(1)
bg_palette[0] = 0x000000
bg = displayio.TileGrid(bg_bitmap, pixel_shader=bg_palette)
group.append(bg)

# Dodir
touch = xpt2046_circuitpython.Touch(
board.SPI(),
cs=digitalio.DigitalInOut(board.TOUCH_CS)
)

while True:
    x, y = touch.get_coordinates()

    if x is not None and y is not None:
        print("Dodir:", x, y)

        text = label.Label(
        terminalio.FONT,
        text="TU!",
        color=0xFFFFFF
        )
        text.x = x
        text.y = y
        
        group.append(text)
        
        time.sleep(1)