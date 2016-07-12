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

i = 0
lcd = FaBoLCD_PCF8574.PCF8574()

thisChar = ord('a')

lcd.cursor()

try:
    while True:
        char = chr(thisChar)
        if char == 'j':
            lcd.rightToLeft()

        if char == 's':
            lcd.leftToRight()

        if thisChar > ord('z'):
            lcd.home()
            char = 'a'
            thisChar = ord(char)

        lcd.write(char)

        time.sleep(0.5)
        thisChar += 1

except KeyboardInterrupt:
    sys.exit()
