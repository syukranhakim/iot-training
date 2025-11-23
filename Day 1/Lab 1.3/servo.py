import RPi.GPIO as GPIO
import time

SERVO_PIN = 17  # GPIO17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz
pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle / 18)  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)  # Stop sending pulse

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
