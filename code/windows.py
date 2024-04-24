"""Module that holds all tkinter window and frame objects

This module contains all the classes that are used to create the tkinter windows and frames.
The classes are used to create the main menu, the bets window, and the statistic windows.
The classes are all subclasses of the ttk.Frame class and are used to create the windows and frames that are displayed to the user.

"""


import tkinter as tk
from tkinter import ttk
import pandas as pd
import statistics



class MainWindow(tk.Tk):
    """Class for the main window of the application

    This class is used to create the main window of the application.
    The main window is the window that is displayed when the application is first opened, it
    contains the main menu and is used to navigate to the other frames.

    Attributes:
        frames: Dictionary of all frames within the application, used to toggle between frames
        container: The base frame, used to hold all other frames from the other classes
    """
    def __init__(self):
        """"Initializes the main window of the application

            Args:
                None        
        """
        super().__init__()
        self.title("Bet Tracker")
        self.geometry("400x400")
        self.minsize(400, 400)

        container = tk.Frame(self, height=400, width=600)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Menu, Bets, ChooseStats, AllStats, MonthlyStats, WeeklyStats):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)


        #self.menu = Menu(self)

        self.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()





class Menu(ttk.Frame):
    """Frame with all the main menu options

    This class builds off of the frame provided by the MainWindow class.
    This class creates the main menu for the application, containing buttons to navigate
    to other frames or quit the program.
    
    Attributes:
        self.create_widgets(): Method that displays all widgets and defines their functionatiliy
        self.quit(): Method that quits the program
    
    """
    def __init__(self, parent, controller):
        """Initializes this frame

            Args:
                parent: The parent frame that this frame is a child of
                controller: The controller that is used to switch between frames
        """
        super().__init__(parent)

        #self.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets(controller)

    def create_widgets(self, controller):
        """Creates and states function of labels and buttons within this frame

            Args:
                controller: The controller that is used to switch between frames
        """

        # Creating all widgets (labels and buttons)
        title_lbl = ttk.Label(self, text="Main Menu", anchor=tk.CENTER)
        bet_btn = ttk.Button(self, text="Bets", width=12, command=lambda: controller.show_frame(Bets))  # command activates on click, switches to another frame
        stat_btn = ttk.Button(self, text="Statistics", width=12, command=lambda: controller.show_frame(ChooseStats))
        quit_btn = ttk.Button(self, text="Quit", width=12, command=quit)

        # Configuring the grid layout
        self.columnconfigure((0,1), weight=1, uniform='a')
        self.rowconfigure((0,1,2), weight=1, uniform='a')
       
       # Placing all widgets in the grid layout
        title_lbl.grid(row=0, column=0, columnspan=2, ipady=5, sticky='nsew')
        bet_btn.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        stat_btn.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        quit_btn.grid(row=2, column=0, columnspan=2, padx=50, pady=10, ipady=5)


    def quit(self):
        """Quits the program
        """
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()

