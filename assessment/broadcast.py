import json
import time
import paho.mqtt.client as mqtt
import random

MQTT_BROKER = "localhost"

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

staffs = {
    '01066': 'marlina',
    '01556': 'sulastri',
    '01752': 'afif',
    '01789': 'nasir',
    '01989': 'syukran',
    '02012': 'wsyahirah'
}

def main():
    try:
        while True:
            leds = {
                k: random.choice(range(3))
                for k in staffs.keys()
            }
            for k, v in leds.items():
                print(f"{staffs[k]:10} -> LED {v}")
                msg = json.dumps({"led": v})
                client.publish(k, msg)
            print()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping publisher...")

    return

if __name__ == "__main__":
    main()
