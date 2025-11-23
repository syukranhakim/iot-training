# This script demonstrate how to turn on LED using switch
# on Raspberry Pi

import RPi.GPIO as GPIO
import time

# Pin setup
LED_PIN = 18       # GPIO pin connected to LED
SWITCH_PIN = 23    # GPIO pin connected to switch

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # internal pull-up


def main():
    try:
        while True:
            if GPIO.input(SWITCH_PIN) == GPIO.LOW:  # Switch pressed
                GPIO.output(LED_PIN, True)
                print("Switch Pressed")
            else:
                GPIO.output(LED_PIN, False)
            time.sleep(0.1)

    finally:
        GPIO.cleanup()

    return

if __name__ == "__main__":
    main()
