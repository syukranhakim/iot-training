import requests
import random

def main():

    ip_address = "10.61.79.197:5000"
    url = f"http://{ip_address}/push-data"

    data = {
        "temperature": random.randint(10, 30)
    }

    resp = requests.post(url, json=data)
    print(resp, resp.json())
    return

if __name__ == "__main__":
    main()