class Bets(ttk.Frame):
    """Frame that allows the user to record a bet, adding it to the database

    This class holds many widgets that allow the user to input data about a bet they have made.
    Those widgets include comboboxes, entries, and radio buttons, allowing them to provide all
    neccessary betting info for this application. Upon clicking submit, the data is added to an
    excel file.

    Attributes:
        self.create_widgets(): Method that displays all widgets and defines their functionatiliy
        self.submit(): Method that adds the data to the excel file
    
    """
    def __init__(self, parent, controller):
        """Initializes the frame
        """
        super().__init__(parent)
        #self.master = parent
        
        self.create_widgets(controller)
        

    def create_widgets(self, controller):
        """Creates and places all widgets on the frame

            This uses widgets to collect user input and then store it in the excel file.
            It utilizes a grid layout like previous frames to place widgets properly

            Args:
                controller: The controller that is used to switch between frames
        """
        # Creating all widgets
        title_lbl = ttk.Label(self, text="Bets", anchor=tk.CENTER)
        
        sportsbook_lbl = ttk.Label(self, text="Sportsbook", anchor=tk.CENTER)
        sportsbook_combo = ttk.Combobox(self, values=["Bet365", "BetMGM", "DraftKings", "FanDuel", "ESPNBet"])

        odds_lbl = ttk.Label(self, text="Odds (+/-###)", anchor=tk.CENTER)
        odds_entry = ttk.Entry(self)

        sport_lbl = ttk.Label(self, text="Sport", anchor=tk.CENTER)
        sport_entry = ttk.Combobox(self, values=["NFL", "NBA", "NHL", "MLB", "NCAAF", "NCAAM", "NCAAW"])

        date_lbl = ttk.Label(self, text="Date (MM-DD-YYY)", anchor=tk.CENTER)
        date_entry = ttk.Entry(self)

        stake_lbl = ttk.Label(self, text="Stake", anchor=tk.CENTER)
        stake_entry = ttk.Entry(self)

        # Radion buttons for bonus bet and result
        yn = tk.IntVar()
        yn.set(0)
        bonus_bet_lbl = ttk.Label(self, text="Bonus Bet", anchor=tk.CENTER)
        yes_radio = ttk.Radiobutton(self, text="Yes", variable=yn, value=0)
        no_radio = ttk.Radiobutton(self, text="No", variable=yn, value=1)

        wl = tk.IntVar()
        wl.set(0)
        result_lbl = ttk.Label(self, text="Result", anchor=tk.CENTER)
        win_radio = ttk.Radiobutton(self, text="Win", variable=wl, value=0)
        loss_radio = ttk.Radiobutton(self, text="Loss", variable=wl, value=1)

        return_lbl = ttk.Label(self, text="Return", anchor=tk.CENTER)
        return_entry = ttk.Entry(self)

        submit_btn = ttk.Button(self, text="Submit", width=10, command=lambda: submit())
        back_btn = ttk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(Menu))

        

        # Configuring the grid layout
        self.columnconfigure((0,1,2,3), weight=1, uniform='a')
        self.rowconfigure(0, weight=2)
        self.rowconfigure((1,2,3,4,5,6,7,8,9,10), weight=1)
       
       

        # Placing all widgets in the grid layout
        title_lbl.grid(row=0, column=0, columnspan=8, sticky='nsew')
        sportsbook_lbl.grid(row=1, column=0, columnspan=2,  padx=2, pady=2, sticky='e')
        sportsbook_combo.grid(row=1, column=2, columnspan=2,  padx=2, pady=2, sticky='w')
        odds_lbl.grid(row=2, column=0, columnspan=2,  padx=2, pady=2, sticky='e')
        odds_entry.grid(row=2, column=2, columnspan=2,  padx=2, pady=2, sticky='w')
        sport_lbl.grid(row=3, column=0, columnspan=2,  padx=2, pady=2, sticky='e')
        sport_entry.grid(row=3, column=2, columnspan=2, padx=2, pady=2, sticky='w')
        date_lbl.grid(row=4, column=0, columnspan=2, padx=2, pady=2, sticky='e')
        date_entry.grid(row=4, column=2, columnspan=2, padx=2, pady=2, sticky='w')
        stake_lbl.grid(row=5, column=0, columnspan=2, padx=2, pady=2, sticky='e')
        stake_entry.grid(row=5, column=2, columnspan=2, padx=2, pady=2, sticky='w')
        bonus_bet_lbl.grid(row=6, column=0, columnspan=2, padx=2, pady=2, sticky='e')
        yes_radio.grid(row=6, column=2, columnspan=1, padx=2, pady=2, sticky='w')
        no_radio.grid(row=6, column=3, columnspan=1, padx=2, pady=2, sticky='w')
        result_lbl.grid(row=7, column=0, columnspan=2, padx=2, pady=2, sticky='e')
        win_radio.grid(row=7, column=2, columnspan=1, pady=2, sticky='w')
        loss_radio.grid(row=7, column=3, columnspan=1, pady=2, sticky='w')
        return_lbl.grid(row=8, column=0, columnspan=2, padx=2, pady=2, sticky='e')
        return_entry.grid(row=8, column=2, columnspan=2, padx=2, pady=2, sticky='w')
        submit_btn.grid(row=9, column=0, columnspan=2, padx=15, pady=10, ipady=5, sticky='e')
        back_btn.grid(row=9, column=2, columnspan=2, padx=15, pady=10, ipady=5, sticky='w')


        def submit():
            """Adds user input from the widgets into the excel file

                Upon click of the submit button, this method collects the
                data, stores it in a pandas dataframe, and then appends that
                dataframe to a dataframe that is read from an excel file. The new dataframe,
                the combination of old and new data, is then written into the excel file.
            """
            # Reading the data from the excel file
            file = "Log.xlsx"
            df = pd.read_excel(file)


            # Collecting the data from the widgets
            data = {}
            data["Sportsbook"] = sportsbook_combo.get()
            data["Odds"] = odds_entry.get()
            data["Sport"] = sport_entry.get()
            data["Date"] = date_entry.get()
            data["Result"] = "Win" if wl.get() == 0 else "Loss"
            data["Bonus Bet"] = "Yes" if yn.get() == 0 else "No"
            data["Stake"] = stake_entry.get()
            data["Return"] = return_entry.get()

            # Creating a new dataframe with the data
            df_new_row = pd.DataFrame(data, index=[0])

            # Appending the new row to the old dataframe
            df = df._append(df_new_row, ignore_index=True)

            # Writing the new dataframe to the excel file
            df.to_excel(file, index=False)


