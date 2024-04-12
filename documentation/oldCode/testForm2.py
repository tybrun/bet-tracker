
from tkinter import *

root = Tk()
root.config(bg="grey95")
root.title("Main Menu")
root.maxsize(780, 1000)

left_frame = Frame(root, width=400, height=1000, bg="grey90")
left_frame.grid(row=0, column=0, padx=10, pady=5,sticky='w'+'e'+'n'+'s')

bets_label = Label(left_frame, text="Bets")
bets_label.grid(row=0, column=0, padx=5, pady=20)

add_bet_button = Button(left_frame, text="Add", fg="Black", bg="PaleGreen1")
add_bet_button.grid(row=1,column=0, padx=5, pady=10, sticky='w'+'e'+'n'+'s')

add_edit_button = Button(left_frame, text="Edit", fg="Black", bg="PaleGreen1")
add_edit_button.grid(row=2,column=0, padx=5, pady=10, sticky='w'+'e'+'n'+'s')




middle_frame = Frame(root, width=260, height=400, bg="grey90")
middle_frame.grid(row=0, column=1, padx=10, pady=5)

trans_label = Label(middle_frame, text="Transactions")
trans_label.grid(row=0, column=0)

add_add_button = Button(middle_frame, text="Add", fg="Black", bg="LightGoldenrod1")
add_edit_button = Button(middle_frame, text="Edit", fg="Black", bg="LightGoldenrod1")

add_add_button.grid(row=1,column=0)
add_edit_button.grid(row=2,column=0)


right_frame = Frame(root, width=260, height=400, bg="grey90")
right_frame.grid(row=0, column=2, padx=10, pady=5)

stats_label = Label(right_frame, text="Statistics")
stats_label.grid(row=0, column=0)

weekly_button = Button(right_frame, text="Weekly", fg="Black", bg="cornflower blue")
monthly_button = Button(right_frame, text="Monthly", fg="Black", bg="cornflower blue")

weekly_button.grid(row=1,column=0)
monthly_button.grid(row=2,column=0)

root.mainloop()