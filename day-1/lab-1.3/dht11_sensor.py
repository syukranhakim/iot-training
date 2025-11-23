# Script to read dht11 sensor data connected to
# Raspberry Pi board

import adafruit_dht
import board
import time

# Set data pin to be GPIO5
dht = adafruit_dht.DHT11(board.D5)

def main():
    while True:
        try:
            temp = dht.temperature
            hum = dht.humidity
            print(f"Temp={temp}°C Humidity={hum}%")
        except Exception as e:
            print("Read error:", e)
        time.sleep(2.0)

    return


if __name__ == "__main__":
    main()

