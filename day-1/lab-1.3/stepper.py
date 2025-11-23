#TMC 2209 

import RPi.GPIO as GPIO
import time

def main():

    STEP = 17  # GPIO for STEP
    DIR  = 27  # GPIO for direction

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.setup(DIR, GPIO.OUT)

    GPIO.output(DIR, GPIO.HIGH)  # Set direction

    for i in range(200):        # 200 steps (1 revolution typical)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.001)        # pulse width
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.001)        # pulse interval

    GPIO.cleanup()

    return

    """
    Microstepping (like 1/16 steps) is handled by the driver's MS1/MS2 pins or UART.
    The TMC2209 can run at its default microstep setting (usually 1/16) internally.
    Toggle STEP for each step and set DIR for rotation direction.
    MS1/MS2 (or UART) are only needed if we wish to change microstep resolution
    or configure current.
    """

if __name__ == "__main__":
    main()