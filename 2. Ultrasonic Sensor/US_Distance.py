import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)

lcd.clear()

lcd.cursor_pos = (0, 0)
lcd.write_string(f'Ultrasonic Distance')
lcd.cursor_pos = (1, 0)
lcd.write_string(f'Measurement')

GPIO.setwarnings(False)

trigger_pin = 23
echo_pin = 24
led_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)


def get_distance():
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    while GPIO.input(echo_pin) == 0:
        start_time = time.time()

    while GPIO.input(echo_pin) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2
    return round(distance, 2)


try:
    while True:
        distance = get_distance()
        lcd.clear()

        lcd.cursor_pos = (0, 0)
        lcd.write_string(f'Ultrasonic Distance')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(f'Measurement')

        lcd.cursor_pos = (3, 0)
        lcd.write_string(f'Distance: {distance} cm')

        if 10 < distance < 35:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)

        time.sleep(0.5)

except Exception as e:
    print(f"Error: {e}")

finally:
    GPIO.cleanup()
