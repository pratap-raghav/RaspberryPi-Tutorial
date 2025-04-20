import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)

GPIO.setwarnings(False)

led_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

ldr_channel = AnalogIn(ads, ADS.P0)

v_ref = 4.096

try:
    while True:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(f'LDR Intensity')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(f'Controller')

        voltage = ldr_channel.voltage
        intensity = (voltage / v_ref) * 100

        print(f"Light Intensity: {100 - intensity:.0f}%")
        lcd.cursor_pos = (3, 0)
        lcd.write_string(f"Light Intensity:{100 - intensity:.0f}%")
        if (100 - intensity) > 50:
            lcd.cursor_pos = (2, 0)
            lcd.write_string(f"Curtain Open")
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            lcd.cursor_pos = (2, 0)
            lcd.write_string(f"Curtain Closed")
            GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting...")
