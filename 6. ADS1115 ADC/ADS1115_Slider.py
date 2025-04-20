import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from RPLCD.i2c import CharLCD

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

lcd = CharLCD('PCF8574', 0x27)

ADC_MAX = 32767

while True:
    sensor_value = AnalogIn(ads, ADS.P0).value
    percentage = int((sensor_value / ADC_MAX) * 100)
    slider_blocks = int((percentage / 10))
    slider = "[" + ("#" * slider_blocks).ljust(10) + "]"

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("ADS1115 Analog Value\n")
    lcd.cursor_pos = (2, 0)
    lcd.write_string(f"Slider: {percentage}%\n")
    lcd.cursor_pos = (3, 0)
    lcd.write_string(slider)

    time.sleep(1)
