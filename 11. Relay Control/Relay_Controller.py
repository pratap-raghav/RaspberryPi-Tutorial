import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

relay1_pin = 26
relay2_pin = 27
button1_pin = 23
button2_pin = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(relay2_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lcd = CharLCD('PCF8574', 0x27)

relay1_state = False
relay2_state = False

def update_display():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Relay Controller\n")
    lcd.cursor_pos = (2, 0)
    lcd.write_string(f"Relay 1: {'ON' if relay1_state else 'OFF'}\n")
    lcd.cursor_pos = (3, 0)
    lcd.write_string(f"Relay 2: {'ON' if relay2_state else 'OFF'}")

try:
    update_display()
    while True:
        if GPIO.input(button1_pin) == GPIO.LOW:
            relay1_state = not relay1_state
            GPIO.output(relay1_pin, relay1_state)
            update_display()
            time.sleep(0.3)

        if GPIO.input(button2_pin) == GPIO.LOW:
            relay2_state = not relay2_state
            GPIO.output(relay2_pin, relay2_state)
            update_display()
            time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()
    lcd.clear()
    print("Program Stopped")
