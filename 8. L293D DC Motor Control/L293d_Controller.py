import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

GPIO.setwarnings(False)

pwm_pin = 18
dir_pin1 = 23
dir_pin2 = 24
button_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(dir_pin1, GPIO.OUT)
GPIO.setup(dir_pin2, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lcd = CharLCD('PCF8574', 0x27)

pwm = GPIO.PWM(pwm_pin, 1000)
pwm.start(50)

def set_motor_direction(direction):
    if direction == 0:
        GPIO.output(dir_pin1, GPIO.HIGH)
        GPIO.output(dir_pin2, GPIO.LOW)
        return "Clockwise"
    else:
        GPIO.output(dir_pin1, GPIO.LOW)
        GPIO.output(dir_pin2, GPIO.HIGH)
        return "Anti-Clockwise"

try:
    while True:
        motor_dir = GPIO.input(button_pin)
        direction_label = set_motor_direction(motor_dir)

        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Motor Control\n")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Speed: 50%\n")
        lcd.cursor_pos = (2, 0)
        lcd.write_string("Direction:")
        lcd.cursor_pos = (3, 0)
        lcd.write_string(f"{direction_label}")

        time.sleep(0.5)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    lcd.clear()
    print("Program Stopped")
