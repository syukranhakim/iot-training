#from customtkinter import *
import customtkinter as ctk

import RPi.GPIO as GPIO
import adafruit_dht
import board
import time

LED_PIN = 18       # GPIO pin connected to LED
SWITCH_PIN = 23    # GPIO pin connected to switch


# Set data pin to be GPIO5
dht = adafruit_dht.DHT11(board.D5)

led_state = False


def click_handler():
    global led_state
    print("Button clicked")
    led_state = not led_state
    GPIO.output(LED_PIN, led_state)
    return


def update_label(label, app):
    try:
        temp = dht.temperature
    except Exception as e:
        pass
    label.configure(text=f"Temperature is {temp} °C")
    app.after(2000, update_label, label, app)


def main():

    # Init GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # internal pull-up

    app = ctk.CTk()
    app.geometry("300x240")
    app.title("IoT GUI")

    ctk.set_appearance_mode("dark")

    # LED button
    btn = ctk.CTkButton(master=app, text="Toggle LED", command=click_handler)
    btn.place(relx=0.5, rely=0.5, anchor="center")

    # Sensor value
    label = ctk.CTkLabel(app, text='...')
    label.place(relx=0.5, rely=0.7, anchor="center")

    update_label(label, app)

    app.mainloop()

    GPIO.cleanup()

    return


if __name__ == "__main__":
    main()

