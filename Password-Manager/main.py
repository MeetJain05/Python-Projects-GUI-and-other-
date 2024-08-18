#Password is copied to your clipboard when you click Generate Password Button
from tkinter import *
# as messagebox is a module it does not comes under *(import everything)
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def GeneratePassword():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website_name = website_entry.get()
    emailid_username = email_entry.get()
    password = password_entry.get()

    new_data = {
        website_name: {
            'email':  emailid_username,
            'password': password
        }
    }

    if len(website_name) == 0 or len(password) == 0 or len(emailid_username) == 0:
        messagebox.showwarning(
            title='Oops', message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website_name, message=f'These are the details entered:\nEmail/Username: {emailid_username}\nPassword: {password}\nPress OK to Confirm.')

        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # reading the old data
                    data = json.load(data_file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = new_data
            else:
                # updating the old data with new data
                data.update(new_data)

            # dumping the updated data
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- Finding password ----------------------------#


def find_password():
    website_name = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            existing_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(
            title='Error', message='Data File is empty')
    else:
        if website_name in existing_data:
            website_data = existing_data[website_name]

            messagebox.showinfo(title=website_name, message=f"Email\\Username: {
                                website_data['email']}\nPassword: {website_data['password']}")
        else:
            messagebox.showerror(title='Error',
                                 message='No details for the website exists')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)


canva = Canvas(width=200, height=200, highlightthickness=0)

# logo image
logo_image = PhotoImage(file='logo.png')
canva.create_image(100, 100, image=logo_image)
canva.grid(column=1, row=0)

# labels

website_txt = Label(text='Website: ')
website_txt.grid(column=0, row=1)

email_txt = Label(text=r'Email/Username: ')
email_txt.grid(column=0, row=2)

password_txt = Label(text='Password: ')
password_txt.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1,
                   sticky='NSEW', padx=4, pady=4)
website_entry.focus()

# for understnading the use of sticky in grid():
# https://riptutorial.com/tkinter/example/29713/grid--

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky='NSEW', padx=4, pady=4)
# default email(eg your most commonly used email)
email_entry.insert(0, 'name@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='NSEW', padx=4, pady=4)

# Buttons

generatepassword = Button(text='Generate Password',
                          width=15, command=GeneratePassword)
generatepassword.grid(column=2, row=3, sticky='EW', padx=4, pady=4)

add = Button(text='Add', width=36, command=save)
add.grid(column=1, row=4, columnspan=2, sticky='EW', padx=4, pady=4)

search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(column=2, row=1, sticky='EW', padx=4, pady=4)

window.mainloop()
