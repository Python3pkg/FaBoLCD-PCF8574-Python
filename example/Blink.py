# coding: utf-8
## @package FaBoLCD_PCF8574
#  This is a library for the FaBo LCD I2C Brick.
#
#  http://fabo.io/212.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoLCD_PCF8574
import time
import sys

lcd = FaBoLCD_PCF8574.PCF8574()

lcd.write("Blink Test")

i=0

try:
    while True:

        lcd.noBlink()

        lcd.setCursor(0, 1)
        lcd.write(str(i))
        time.sleep(0.5)

        lcd.blink()

        time.sleep(1.5)
        i += 1

except KeyboardInterrupt:
    sys.exit()
