import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)

GPIO.setwarnings(False)

led_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

reader = SimpleMFRC522()

try:
    print("Place your RFID card/tag near the reader...")
    while True:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(f'RFID Authentication')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(f'System')

        lcd.cursor_pos = (3, 0)
        lcd.write_string(f'Please scan ID')

        tag_id, tag_text = reader.read()
        print(f"RFID UID: {tag_id}")
        print(f"Card Data: {tag_text.strip()}")
        if tag_id == 166835356500:
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f'RFID Authentication')
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f'System')
            lcd.cursor_pos = (2, 0)
            lcd.write_string(f'Authorised: ')
            lcd.cursor_pos = (3, 0)
            lcd.write_string(f'Door Open')
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(led_pin, GPIO.LOW)
        else:
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f'RFID Authentication')
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f'System')
            lcd.cursor_pos = (2, 0)
            lcd.write_string(f'Not Authorised')
            time.sleep(2)

except KeyboardInterrupt:
    print("\nStopping...")
    GPIO.cleanup()
