import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

sensor_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

lcd = CharLCD('PCF8574', 0x27)

def update_lcd(status_text):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Proximity Sensor")
    lcd.cursor_pos = (2, 0)
    lcd.write_string("Status:")
    lcd.cursor_pos = (3, 0)
    lcd.write_string(status_text)

try:
    while True:
        is_object_detected = GPIO.input(sensor_pin)
        status_text = "Object Detected" if is_object_detected == GPIO.HIGH else "No Object"
        update_lcd(status_text)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    lcd.clear()
    print("Program Stopped")
