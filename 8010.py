import time
import board
import analogio
import board
import displayio
from adafruit_ili9341 import ILI9341
from adafruit_display_text import label
import terminalio

pinTemp = board.TEMP
analog_in = analogio.AnalogIn(pinTemp)

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

# Nacrtajte naljepnicu
text_group = displayio.Group(scale=2, x=5, y=80)
text = "Pozdrav Hrvatska!"
text_area = label.Label(terminalio.FONT, text=text, color=0xbd7131)
text_group.append(text_area)
splash.append(text_group)

# Nacrtajte naljepnicu
text_group = displayio.Group(scale=2, x=5, y=120)
text = "Danas je prekrasan dan"
text_area = label.Label(terminalio.FONT, text=text, color=0xbd7131)
text_group.append(text_area)
splash.append(text_group)

# Nacrtajte naljepnicu
text_group = displayio.Group(scale=2, x=5, y=160)
text = "Temperatura je..."
text_area = label.Label(terminalio.FONT, text=text, color=0xbd7131)
text_group.append(text_area)
splash.append(text_group)

# Nacrtajte naljepnicu
text_group = displayio.Group(scale=2, x=210, y=160)
text_area = label.Label(terminalio.FONT, color=0xbd7131)
text_group.append(text_area)
splash.append(text_group)

ATTENUATION_FACTOR = 0.97  

# Funkcija za pretvaranje očitane vrijednosti senzora u napon
def get_voltage(pin):
    return (pin.value * 3.3) / 65535 * ATTENUATION_FACTOR

# Funkcija za pretvaranje napona u temperaturu
def get_temperature(voltage):
   # MCP9700A ima izlaz od 10mV/°C s pomakom od 500mV na 0°C
    temp = (voltage - 0.5) * 100
    temp = "{:.1f}".format(temp) + " °C"
    return temp
    
while True:
    # Očitajte napon senzora
    voltage = get_voltage(analog_in)
    
    # Pretvori napon u temperaturu
    temp = get_temperature(voltage)
    
    text_area.text = str(temp)
    
    # Pričekajte prije ponovnog očitavanja
    time.sleep(1)