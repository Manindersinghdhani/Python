from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generatepassword() :
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter= [choice(letters) for _ in range(randint(8, 10))]
    password_symbols= [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers= [choice(numbers) for _ in range(randint(2, 4))]

    password_list= password_letter+password_numbers+password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    Password_entry.delete(0, END)
    Password_entry.insert(0 ,password)
    pyperclip.copy(password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = EU_entry.get()
    password = Password_entry.get()

    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title= "Oops", message="Please dont leave any field blank ")

    else :

        is_ok= messagebox.askokcancel(title=website, message=f"Verify before updating. \n Email:{email} \n Password: {password} \n Is it ok to save?")

        if is_ok :
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                Password_entry.delete(0, END)

    #messagebox.showinfo(title="Successful", message="Data has been added")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

canvas = Canvas(height =200, width =200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row= 0, column= 1)

website_label = Label(text="Website :")
website_label.grid(row=1 , column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1 , column=1 , columnspan= 2,sticky="ew")
website_entry.focus()

EU_label = Label(text="Email/Username :")
EU_label.grid(row=2 , column=0)

EU_entry = Entry(width=35)
EU_entry.grid(row=2 , column=1 , columnspan= 2,sticky="ew")
EU_entry.insert(0,"sample@email.com")

Password_label = Label(text="Password :")
Password_label.grid(row=3 , column=0)

Password_entry = Entry(width=21)
Password_entry.grid(row=3 , column=1,sticky="ew")

Generate_Button = Button(text="Generate Password",command=generatepassword)
Generate_Button.grid(row=3 , column=2,sticky="ew")

Add_Button = Button (text="Add", width=35,command=save)
Add_Button.grid(row=4, column=1,columnspan= 2,sticky="ew")




mainloop()