import time

import machine

# Pin D1 is mapped to GPIO 5
ledPin = machine.Pin(5, machine.Pin.OUT)

while True:
    ledPin.on()
    print("LED is on")
    time.sleep(2.0)

    ledPin.off()
    print("LED is off")
    time.sleep(2.0)
