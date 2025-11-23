# Script to read dht11 sensor data
import adafruit_dht
import board
import time

dht = adafruit_dht.DHT11(board.D4)  # GPIO4

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
