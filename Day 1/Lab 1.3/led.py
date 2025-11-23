import RPi.GPIO as GPIO
import time


def main():
    LED_PIN = 17  # GPIO17

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
    time.sleep(5)                     # Keep it on for 5 seconds
    GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off

    GPIO.cleanup()

    return

if __name__ == "__main__":
    main()
