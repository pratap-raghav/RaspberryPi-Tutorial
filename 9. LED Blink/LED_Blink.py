from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time

lcd = CharLCD('PCF8574', 0x27)

GPIO.setwarnings(False)

led_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('LED Blink')
    lcd.cursor_pos = (2, 0)
    lcd.write_string('LED - ON')
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(1)

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('LED Blink')
    lcd.cursor_pos = (2, 0)
    lcd.write_string('LED - OFF')
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(1)
