<h1> Led Bar </h1>
<h3>Um array feito em python, para 10 leds ligarem e desligarem simultaneamente</h3>
<br>
<hr>
Link do Wokwi: <br>
https://wokwi.com/projects/373877550709754881](https://wokwi.com/projects/373245173893432321)
<hr>

 <h3> Código: </h3>
 
from machine import Pin <br>
import utime <br> 

leds = [28,27,26,22,21,20,19,18,17,16] <br>



leds[0] = Pin(28,Pin.OUT)<br>
leds[1] = Pin(27,Pin.OUT)<br>
leds[2] = Pin(26,Pin.OUT)<br>
leds[3] = Pin(22,Pin.OUT)<br>
leds[4] = Pin(21,Pin.OUT)<br>
leds[5] = Pin(20,Pin.OUT)<br>
leds[6] = Pin(19,Pin.OUT)<br>
leds[7] = Pin(18,Pin.OUT)<br>
leds[8] = Pin(17,Pin.OUT)<br>
leds[9] = Pin(16,Pin.OUT)<br>

while True:<br>
  leds[0].value(1)<br>
  leds[1].value(1)<br>
  leds[2].value(1)<br>
  leds[3].value(1)<br>
  leds[4].value(1)<br>
  leds[5].value(1)<br>
  leds[6].value(1)<br>
  leds[7].value(1)<br>
  leds[8].value(1)<br>
  leds[9].value(1)<br>
  utime.sleep(1)<br>
  leds[0].value(0)<br>
  leds[1].value(0)<br>
  leds[2].value(0)<br>
  leds[3].value(0)<br>
  leds[4].value(0)<br>
  leds[5].value(0)<br>
  leds[6].value(0)<br>
  leds[7].value(0)<br>
  leds[8].value(0)<br>
  leds[9].value(0)<br>
  utime.sleep(1)<br>



