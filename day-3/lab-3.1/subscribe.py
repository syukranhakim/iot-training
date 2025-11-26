import json
import paho.mqtt.client as mqtt

# ThingsBoard MQTT broker details
THINGSBOARD_HOST = 'mqtt.thingsboard.cloud'
MQTT_PORT = 1883

# TODO: Replace with access token from device details
ACCESS_TOKEN = ''

MQTT_TOPIC = 'v1/devices/me/rpc/request/+'

# Connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to ThingsBoard MQTT broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("message received:", payload)
    except json.JSONDecodeError:
        print("Invalid JSON:", msg.payload)


# Main function
def main():
    client = mqtt.Client()
    client.username_pw_set(ACCESS_TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(THINGSBOARD_HOST, MQTT_PORT, 60)
    client.loop_forever()

    return

if __name__ == "__main__":
    main()