class ChooseStats(ttk.Frame):
    """Frame that allows user to choose which statistic frame to view

        The user can view three different timeframes of their sportsbetting statistics.
        It has three buttons, "Weekly", "Monthly", and "All Time", that allow the user to
        open a new frame that dispalys the statistics for that timeframe.

        Attributes:
            self.create_widgets(): Method that displays all widgets and defines their functionatiliy
    """
    def __init__(self, parent, controller):
        """Initializes the frame
        """
        super().__init__(parent)
        self.create_widgets(controller)

    def create_widgets(self, controller):
        """Creates and places all widgets on the frame

            This frame is like another menu, asking the user to click a button
            in order to traverse to antoher frame with the information they are looking for.
        """
        # Creating all widgets
        bets_lbl = ttk.Label(self, text="Statistics", anchor=tk.CENTER)
        weekly_btn = ttk.Button(self, text="Weekly", width=12, command=lambda: controller.show_frame(WeeklyStats))
        monthly_btn = ttk.Button(self, text="Monthly", width=12, command=lambda: controller.show_frame(MonthlyStats))
        all_btn = ttk.Button(self, text="All Time", width=12, command=lambda:controller.show_frame(AllStats))
        back_btn = ttk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(Menu))

        # Configuring the grid layout
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2), weight=1, uniform='a')
       
        # Placing all widgets in the grid layout
        bets_lbl.grid(row=0, column=0, columnspan=3, ipady=10, sticky='nsew')
        weekly_btn.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        monthly_btn.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        all_btn.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
        back_btn.grid(row=2, column=1, padx=10, pady=10, ipady=5)


