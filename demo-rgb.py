import machine

led_r = machine.PWM(machine.Pin(15, machine.Pin.OUT), freq=1000, duty=0)
led_g = machine.PWM(machine.Pin(12, machine.Pin.OUT), freq=1000, duty=0)
led_b = machine.PWM(machine.Pin(13, machine.Pin.OUT), freq=1000, duty=0)

button = machine.Pin(4, machine.Pin.IN)
photo = machine.ADC(0)
