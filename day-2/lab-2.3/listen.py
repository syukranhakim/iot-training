import paho.mqtt.client as mqtt

# Callback function when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")
    return


def main():
    # MQTT setup
    # Change to your broker IP e.g. 79.10.10.8 or hostname
    broker = "localhost"
    port = 1883

    client = mqtt.Client()
    client.on_message = on_message

    client.connect(broker, port)
    client.subscribe("room-temperature")

    # Blocking loop to listen for messages
    client.loop_forever()
    return

if __name__ == "__main__":
    main()
