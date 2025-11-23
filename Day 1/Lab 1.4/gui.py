from customtkinter import *

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



    return


if __name__ == "__main__":
    main()

