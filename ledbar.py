from machine import Pin
import utime

leds = [28,27,26,22,21,20,19,18,17,16]

leds[0] = Pin(28,Pin.OUT)
leds[1] = Pin(27,Pin.OUT)
leds[2] = Pin(26,Pin.OUT)
leds[3] = Pin(22,Pin.OUT)
leds[4] = Pin(21,Pin.OUT)
leds[5] = Pin(20,Pin.OUT)
leds[6] = Pin(19,Pin.OUT)
leds[7] = Pin(18,Pin.OUT)
leds[8] = Pin(17,Pin.OUT)
leds[9] = Pin(16,Pin.OUT)

while True:
leds[0].value(1)
leds[1].value(1)
leds[2].value(1)
leds[3].value(1)
leds[4].value(1)
leds[5].value(1)
leds[6].value(1)
leds[7].value(1)
leds[8].value(1)
leds[9].value(1)
utime.sleep(1)
leds[0].value(0)
leds[1].value(0)
leds[2].value(0)
leds[3].value(0)
leds[4].value(0)
leds[5].value(0)
leds[6].value(0)
leds[7].value(0)
leds[8].value(0)
leds[9].value(0)
utime.sleep(1)
