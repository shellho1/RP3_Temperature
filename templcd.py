#!/usr/bin/env python
import sys
import csv
import Adafruit_DHT
import RPi.GPIO as GPIO
import csv
from datetime import datetime
from time import sleep
from RPLCD import CharLCD

def main():
	# initialize lcd screen
	lcd = CharLCD(cols=16,rows=2, pin_rs=37, pin_e=35, pins_data = [33,31,29,23])

	# DHT22 sensor is only accurate to +/- 2% humidity and +/- 0.5 celsius
	# Poll 10 times and calculate median to get more accurate value
	templist = []
	humidlist = []

	lcd.cursor_pos = (0,0)
	lcd.write_string("Polling...")
	lcd.cursor_pos = (1,0)
	bar = "[----------]"
	lcd.write_string(bar)
	lcd.clear()

	for i in range(1,11):
		data = poll()

		lcd.cursor_pos = (0,0)
		lcd.write_string("Polling....")
		lcd.cursor_pos = (1,0)
		
		bar = list(bar)
		bar[i] = '#'
		bar = ''.join(bar)
		lcd.write_string(bar)
 
		# Don't poll more often than every 2 seconds
		sleep(3)
		lcd.clear() 
		temp = int(round(data[0]))
		humid = int(round(data[1]))
		templist.append(temp)
		humidlist.append(humid)

	lcd.clear()
	
	# Calculate median value
	temp = (sorted(templist))[5]
	humid = (sorted(humidlist))[5]
	
	# Display results to LCD
	display(lcd, temp, humid)

	# Write data to CSV file for later analysis
	write_data(temp,humid)
	
	# Clears the screen / resets cursor position and closes connection
	lcd.clear()
	lcd.close(clear=True)	

def poll():
	try:
		# Poll data and convert to temp and fahrenheit 
		humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,18)
		temperature = temperature * 9/5.0 + 32
		print("Temp: %d F" % temperature)
		print("Humidity: %d %%" % humidity)
		data = [temperature, humidity]
		return data

	except KeyboardInterrupt:
		print("Keyboard interrupt detected. Exiting program...")

def display(lcd, temp, humid):
	try:
		# Sets LCD screen cursor to top line and write temp
		lcd.cursor_pos = (0,0)
		lcd.write_string("Temperature: %d F" % temp)

		# Sets LCD screen cursor to bottom line and write humidity
		lcd.cursor_pos = (1,0)
		lcd.write_string("Humidity: %d %%" % humid)

		# Display for 5 seconds
		sleep(5)
	
	except KeyboardInterrupt:
		print("Keyboard interrupt detected. Exiting program...")

	finally:
		# Clear screen when finished
		lcd.clear()

def write_data(temp, humid):
	# Opens/creates CSV file and appends data with current time
	with open('data.csv', 'a+') as csvfile:
		writer = csv.writer(csvfile, delimiter='|')
		writer.writerow([str(datetime.now())] + [temp] + [humid])
	
main()
