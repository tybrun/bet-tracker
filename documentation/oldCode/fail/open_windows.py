import tkinter as tk
from tkinter import ttk
import AddBet

bg_color = 'light steel blue'
bets_color = 'salmon'

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("600x400")
        self.minsize(600, 400)


        self.menu = Menu(self)

        self.mainloop()

        '''self.grid_rowconfigure(0, weight=1) # this needed to be added
        self.grid_columnconfigure(0, weight=1) # as did this

        main_frame = ttk.Frame(self)
        main_frame.grid(row=0, column=0, sticky='nsew')
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure((0,1,2), weight=1)

        bets_frame = ttk.Frame(main_frame, width=200, height=200, relief='sunken', borderwidth=5)
        bets_frame.grid(row=0, column=0, sticky='nsew')
        
        bets_lbl = ttk.Label(bets_frame, text="Bets", anchor=tk.CENTER,
                             background=bg_color)
        
        add_bet = ttk.Button(bets_frame, text="Add", width=10)
        

        update_bet = ttk.Button(bets_frame, text="Update", width=10) #command=self.open_update_bet_window, style='Bets.TButton
        
        bets_lbl.grid(row=0, column=0) #, ipadx=5, ipady=10, sticky='nsew')
        add_bet.grid(row=1, column=0)
        update_bet.grid(row=2, column=0)


        
        trans_frame = ttk.Frame(main_frame, width=200, height=200, relief='sunken', borderwidth=5)
        trans_frame.grid(row=0, column=1, sticky='nsew')

        stats_frame = ttk.Frame(main_frame, width=200, height=200, relief='sunken', borderwidth=5)
        stats_frame.grid(row=0, column=2, sticky='nsew')'''
        


        '''#super().__init__()
        self.title("Main Menu")
        self.geometry('600x400')
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2), weight=1)

        self.master.configure(background=bg_color)



        s=ttk.Style()
        s.theme_use('alt')
        s.configure('TButton', background = bg_color, foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
        s.map('TButton', background=[('active','red')])

        bets_lbl = ttk.Label(self, text="Bets", anchor=tk.CENTER, background=bg_color)
        bets_lbl.grid(row=0, column=0, ipadx=5, ipady=10, sticky='nsew')

        add_bet = ttk.Button(self, text="Add", width=10,
                          command=self.open_add_bet_window)
        add_bet.grid(row=1, column=0)

        update_bet = ttk.Button(self, text="Update", width=10, 
                          command=self.open_update_bet_window, style='Bets.TButton')
        update_bet.grid(row=2, column=0)




        trans_lbl = ttk.Label(self, text="Transations", anchor=tk.CENTER, background=bg_color).grid(row=0, column=1, sticky='nsew')

        add_trans = ttk.Button(self, text="Add", width=10, 
                          command=self.open_add_trans_window)
        add_trans.grid(row=1, column=1, padx=10, pady=10)

        update_trans = ttk.Button(self, text="Update", width=10, 
                          command=self.open_update_trans_window)
        update_trans.grid(row=2, column=1, padx=10, pady=10)


        stats_lbl = ttk.Label(self, text="Statistics", anchor=tk.CENTER, background=bg_color).grid(row=0, column=2, sticky='nsew')

        weekly_stats = ttk.Button(self, text="Add Bet", width=10, 
                          command=self.open_weekly_window)
        weekly_stats.grid(row=1, column=2, padx=10, pady=10)

        monthly_stats = ttk.Button(self, text="Add Bet", width=10, 
                          command=self.open_monthly_window)
        monthly_stats.grid(row=2, column=2, padx=10, pady=10)

        self.pack()
         
    def open_add_bet_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        AddBetWindow(self.master)

    def open_update_bet_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        UpdateBetWindow(self.master)
         
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

    def open_monthly_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MonthlyWindow(self.master)'''


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        bets_lbl = ttk.Label(self, text="Bets", anchor=tk.CENTER, background=bg_color)
        add_bet = ttk.Button(self, text="Add", width=10, command=self.open_add_bet_menu)

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

    def open_add_bet_menu(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        AddBet.AddBetMenu(parent=self.master, controller=self)

    def open_add_bet_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        self.menu = AddBet.AddBetMenu(self.master)

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




'''class AddBetWindow(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("600x400")
        self.minsize(600, 400)


        self.menu = AddBetMenu(self)




        self.pack()
             
    def submit(self):
        pass
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MenuWindow(self.master)


class Menu(ttk.Frame):
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
        WeeklyWindow(self.master)'''

class UpdateBetWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Update Bet")
        self.master.resizable(False, False)
        self.master.geometry("600x400")

        self.pack()
             
    def submit(self):
        pass
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MenuWindow(self.master)

class AddTransWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Update Bet")
        self.master.resizable(False, False)
        self.master.geometry("600x400")

        self.pack()
             
    def submit(self):
        pass
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MenuWindow(self.master)

class UpdateTransWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Update Bet")
        self.master.resizable(False, False)
        self.master.geometry("600x400")

        self.pack()
             
    def submit(self):
        pass
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MenuWindow(self.master)

class WeeklyWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Update Bet")
        self.master.resizable(False, False)
        self.master.geometry("600x400")

        self.pack()
             
    def submit(self):
        pass
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MenuWindow(self.master)

class MonthlyWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Update Bet")
        self.master.resizable(False, False)
        self.master.geometry("600x400")

        self.pack()
             
    def submit(self):
        pass
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MenuWindow(self.master)



'''def open_root():
    root = Tk()
    root.configure(background='light steel blue')
    root.title("Main Menu")
    root.geometry("600x400")

    btn = Button(root, text="Add Bet", command=open_add_bet).pack()

    root.mainloop()


def open_add_bet():
    add_bet = Tk()
    add_bet.configure(background='light steel blue')
    add_bet.title("Add Bet")
    add_bet.geometry("400x400")
    add_bet.transient()
    add_bet.grab_set()
    root.wait_window(add_bet)
'''