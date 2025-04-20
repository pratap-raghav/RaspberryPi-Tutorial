import smbus
import time
from datetime import datetime
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)

bus = smbus.SMBus(1)
rtc_address = 0x68

lcd.clear()
lcd.write_string("RTC Clock Ready")


def dec_to_bcd(value):
    return (value // 10) * 16 + (value % 10)


def set_time():
    now = datetime.now()
    seconds = dec_to_bcd(now.second)
    minutes = dec_to_bcd(now.minute)
    hours = dec_to_bcd(now.hour)
    day = dec_to_bcd(now.day)
    month = dec_to_bcd(now.month)
    year = dec_to_bcd(now.year - 2000)
    weekday = dec_to_bcd(now.isoweekday())

    data = [seconds, minutes, hours, weekday, day, month, year]
    bus.write_i2c_block_data(rtc_address, 0x00, data)
    print(f"RTC Time Set to: {now.strftime('%Y-%m-%d %H:%M:%S')} | Day of the week: {now.strftime('%A')}")


def bcd_to_dec(value):
    return (value // 16) * 10 + (value % 16)


def read_time():
    data = bus.read_i2c_block_data(rtc_address, 0x00, 7)
    seconds = bcd_to_dec(data[0])
    minutes = bcd_to_dec(data[1])
    hours = bcd_to_dec(data[2])
    weekday = bcd_to_dec(data[3])
    day = bcd_to_dec(data[4])
    month = bcd_to_dec(data[5])
    year = bcd_to_dec(data[6]) + 2000

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(
        f"RTC Time: {year}-{month:02d}-{day:02d} {hours:02d}:{minutes:02d}:{seconds:02d} | Day: {weekdays[weekday - 1]}")

    lcd.clear()

    lcd.cursor_pos = (0, 0)
    lcd.write_string(f'RTC DS3231')

    lcd.cursor_pos = (1, 0)
    lcd.write_string(f'{year}-{month:02d}-{day:02d}')

    lcd.cursor_pos = (2, 0)
    lcd.write_string(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

    lcd.cursor_pos = (3, 0)
    lcd.write_string(f"Day: {weekdays[weekday - 1]}")


while True:
    read_time()
    time.sleep(1)
