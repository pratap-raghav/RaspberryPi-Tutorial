import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)

GPIO.setwarnings(False)

touch_pin = 17
led_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string('Capacitive Touch')
        lcd.cursor_pos = (1, 0)
        lcd.write_string('Sensor')

        if GPIO.input(touch_pin) == 0:
            GPIO.output(led_pin, GPIO.HIGH)
            lcd.cursor_pos = (3, 0)
            lcd.write_string('Touch detected!')
        else:
            GPIO.output(led_pin, GPIO.LOW)
            lcd.cursor_pos = (3, 0)
            lcd.write_string('No touch detected!')

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
