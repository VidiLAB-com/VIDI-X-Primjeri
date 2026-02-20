import board
import displayio
from adafruit_ili9341 import ILI9341
from adafruit_display_text import label
import terminalio

# Oslobodite sve resurse koji se trenutno koriste za zaslon
displayio.release_displays()

# Definiraj SPI sabirnicu i pinove zaslona
spi = board.SPI()  
tft_cs = board.LCD_CS
tft_dc = board.LCD_DC
tft_rst = None  # Promijeni ovo u None ako tvoj zaslon nema reset pin

# Izradite sabirnicu zaslona
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

# Definirajte parametre zaslona
display = ILI9341(display_bus, width=320, height=240, rotation=180)

splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000  # Crna
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Nacrtajte naljepnicu
text_group = displayio.Group(scale=2, x=57, y=120)
text_area = label.Label(terminalio.FONT, text="Pozdrav od VIDI X-a!", color=0xbd7131)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

# Održite zaslon aktivnim
while True:
    pass