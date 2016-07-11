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

i = 0
lcd = FaBoLCD_PCF8574.PCF8574()

lcd.write("Hello, World!")

while True:
    lcd.setCursor(0,1)
    lcd.write(i)

    i += 1
    time.sleep(0.5)
