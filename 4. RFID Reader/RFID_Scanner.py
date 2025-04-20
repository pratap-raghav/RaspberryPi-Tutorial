import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led_pin = 13
GPIO.setup(led_pin, GPIO.OUT)
reader = SimpleMFRC522()

try:
    print("Scan your RFID tag...")
    while True:
        tag_id, tag_text = reader.read()
        print(f"RFID Tag ID: {tag_id}")
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(led_pin, GPIO.LOW)
        print("Scan again...")

except KeyboardInterrupt:
    print("Exiting program...")
    GPIO.cleanup()
