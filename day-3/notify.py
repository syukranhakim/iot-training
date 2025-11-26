import requests

def main():

    url = "https://api.pushover.net/1/messages.json"

    message = \
    """
    "**Hello there** _notification_ from `pushoverbot` [Check in](https://umpsa.edu.my)"

    """

    data = {
        "token": "??",  # User Token
        "user": "??",   # User ID
        "message": message
    }

    resp = requests.post(url, data=data)
    print(resp.text)

    return


if __name__ == "__main__":
    main()
