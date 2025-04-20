import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from RPLCD.i2c import CharLCD
import math

i2c = busio.I2C(board.SCL, board.SDA)
adc = ADS.ADS1115(i2c)
thermistor_channel = AnalogIn(adc, ADS.P0)
lcd = CharLCD('PCF8574', 0x27)

ref_resistor = 10000
beta_coeff = 3950
t0_kelvin = 298.15

def calculate_temperature():
    v_out = thermistor_channel.voltage
    resistance = ref_resistor * (3.3 / v_out - 1)
    temp_kelvin = 1 / ((1 / t0_kelvin) + (math.log(resistance / ref_resistor) / beta_coeff))
    temp_celsius = temp_kelvin - 273.15
    return temp_celsius

def update_lcd(temp_celsius):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Thermistor Temp")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"T: {temp_celsius:.2f} C")

try:
    while True:
        temperature = calculate_temperature()
        update_lcd(temperature)
        time.sleep(1)

except KeyboardInterrupt:
    lcd.clear()
    print("Program Stopped")
