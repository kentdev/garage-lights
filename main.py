from machine import Pin, Timer

LED_PIN = 25

led = Pin(LED_PIN, Pin.OUT)
t = Timer()

def blink(timer:Timer):
    global led
    if led.value():
        led.off()
    else:
        led.on()

t.init(mode=Timer.PERIODIC, period=250, callback=blink)

