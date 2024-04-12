
from tkinter import *

root = Tk()
root.configure(background='light steel blue')
root.title("Bet Tracker Main Menu")
root.geometry("760x400")


first_name = Label(root, text="First Name")
last_name = Label(root, text="Last Name")
email = Label(root, text="Email")



first_name.grid(row=0, column=0, sticky=E)
last_name.grid(row=1, column=0, sticky=E)
email.grid(row=2, column=0, sticky=E)

first_name_entry = Entry(root)
last_name_entry = Entry(root)
email_entry = Entry(root)

first_name_entry.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)

root.mainloop()