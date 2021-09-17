from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

BROWN = "#d79771"
YELLOW = "#ffebc9"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    final_password = "".join(password_list)  # join() allows us to join strings with or without a character, here empty.
    password.insert(0, final_password)
    pyperclip.copy(final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_entry = website.get()
    email_entry = email.get()
    password_entry = password.get()

    if len(website_entry) == 0 or len(email_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any fields empty ! ")

    else:
        is_ok = messagebox.askokcancel(title=website_entry,
                                       message=f"These are the details entered : \nEmail: {email_entry} "
                                               f"\nPassword: {password_entry} \nAre those ok to save ?")

        if is_ok:
            with open("data.txt", "a") as data:  # Don't have to data.close() with this method
                data.write(f"{website_entry} | {email_entry} | {password_entry} \n")
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=35, pady=35, bg=BROWN)

# Canvas
canvas = Canvas(width=200, height=200, bg=BROWN, highlightthickness=0)
padlock_img = PhotoImage(file="padlock.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Arial", 13), bg=BROWN, highlightthickness=0)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Arial", 13), bg=BROWN, highlightthickness=0)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Arial", 13), bg=BROWN, highlightthickness=0)
password_label.grid(column=0, row=3)

# Entries
website = Entry()
website.grid(column=1, row=1, columnspan=2, sticky="EW")
website.focus()
email = Entry()
email.grid(column=1, row=2, columnspan=2, sticky="EW")
email.insert(0, "your.email@gmail.com")
password = Entry(width=32)
password.grid(column=1, row=3, sticky="W")

# Buttons
generate = Button(text="Generate Password", bg=YELLOW, highlightthickness=0, command=generate_password)
generate.grid(column=2, row=3)
add = Button(text="Add", width=35, bg=YELLOW, highlightthickness=0, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
