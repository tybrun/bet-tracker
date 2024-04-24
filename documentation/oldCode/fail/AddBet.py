import tkinter as tk
from tkinter import ttk
import open_windows

bg_color = 'light steel blue'
bets_color = 'salmon'




class AddBetWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Back", anchor=tk.CENTER, background=bg_color)
        back_btn = ttk.Button(self, text="Back", width=10, command=self.back)

        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure((0,1), weight=1, uniform='a')
       
       
        label.grid(row=0, column=0, ipady=10, sticky='nsew')
        back_btn.grid(row=1, column=0)

        '''self.title("Main Menu")
        self.geometry("600x400")
        self.minsize(600, 400)


        self.menu = AddBetMenu(self)'''




        #self.pack()
             
    def submit(self):
        pass
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        open_windows.MainWindow()


class AddBetMenu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        bets_lbl = ttk.Label(self, text="Bets", anchor=tk.CENTER, background=bg_color)
        add_bet = ttk.Button(self, text="Add", width=10, command=self.open_add_bet_window)

        trans_lbl = ttk.Label(self, text="Transations", anchor=tk.CENTER, background=bg_color)
        add_trans = ttk.Button(self, text="Add", width=10)

        stats_lbl = ttk.Label(self, text="Statistics", anchor=tk.CENTER, background=bg_color)
        weekly_stats = ttk.Button(self, text="Weekly", width=10)
       

        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1), weight=1, uniform='a')
       
       
        bets_lbl.grid(row=0, column=0, ipady=10, sticky='nsew')
        add_bet.grid(row=1, column=0)

        trans_lbl.grid(row=0, column=1, ipady=10, sticky='nsew')
        add_trans.grid(row=1, column=1, padx=10, pady=10)

        stats_lbl.grid(row=0, column=2, sticky='nsew')
        weekly_stats.grid(row=1, column=2, padx=10, pady=10)


    def open_add_bet_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        AddBetWindow(self.master)

    def open_add_trans_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        AddTransWindow(self.master)

    def open_update_trans_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        UpdateTransWindow(self.master)

    def open_weekly_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WeeklyWindow(self.master)