class WeeklyStats(ttk.Frame):
    """Frame that displays the user's betting stats over the last 7 days

        This frame pulls date from the excel file, using methods defined in another file,
        statistics.py. These methods calculate the number of bets, win percentage, and profits/losses
        over the last 7 days. This data is then displayed in an easy, digestable manner
        for the user, using colors to highlight their good and bad statistics.

        Attributes:
            self.create_widgets(): Method that displays all widgets and defines their functionatiliy
    """
    def __init__(self, parent, controller):
        """Initializes the frame
        """
        super().__init__(parent)
        self.create_widgets(controller)

    def create_widgets(self, controller):
        """Creates and places all widgets on the screen
        """

        # Getting the data from the statistics file
        num_bets, win_percent, pl = statistics.GetWeeklyStats()

        # Formatting the data
        pl_text = "$" + str(round(pl,2))
        win_percent_text = str(round(win_percent,2)) + "%"
        num_bets_text = str(num_bets)

        # Defining colors for the widgets
        good_color = 'PaleGreen1'
        bad_color = 'salmon'
        num_bets_color = 'light blue'
        # Defining the color of the widgets based on the data
        if win_percent > 50:
            win_percent_color = good_color
        else:
            win_percent_color = bad_color


        # Creating all widgets
        bets_lbl = ttk.Label(self, text="All Time Stats", anchor=tk.CENTER)
        num_bets_title_lbl = ttk.Label(self, text="Number of Bets", anchor=tk.CENTER, background=num_bets_color)
        num_bets_lbl = ttk.Label(self, text=num_bets_text, anchor=tk.CENTER, background=num_bets_color)
        win_title_lbl = ttk.Label(self, text="Win Percentage", anchor=tk.CENTER, background=win_percent_color)
        win_lbl = ttk.Label(self, text=win_percent_text, anchor=tk.CENTER, background=win_percent_color)

        # Defining the color and label text of the profits/losses based on the data
        if pl > 0:
            pl_color = good_color
            pl_title_lbl = ttk.Label(self, text="Profits", anchor=tk.CENTER, background=pl_color)
        else:
            pl_color = bad_color
            pl_title_lbl = ttk.Label(self, text="Losses", anchor=tk.CENTER, background=bad_color)
        pl_lbl = ttk.Label(self, text=pl_text, anchor=tk.CENTER, background=pl_color)
        back_btn = ttk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(ChooseStats))


        # Configuring the grid layout
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3), weight=1, uniform='a')
       
        # Placing all widgets in the grid layout
        bets_lbl.grid(row=0, column=0, columnspan=3, ipady=10, sticky='nsew')
        num_bets_lbl.grid(row=1, column=0, padx=10, ipady=10, sticky='nsew')
        num_bets_title_lbl.grid(row=2, column=0, padx=10, ipady=10, sticky='new')
        win_lbl.grid(row=1, column=1, padx=10, ipady=10, sticky='nsew')
        win_title_lbl.grid(row=2, column=1, padx=10, ipady=10, sticky='new')
        pl_lbl.grid(row=1, column=2, padx=10, ipady=10, sticky='nsew')
        pl_title_lbl.grid(row=2, column=2, padx=10, ipady=10, sticky='new')
        back_btn.grid(row=3, column=1, padx=10, pady=10, ipady=5)

class MonthlyStats(ttk.Frame):
    """Frame that displays the user's betting stats over the last 31 days

        This frame pulls date from the excel file, using methods defined in another file,
        statistics.py. These methods calculate the number of bets, win percentage, and profits/losses
        over the last 31 days. This data is then displayed in an easy, digestable manner
        for the user, using colors to highlight their good and bad statistics.

        Attributes:
            self.create_widgets(): Method that displays all widgets and defines their functionatiliy
    """
    def __init__(self, parent, controller):
        """Initializes the frame
        """
        super().__init__(parent)
        self.create_widgets(controller)

    def create_widgets(self, controller):
        """Creates and places all widgets on the screen
        """
        # Getting the data from the statistics file
        num_bets, win_percent, pl = statistics.GetMonthlyStats()

        # Formatting the data
        pl_text = "$" + str(round(pl,2))
        win_percent_text = str(round(win_percent,2)) + "%"
        num_bets_text = str(num_bets)

        # Defining colors for the widgets
        good_color = 'PaleGreen1'
        bad_color = 'salmon'
        num_bets_color = 'light blue'
        if win_percent > 50:
            win_percent_color = good_color
        else:
            win_percent_color = bad_color


        # Creating all widgets
        bets_lbl = ttk.Label(self, text="All Time Stats", anchor=tk.CENTER)
        num_bets_title_lbl = ttk.Label(self, text="Number of Bets", anchor=tk.CENTER, background=num_bets_color)
        num_bets_lbl = ttk.Label(self, text=num_bets_text, anchor=tk.CENTER, background=num_bets_color)
        win_title_lbl = ttk.Label(self, text="Win Percentage", anchor=tk.CENTER, background=win_percent_color)
        win_lbl = ttk.Label(self, text=win_percent_text, anchor=tk.CENTER, background=win_percent_color)
        # Defining the color and label text of the profits/losses based on the data
        if pl > 0:
            pl_color = good_color
            pl_title_lbl = ttk.Label(self, text="Profits", anchor=tk.CENTER, background=pl_color)
        else:
            pl_color = bad_color
            pl_title_lbl = ttk.Label(self, text="Losses", anchor=tk.CENTER, background=bad_color)  
        pl_lbl = ttk.Label(self, text=pl_text, anchor=tk.CENTER, background=pl_color)
        back_btn = ttk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(ChooseStats))


        # Configuring the grid layout
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3), weight=1, uniform='a')
       
        # Placing all widgets in the grid layout
        bets_lbl.grid(row=0, column=0, columnspan=3, ipady=10, sticky='nsew')
        num_bets_lbl.grid(row=1, column=0, padx=10, ipady=10, sticky='nsew')
        num_bets_title_lbl.grid(row=2, column=0, padx=10, ipady=10, sticky='new')
        win_lbl.grid(row=1, column=1, padx=10, ipady=10, sticky='nsew')
        win_title_lbl.grid(row=2, column=1, padx=10, ipady=10, sticky='new')
        pl_lbl.grid(row=1, column=2, padx=10, ipady=10, sticky='nsew')
        pl_title_lbl.grid(row=2, column=2, padx=10, ipady=10, sticky='new')
        back_btn.grid(row=3, column=1, padx=10, pady=10, ipady=5)


