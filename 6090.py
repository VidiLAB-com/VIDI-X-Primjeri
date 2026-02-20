import time
import board
import digitalio

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT

kratko = 0.5
dugo = 2
kreni = 4

boja = 1   # 1 = crveno, 2 = zeleno

if boja == 1:
    # 🔴 CRVENO – stani
    Led.value = True
    time.sleep(dugo)

    # 🟡 PRIPREMA – 2 bljeska
    brojac = 1
    while brojac <= 2:
        Led.value = False
        time.sleep(kratko)
        Led.value = True
        time.sleep(kratko)
        brojac = brojac + 1

    boja = 2   # mijenjamo u zeleno

else:
    # 🟢 ZELENO – kreni
    Led.value = True
    time.sleep(kreni)

    # ⏳ ZELENO uskoro završava – 3 brza bljeska
    brojac = 1
    while brojac <= 3:
        Led.value = False
        time.sleep(kratko)
        Led.value = True
        time.sleep(kratko)
        brojac = brojac + 1

    # 🔴 opet crveno – stani
    Led.value = False