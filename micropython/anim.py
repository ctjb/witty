import machine
import time
import math

led_r = machine.PWM(machine.Pin(15, machine.Pin.OUT), freq=1000, duty=0)
led_g = machine.PWM(machine.Pin(13, machine.Pin.OUT), freq=1000, duty=0)
led_b = machine.PWM(machine.Pin(12, machine.Pin.OUT), freq=1000, duty=0)

button = machine.Pin(4, machine.Pin.IN)
photo = machine.ADC(0)

t = 0

while True:
    # read button and photoresistor states
    print('button:', button.value(), 'photo:', photo.read())
    # set led colors
    led_r.duty( int(math.cos(0.3 * t) * 450 + 500) )
    led_g.duty( int(math.cos(0.5 * t) * 450 + 500) )
    led_b.duty( int(math.cos(0.7 * t) * 450 + 500) )
    # wait 10 ms
    time.sleep(0.01)
    t += 0.01
