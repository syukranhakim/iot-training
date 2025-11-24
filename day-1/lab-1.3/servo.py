import RPi.GPIO as GPIO
import time

SERVO_PIN = 17  # GPIO17 (physical pin 11)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# 50 Hz PWM -> period = 20 ms
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

# Adjust these if needed after testing
MIN_DUTY = 2.5   # duty cycle for ~0°
MAX_DUTY = 12.5  # duty cycle for ~180°

def set_angle(angle):
    # Limit angle to [0, 180]
    angle = max(0, min(180, angle))

    # Map angle (0–180) to duty (MIN_DUTY–MAX_DUTY)
    duty = MIN_DUTY + (angle / 180.0) * (MAX_DUTY - MIN_DUTY)

    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    # If you want it to keep holding position, comment out the next line
    # pwm.ChangeDutyCycle(0)


def main():
    try:
        print("0°")
        set_angle(0)
        time.sleep(1)

        print("90°")
        set_angle(90)
        time.sleep(1)

        print("180°")
        set_angle(180)
        time.sleep(1)

        print("Back to 0°")
        set_angle(0)
        time.sleep(1)

    finally:
        pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()

