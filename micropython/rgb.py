import machine
import time

led_r = machine.PWM(machine.Pin(15, machine.Pin.OUT), freq=1000, duty=0)
led_g = machine.PWM(machine.Pin(13, machine.Pin.OUT), freq=1000, duty=0)
led_b = machine.PWM(machine.Pin(12, machine.Pin.OUT), freq=1000, duty=0)

while True:
    led_r.duty(1023)
    led_g.duty(0)
    led_b.duty(0)
    time.sleep(1)

    led_r.duty(0)
    led_g.duty(1023)
    led_b.duty(0)
    time.sleep(1)

    led_r.duty(0)
    led_g.duty(0)
    led_b.duty(1023)
    time.sleep(1)
