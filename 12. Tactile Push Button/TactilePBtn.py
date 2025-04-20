import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)
GPIO.setwarnings(False)

button_pin = 24
led_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string('Tactile Push Button')
        lcd.cursor_pos = (1, 0)
        lcd.write_string('State - ')

        if GPIO.input(button_pin) == 0:
            GPIO.output(led_pin, GPIO.HIGH)
            lcd.cursor_pos = (3, 0)
            lcd.write_string('Button Pressed!')
        else:
            GPIO.output(led_pin, GPIO.LOW)
            lcd.cursor_pos = (3, 0)
            lcd.write_string('Button Not Pressed!')

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
