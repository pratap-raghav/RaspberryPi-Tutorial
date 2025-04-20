import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

servo_pwm = GPIO.PWM(servo_pin, 50)
servo_pwm.start(0)

lcd = CharLCD('PCF8574', 0x27)


def move_servo(angle_deg):
    duty_cycle = (angle_deg / 18) + 2
    GPIO.output(servo_pin, True)
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    servo_pwm.ChangeDutyCycle(0)

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Servo Control")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"Position: {angle_deg}°")


try:
    while True:
        for angle_deg in range(0, 181, 30):
            move_servo(angle_deg)
            time.sleep(1)

        for angle_deg in range(180, -1, -30):
            move_servo(angle_deg)
            time.sleep(1)

except KeyboardInterrupt:
    servo_pwm.stop()
    GPIO.cleanup()
    lcd.clear()
    print("Program Stopped")
