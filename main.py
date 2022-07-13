from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing Entry", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", 'r') as data_file:
                #reading the old data
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError): # recall that else executes if anything in the try block fails
            with open("data.json", "w") as data_file:
                # Create a new file if one does not already exist
                json.dump(new_data, data_file, indent=4)
        else: # note else executes only if everything in the try block succeeds
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)

        finally: # note finally executes regardless of what happens in try, except or else.
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ------------------------ PASSWORD SEARCH-------------------------

def find_password():
    query = website_entry.get().lower()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            email = data[query].get("email")
            password = data[query].get("password")
            print(f"email: {email}")
            print(f"password: {password}")
            pyperclip.copy(password)
            messagebox.showinfo(title=query, message=f"Username: {email}\n Password: {password}\n\n"
                                                              f" password copied to clipboard")
    except (KeyError, FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="No results found", message=f"{query} not found in database\n"
                                                              f"note: website is not case sensitive")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=30)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0, "steven.kruger87@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, columnspan=1, padx=5)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add to database", width=25, command=save)
add_button.grid(row=4, column=1, columnspan=1)
search_button=Button(text="Search", command=find_password, width= 15)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()
