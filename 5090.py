import board
import digitalio
import time

Led = digitalio.DigitalInOut(board.GPIO2)
Led.direction = digitalio.Direction.OUTPUT


# 🔔 Zvoni za početak sata (3 kratka bljeska)
Led.value = True
time.sleep(0.5)
Led.value = False
time.sleep(0.5)

Led.value = True
time.sleep(0.5)
Led.value = False
time.sleep(0.5)

Led.value = True
time.sleep(0.5)
Led.value = False
time.sleep(1)


# 🚶 Učitelj dolazi u učionicu (LED upaljena kratko)
Led.value = True
time.sleep(2)
Led.value = False
time.sleep(0.5)


# 🖊️ Učitelj piše na ploču (kratko, kratko, dugo)

Led.value = True
time.sleep(0.5)
Led.value = False
time.sleep(0.5)

Led.value = True
time.sleep(0.5)
Led.value = False
time.sleep(0.5)

Led.value = True
time.sleep(2)
Led.value = False
time.sleep(1)


# 📓 Učenici pišu u bilježnicu (svijetli dulje vremena)
Led.value = True
time.sleep(4)
Led.value = False
time.sleep(1)


# 🔔 Zvoni za kraj sata (2 kratka bljeska)
Led.value = True
time.sleep(0.5)
Led.value = False
time.sleep(0.5)

Led.value = True
time.sleep(0.5)

# 🚪 Učitelj odlazi iz učionice (LED se ugasi)
Led.value = False