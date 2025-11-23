from customtkinter import *
import customtkinter as ctk

def click_handler():
    print("Clicked")
    return


def main():

    app = CTk()
    app.geometry("500x400")

    set_appearance_mode("dark")


    btn = CTkButton(master=app, text="Click Me", command=click_handler)
    btn.place(relx=0.5, rely=0.5, anchor="center")

    app.mainloop()


    print("Hello Warudo")


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Minimal GUI")
    app.geometry("600x480")

    btn = ctk.CTkButton(app, text="Click")
    btn.pack(pady=20)

    app.mainloop()

    return


if __name__ == "__main__":
    main()

