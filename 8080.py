import board
import displayio
import analogio
import time
import terminalio
import digitalio
import simpleio
import adafruit_rgb_display.ili9341 as ili9341
import xpt2046_circuitpython
from adafruit_ili9341 import ILI9341
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.roundrect import RoundRect

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

# Početni pravokutnik
rect = Rect(0, 0, 320, 20, outline=0x0000FF)
splash.append(rect)

# Razina tekst
text_groupL = displayio.Group(scale=2, x=5, y=10)
text = "Razina: " + str(level)
text_areaL = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_groupL.append(text_areaL)
splash.append(text_groupL)

# Rezultat tekst
text_groupS = displayio.Group(scale=2, x=220, y=10)
text = "Rezultat: " + str(score)
text_areaS = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_groupS.append(text_areaS)
splash.append(text_groupS)

# Tekst pitanja
text_groupQ = displayio.Group(scale=1, x=10, y=30)
text = str(level) + "." + questionText
text_areaQ = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_groupQ.append(text_areaQ)
splash.append(text_groupQ)

# okvir A
roundrectA = RoundRect(80, 50, 150, 50, 5, outline=0x0000FF)
splash.append(roundrectA)
text_groupA = displayio.Group(scale=1, x=90, y=75)
text = "A: "+ str(a)
text_areaA = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_groupA.append(text_areaA)
splash.append(text_groupA)

# okvir B
roundrectB = RoundRect(5, 115, 150, 50, 5, outline=0x0000FF)
splash.append(roundrectB)
text_groupB = displayio.Group(scale=1, x=15, y=140)
text = "B: "+ str(b)
text_areaB = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_groupB.append(text_areaB)
splash.append(text_groupB)

# okvir C
roundrectC = RoundRect(165, 115, 150, 50, 5, outline=0x0000FF)
splash.append(roundrectC)
text_groupC = displayio.Group(scale=1, x=175, y=140)
text = "C: "+ str(c)
text_areaC = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_groupC.append(text_areaC)
splash.append(text_groupC)

# okvir D
roundrectD = RoundRect(80, 180, 150, 50, 5, outline=0x0000FF)
splash.append(roundrectD)
text_groupD = displayio.Group(scale=1, x=90, y=205)
text = "D: "+ str(d)
text_areaD = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_groupD.append(text_areaD)
splash.append(text_groupD)


def menu(questionText, a, b, c, d, correctAnswer):
    roundrectA.outline = 0x0000FF
    roundrectB.outline = 0x0000FF
    roundrectC.outline = 0x0000FF
    roundrectD.outline = 0x0000FF
    text_areaL.text = "Razina: " + str(level)
    text_areaS.text = "Rezultat: " + str(score)
    text_areaQ.text = str(level) + "." + questionText
    text_areaA.text = "A: "+ str(a)
    text_areaB.text = "B: "+ str(b)
    text_areaC.text = "C: "+ str(c)
    text_areaD.text = "D: "+ str(d)
    checkTouchInput(correctAnswer)
    checkButtonInput(correctAnswer)

def correct():
    global score
    global level
    score += 1 
    led.value = True
    time.sleep(0.5)
    led.value = False
    correctAnwserSound()
    level += 1
    

def wrong():
    global level
    wrongAnwserSound()
    level += 1
    
def clearScreen():
    while len(splash) > 0:
        splash.pop()
        
def correctAnwserSound():
    simpleio.tone(PIEZO_PIN, 200, duration=0.2)
    simpleio.tone(PIEZO_PIN, 500, duration=0.5)

def wrongAnwserSound():
    simpleio.tone(PIEZO_PIN, 1000, duration=0.2)
    simpleio.tone(PIEZO_PIN, 500, duration=0.2)
    simpleio.tone(PIEZO_PIN, 200, duration=0.5)

def gameOverSound():
    simpleio.tone(PIEZO_PIN, 1000, duration=0.2)
    simpleio.tone(PIEZO_PIN, 500, duration=0.2)
    simpleio.tone(PIEZO_PIN, 1000, duration=0.5)
    simpleio.tone(PIEZO_PIN, 2000, duration=0.5)
    for i in range(4000, 0, -40):
        simpleio.tone(PIEZO_PIN, i, duration=0.01)

