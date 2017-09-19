#!/usr/bin/env python
from RPLCD import CharLCD

lcd = CharLCD(cols=16,rows=2, pin_rs=37, pin_e=35, pins_data=[33,31,29,223])
lcd.clear()
lcd.close(clear=True)
