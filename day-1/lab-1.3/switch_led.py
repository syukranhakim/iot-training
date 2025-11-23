import RPi.GPIO as GPIO
import time


SWITCH_PIN = 18  # GPIO18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():

    LED_PIN = 17  # GPIO17

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
    time.sleep(5)                     # Keep it on for 5 seconds
    GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off

    GPIO.cleanup()


    try:
        while True:
            if GPIO.input(SWITCH_PIN) == GPIO.LOW:
                print("Switch pressed")
            else:
                print("Switch released")
            time.sleep(0.2)
    finally:
        GPIO.cleanup()

    return

if __name__ == "__main__":
    main()
