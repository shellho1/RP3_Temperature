
# Raspberry Pi 3 Temperature / Humidity Monitor

Python script that uses the DHT22/AM2302 to poll for temperature and humidity. The median of the polled data is then displayed on a 16x2 CharLCD and recorded to a CSV file for later analysis.

## Important Info

The sensor is only accurate to +/- 2% humidity and +/- 0.5 celsius. Readings can very even more if the sensor is polled more than every two seconds due to the sensor heating up and subsequently squelching the humidity. To counteract this, the sensor is polled 10 times every three seconds and the median values of the recorded data are recorded. 

During this project issues with the backlight and contrast of the CharLCD were also prevalent. To counteract this two 10KΩ potentiometers were used to vary the backlight and contrast. 

Occasionally the CharLCD will become overrun with random characters if the wires are bumped. A short script called "fix.py" clears the LCD and resets the configuration.


