import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from RPLCD.i2c import CharLCD

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

lcd = CharLCD('PCF8574', 0x27)

while True:
    sensor_value_1 = AnalogIn(ads, ADS.P0).value
    sensor_value_2 = AnalogIn(ads, ADS.P1).value
    sensor_value_3 = AnalogIn(ads, ADS.P2).value

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("ADS1115 Analog Value\n")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"Sensor 1 - {sensor_value_1}\n")
    lcd.cursor_pos = (2, 0)
    lcd.write_string(f"Sensor 2 - {sensor_value_2}\n")
    lcd.cursor_pos = (3, 0)
    lcd.write_string(f"Sensor 3 - {sensor_value_3}")

    time.sleep(1)
