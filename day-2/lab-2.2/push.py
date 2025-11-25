import requests
import random

def main():

    ip_address = "10.61.79.197"
    url = f"http://{ip_address}:5000/push-data"

    # Creaate dummy data
    data = {
        "temperature": random.randint(10, 30)
    }

    print(data)
    resp = requests.post(url, json=data)
    print(resp, resp.json())
    return

if __name__ == "__main__":
    main()
