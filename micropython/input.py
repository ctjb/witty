import machine
import time

led_r = machine.PWM(machine.Pin(15, machine.Pin.OUT), freq=1000, duty=0)
led_g = machine.PWM(machine.Pin(13, machine.Pin.OUT), freq=1000, duty=0)
led_b = machine.PWM(machine.Pin(12, machine.Pin.OUT), freq=1000, duty=0)

button = machine.Pin(4, machine.Pin.IN)
photo = machine.ADC(0)

which = 0

while True:
    light = photo.read()
    if button.value() == 0 or light < 700:
        led_r.duty( 1023 if which == 0 else 0 )
        led_g.duty( 1023 if which == 1 else 0 )
        led_b.duty( 1023 if which == 2 else 0 )
        which = (which + 1) % 3
        time.sleep(0.3)
