import time
import board
import busio
from adafruit_ina219 import INA219
from RPLCD.i2c import CharLCD

i2c = busio.I2C(board.SCL, board.SDA)
ina219 = INA219(i2c)
lcd = CharLCD('PCF8574', 0x27)

def update_lcd(voltage, current_ma, power_mw):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("INA219 Readings")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"V: {voltage:.2f} V")
    lcd.cursor_pos = (2, 0)
    lcd.write_string(f"I: {current_ma/1000:.2f} A")
    lcd.cursor_pos = (3, 0)
    lcd.write_string(f"P: {power_mw/1000:.2f} W")

try:
    while True:
        voltage = ina219.bus_voltage
        current_ma = ina219.current
        power_mw = ina219.power

        update_lcd(voltage, current_ma, power_mw)
        time.sleep(1)

except KeyboardInterrupt:
    lcd.clear()
    print("Program Stopped")
