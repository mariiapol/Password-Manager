from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#seach website to find password
def search():
    w = entry_w.get()
    if len(w) == 0:
        messagebox.showinfo(title="Oops", message="Please add website name!")
    else:
        try:
            with open("data.json", "r") as data:
                # read old data
                d = json.load(data)
                print(type(d))


        except FileNotFoundError:
            messagebox.showinfo(message="No data file found!")

        else:
            if w not in d:
                messagebox.showinfo(message=f"No details for the {w} exist.")
            else:

                messagebox.showinfo(message=f'Website name: {w}.\nEmail: {d[w]["email"]}.\nPassword: {d[w]["password"]}.')



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
#password = ""
#for char in password_list:
#  password += char
    entry_p.insert(0, password)
    pyperclip.copy(password)

    #print(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_p():
    w = entry_w.get()
    e = entry_e.get()
    p = entry_p.get()
    new_data = {
        w:
            {
             "email": e,
             "password": p,
        }
    }


    if len(w) == 0 or len(p)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=w, message=f"These are the details entered: \nEmail: {e} \nPassword: {p}\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data:
                    #read old data
                    d = json.load(data)
                    #update, add new data
                    d.update(new_data)

            except FileNotFoundError:
                d = new_data



            with open("data.json", "w") as data:

                #saving new data
                json.dump(d, data, indent=4)

            entry_p.delete(0, "end")
            entry_w.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=1)

label_t = Label(text="Website:", bg="white")
label_t.grid(column=1, row=2)

label_e = Label(text="Email/Username:", bg="white")
label_e.grid(column=1, row=3)

label_p = Label(text="Password:", bg="white")
label_p.grid(column=1, row=4)


button_g = Button(text="Generate password", bg="white", command=generate_password, width=14)
button_g.grid(column=3, row=4)

entry_w = Entry(bg="white", width=32)
entry_w.grid(column=2, row=2)
entry_w.focus()


entry_e = Entry(bg="white", width=51)
entry_e.grid(column=2, row=3, columnspan=2)
entry_e.insert(0, "polishchuk.mariya@gmail.com")

entry_p = Entry(bg="white", width=32)
entry_p.grid(column=2, row=4)


button_add = Button(text="Add", width=43, bg="white", command=add_p)
button_add.grid(column=2, row=5, columnspan=2, padx=3, pady=3)

button_s = Button(text="Search", bg="white", width=14, command=search)
button_s.grid(column=3, row=2)










window.mainloop()