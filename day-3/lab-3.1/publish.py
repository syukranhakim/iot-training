import time
import json
import random
import paho.mqtt.client as mqtt

# ThingsBoard MQTT broker details
THINGSBOARD_HOST = 'mqtt.thingsboard.cloud'
MQTT_PORT = 1883
ACCESS_TOKEN = 'KWsWnRqo7Q8fcm2b689L'

# Default telemetry topic
MQTT_TOPIC = 'v1/devices/me/telemetry'

# Connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to ThingsBoard MQTT broker")
    else:
        print(f"Failed to connect, return code {rc}")


def main():
    # Create MQTT client and set callbacks
    client = mqtt.Client()
    client.username_pw_set(ACCESS_TOKEN)
    client.on_connect = on_connect

    # Connect to broker
    client.connect(THINGSBOARD_HOST, MQTT_PORT, 60)
    client.loop_start()

    try:
        while True:
            # Generate dummy telemetry data
            temperature = round(random.uniform(20.0, 30.0), 2)
            humidity = round(random.uniform(30.0, 60.0), 2)
            pressure = round(random.uniform(1000.0, 1025.0), 2)
            data = {
                "temperature": temperature,
                "humidity": humidity,
                "pressure": pressure
            }

            # Convert to JSON and publish
            client.publish(MQTT_TOPIC, json.dumps(data))
            print(f"Published: {data}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        client.loop_stop()
        client.disconnect()

    return


if __name__ == "__main__":
    main()
