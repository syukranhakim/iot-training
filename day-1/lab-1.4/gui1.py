import customtkinter as ctk

def main():

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