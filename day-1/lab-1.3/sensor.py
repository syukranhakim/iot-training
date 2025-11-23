# Script to read dht11 sensor data
import Adafruit_DHT
import time


# Sensor configuration
SENSOR = Adafruit_DHT.DHT11
PIN = 4  # GPIO4

def main():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        print(f"Temp: {temperature}°C  Humidity: {humidity}%")
        time.sleep(2.0)

    return

if __name__ == "__main__":
    main()
