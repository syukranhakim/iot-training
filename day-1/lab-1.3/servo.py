# This script demonstrate how to control
# servo motor using Raspberry Pi

import RPi.GPIO as GPIO
import time

SERVO_PIN = 17  # GPIO17

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set PWM frequency to 50 Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)


def set_angle(angle):
    # Convert angle to duty cycle
    duty = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    # Stop sending pulse
    pwm.ChangeDutyCycle(0) 


def main():
    try:
        set_angle(0)
        set_angle(90)
        set_angle(180)
    finally:
        pwm.stop()
        GPIO.cleanup()

    return

if __name__ == "__main__":
    main()
