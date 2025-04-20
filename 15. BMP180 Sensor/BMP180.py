import time
import board
import busio
import adafruit_bmp280
from RPLCD.i2c import CharLCD

i2c = busio.I2C(board.SCL, board.SDA)
bmp_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)
lcd = CharLCD('PCF8574', 0x27)

def update_lcd(temp_c, pressure_hpa):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("BMP180 Sensor")
    lcd.cursor_pos = (2, 0)
    lcd.write_string(f"T: {temp_c:.2f} C")
    lcd.cursor_pos = (3, 0)
    lcd.write_string(f"P: {pressure_hpa:.2f} hPa")

try:
    while True:
        temp_c = bmp_sensor.temperature
        pressure_hpa = bmp_sensor.pressure

        update_lcd(temp_c, pressure_hpa)
        time.sleep(1)

except KeyboardInterrupt:
    lcd.clear()
    print("Program Stopped")
