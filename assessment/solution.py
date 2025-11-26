# This code is incomplete.
# Modify the TODO parts to fit the question requirements.

import json
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# GPIO setup
LED1 = ??    # TODO: Update pin definition
LED2 = ??    # TODO: Update pin definition

# Init pins as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

# MQTT setup
MQTT_BROKER = "???"   # TODO: Replace with broker IP
MQTT_TOPIC = "01???"  # TODO: Replace with your UMP staff id


def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("message received:", payload)
        
        led_value = payload.get("led")
        
        if led_value == 2:
            # ?? # TODO: Update code
            # ?? # TODO: Update code
        elif led_value == ???:    # TODO: Update condition
            # ?? # TODO: Update code
            # ?? # TODO: Update code
        else:
            # ?? # TODO: Update code
            # ?? # TODO: Update code
    except json.JSONDecodeError:
        print("Invalid JSON:", msg.payload)


# Main function
def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, 1883, 60)
    client.loop_forever()

    return

if __name__ == "__main__":
    main()
