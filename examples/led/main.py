import time

import machine

SLEEP = 1.0

# Pin D1 is mapped to GPIO 5
ledPin = machine.Pin(5, machine.Pin.OUT)

while True:
    ledPin.on()
    print("LED is on")
    time.sleep(SLEEP)

    ledPin.off()
    print("LED is off")
    time.sleep(SLEEP)