class AllStats(ttk.Frame):
    """Frame that displays the user's betting stats over their entire recorded betting history

        This frame pulls date from the excel file, using methods defined in another file,
        statistics.py. These methods calculate the number of bets, win percentage, and profits/losses.
        This data is then displayed in an easy, digestable manner for the user,
        using colors to highlight their good and bad statistics.

        Attributes:
            self.create_widgets(): Method that displays all widgets and defines their functionatiliy
    """
    def __init__(self, parent, controller):
        """Initializes the frame
        """
        super().__init__(parent)
        self.create_widgets(controller)

    def create_widgets(self, controller):
        """Creates and places all widgets on the screen
        """
        # Getting the data from the statistics file
        num_bets, win_percent, pl = statistics.GetAllTimeStats()

        # Formatting the data
        pl_text = "$" + str(round(pl,2))
        win_percent_text = str(round(win_percent,2)) + "%"
        num_bets_text = str(num_bets)

        # Defining colors for the widgets
        good_color = 'PaleGreen1'
        bad_color = 'salmon'
        num_bets_color = 'light blue'

        # Defining the color of the widgets based on the data
        if win_percent > 50:
            win_percent_color = good_color
        else:
            win_percent_color = bad_color


        # Creating all widgets
        bets_lbl = ttk.Label(self, text="All Time Stats", anchor=tk.CENTER)
        num_bets_title_lbl = ttk.Label(self, text="Number of Bets", anchor=tk.CENTER, background=num_bets_color)
        num_bets_lbl = ttk.Label(self, text=num_bets_text, anchor=tk.CENTER, background=num_bets_color)
        win_title_lbl = ttk.Label(self, text="Win Percentage", anchor=tk.CENTER, background=win_percent_color)
        win_lbl = ttk.Label(self, text=win_percent_text, anchor=tk.CENTER, background=win_percent_color)
        # Defining the color and label text of the profits/losses based on the data
        if pl > 0:
            pl_color = good_color
            pl_title_lbl = ttk.Label(self, text="Profits", anchor=tk.CENTER, background=pl_color)
        else:
            pl_color = bad_color
            pl_title_lbl = ttk.Label(self, text="Losses", anchor=tk.CENTER, background=bad_color)
        pl_lbl = ttk.Label(self, text=pl_text, anchor=tk.CENTER, background=pl_color)
        back_btn = ttk.Button(self, text="Back", width=10, command=lambda: controller.show_frame(ChooseStats))

        # Configuring the grid layout
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3), weight=1, uniform='a')
       
        # Placing all widgets in the grid layout
        bets_lbl.grid(row=0, column=0, columnspan=3, ipady=10, sticky='nsew')
        num_bets_lbl.grid(row=1, column=0, padx=10, ipady=10, sticky='nsew')
        num_bets_title_lbl.grid(row=2, column=0, padx=10, ipady=10, sticky='new')
        win_lbl.grid(row=1, column=1, padx=10, ipady=10, sticky='nsew')
        win_title_lbl.grid(row=2, column=1, padx=10, ipady=10, sticky='new')
        pl_lbl.grid(row=1, column=2, padx=10, ipady=10, sticky='nsew')
        pl_title_lbl.grid(row=2, column=2, padx=10, ipady=10, sticky='new')
        back_btn.grid(row=3, column=1, padx=10, pady=10, ipady=5)