import serial
import time


def main():
    ser = serial.Serial('/dev/serial0', 9600, timeout=1) 

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print("Received:", line)
            time.sleep(0.1)
    finally:
        ser.close()

    return

if __name__ == "__main__":
    main()



"""
On a Raspberry Pi, the primary UART pins (GPIO14 = TX, GPIO15 = RX) are usually exposed as /dev/serial0.

serial0 is a symlink that points to the “default UART” for the Pi model.

On most Pi models, this maps to PL011 UART, which is the full-featured UART.

It is not always automatically enabled; you need to enable the serial interface in raspi-config and disable the console login on the serial port.

Steps to ensure it works:

Run sudo raspi-config → Interface Options → Serial Port.

Enable serial hardware.

Disable login shell over serial.

Reboot.

/dev/serial0 will then point to the TX/RX pins.

You can verify with:

ls -l /dev/serial0
It will show which actual UART device it points to (ttyAMA0 or ttyS0).
"""