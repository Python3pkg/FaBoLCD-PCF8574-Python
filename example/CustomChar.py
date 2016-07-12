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

heart=[
    0b00000,
    0b01010,
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b00100
]

smiley = [
    0b00000,
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b01110,
    0b00000
]

frownie = [
    0b00000,
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b00000,
    0b01110,
    0b10001
]

armsDown = [
    0b00100,
    0b01010,
    0b00100,
    0b01110,
    0b10101,
    0b00100,
    0b01010,
    0b10001
]

armsUp = [
    0b00100,
    0b01010,
    0b10101,
    0b01110,
    0b00100,
    0b00100,
    0b01010,
    0b10001
]

lcd = FaBoLCD_PCF8574.PCF8574()

lcd.write("Cusoum Character")

lcd.createChar(0, heart)
lcd.createChar(1, smiley)
lcd.createChar(2, frownie)
lcd.createChar(3, armsDown)
lcd.createChar(4, armsUp)

i = 0

try:
    while True:

        lcd.setCursor(5,1)
        lcd.writeCreateChar(0)
        lcd.write(" ")
        lcd.writeCreateChar(1+i)
        lcd.write(" ")
        lcd.writeCreateChar(3+i)

        i = 1 - i
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