def checkButtonInput(correctAnwser):
    with analogio.AnalogIn(board.BTN_L_R) as analog_pin:
        analog_value = analog_pin.value
        if analog_value > 30000 and analog_value < 60000: # BUTTON RIGHT
            if correctAnwser == "C":
                roundrectC.outline = 0x00FF00
                correct()
            else:
                roundrectC.outline = 0xFF0000
                wrong()
        elif analog_value > 60000: # BUTTON LEFT
            if correctAnwser == "B":
                roundrectB.outline = 0x00FF00
                correct()
            else:
                roundrectB.outline = 0xFF0000
                wrong()
    with analogio.AnalogIn(board.BTN_UP_DOWN) as analog_pin:
        analog_value = analog_pin.value
        if analog_value >30000 and analog_value < 60000: # BUTTON DOWN
            if correctAnwser == "D":
                roundrectD.outline = 0x00FF00
                correct()
            else:
                roundrectD.outline = 0xFF0000
                wrong()
        elif analog_value > 60000: # BUTTON UP
            if correctAnwser == "A":
                roundrectA.outline = 0x00FF00
                correct()
            else:
                roundrectA.outline = 0xFF0000
                wrong()
                
def checkTouchInput(correctAnswer):
    x, y = touch.get_coordinates()
    if x is not None and y is not None:
        if x >= 60 and y >= 100 and x <= 100 and y<= 238:
            if correctAnswer == "A":
                roundrectA.outline = 0x00FF00
                correct()
            else:
                roundrectA.outline = 0xFF0000
                wrong()
        elif x >= 115 and y >= 170 and x <= 160 and y <= 310:
            if correctAnswer == "B":
                roundrectB.outline = 0x00FF00
                correct()
            else:
                roundrectB.outline = 0xFF0000
                wrong()
        elif x >= 115 and y >= 10 and x <= 160 and y<= 150:
            if correctAnswer == "C":
                roundrectC.outline = 0x00FF00
                correct()
            else:
                roundrectC.outline = 0xFF0000
                wrong()
        elif x >= 185 and y >= 100 and x <= 230 and y<= 238:
            if correctAnswer == "D":
                roundrectD.outline = 0x00FF00
                correct()
            else:
                roundrectD.outline = 0xFF0000
                wrong()

def endGame():
    global level
    global score
    clearScreen()
    text_group = displayio.Group(scale=2, x=40, y=80)
    text = "Tvoj rezultat: " + str(score) + "/6"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
    text_group.append(text_area)
    splash.append(text_group)
    text_group = displayio.Group(scale=1, x=40, y=100)
    if score <= 2:
        poruka = "Pokusaj ponovno."
    elif score <= 4:
        poruka = "Nije lose, ali mozes i bolje :)"
    else:
        poruka = "Ti si pravi znalac!"
    text_area = label.Label(terminalio.FONT, text=poruka, color=0xFFFFFF)
    text_group.append(text_area)
    splash.append(text_group)
    gameOverSound()
    level = 1

while True:
    if level == 1:
        menu("Koliko je 2 +2?", 2, 3, 4, 5, "C")
    elif level == 2:
        menu("U formuli F=ma što oznacava m?", "Masu","Akceleraciju","Silu","Brzinu","A")
    elif level == 3:
        menu("Voda se sastoji od kisika i?", "Zlata","Vodika","Ugljika","Bakra","B")
    elif level == 4:
        menu("Sto je \"mozak\" racunala?","GPU", "Memorija", "Disk", "CPU", "D")
    elif level == 5:
        menu("Pitanje 5","odgovor 1", "odgovor 2", "odgovor 3", "odgovor 4", "D")
    elif level == 6:
        menu("Pitanje 6","odgovor 1", "odgovor 2", "odgovor 3", "odgovor 4", "D")
    else:
        endGame()
    time.sleep(0.05)