"""This file contains functions that calculate statistics for the user's betting history.

    The functions in this file calculate the number of bets placed, the win percentage,
    and the profit/loss over a given timeframe. This file is a helper for the windows.py file.
    The functions in this file read from excel files using pandas, calculate data using
    pandas dataframes, and return the calculated data to the windows.py file.
"""

import pandas as pd
import datetime
from datetime import datetime, timedelta


def GetWeeklyStats():
    """This function is a getter function, returning three metrics to the caller
    
        This function returns the number of bets placed, win percentage,
        and profit/loss over the past week. The function calls and promptly returns
        all three caluclation methods with the argument "Weekly" to calculate
        the metrics over the past week.
    """
    timeframe = "Weekly"
    return BetsPlaced(timeframe), WinPercent(timeframe), PL(timeframe)


def GetMonthlyStats():
    """This function is a getter function, returning three metrics to the caller
    
        This function returns the number of bets placed, win percentage,
        and profit/loss over the past month. The function calls and promptly returns
        all three caluclation methods with the argument "Weekly" to calculate
        the metrics over the past week.
    """
    timeframe = "Monthly"
    return BetsPlaced(timeframe), WinPercent(timeframe), PL(timeframe)


def GetAllTimeStats():
    """This function is a getter function, returning three metrics to the caller
    
        This function returns the number of bets placed, win percentage,
        and profit/loss over the entire history. The function calls and promptly returns
        all three caluclation methods with the argument "Weekly" to calculate
        the metrics over the past week.
    """
    timeframe = "All Time"
    return BetsPlaced(timeframe), WinPercent(timeframe), PL(timeframe)

def BetsPlaced(timeframe):
    """This function calculates the number of bets placed over a given timeframe

        This function reads the betting history from an excel file, and calculates
        the number of bets placed over a given timeframe. The function takes in a
        string argument, "timeframe", which determines the timeframe to calculate the
        number of bets placed. The function returns the number of bets placed over the timeframe.

        Args:
            timeframe: The timeframe to calculate the number of bets placed

    """
    # Read the betting history from an excel file
    file = "Log.xlsx"
    df = pd.read_excel(file)

    # Convert the "Date" column to a datetime object
    df["Date"] = pd.to_datetime(df["Date"], format='mixed')

    # Get the current date
    today = datetime.now()

    # Calculate the number of bets placed over the given timeframe
    num_bets = 0
    if timeframe == "Weekly":
        num_bets = df[(df["Date"] >= today - timedelta(days=7))].shape[0]
    elif timeframe == "Monthly":
        num_bets = df[(df["Date"] >= today - timedelta(days=31))].shape[0]
    else:
        num_bets = df.shape[0]

    # Return the number of bets placed
    return num_bets


def WinPercent(timeframe):
    """This function calculates the win percentage over a given timeframe
    
        This function reads the betting history from an excel file, and calculates
        the win percentage over a given timeframe. The function takes in a
        string argument, "timeframe", which determines the timeframe to calculate the
        win percentage. The function returns the win percentage over the timeframe.

        Args:
            timeframe: The timeframe to calculate the win percentage
    """
    # Read the betting history from an excel file
    file = "Log.xlsx"
    df = pd.read_excel(file)

    # Convert the "Date" column to a datetime object
    df["Date"] = pd.to_datetime(df["Date"], format='mixed')

    # Get the current date
    today = datetime.now()

    # Calculate the win percentage over the given timeframe
    num_bets = 0
    if timeframe == "Weekly":
        # Calculate the number of wins and the number of bets placed
        wins = df[(df["Result"] == "Win") & (df["Date"] >= today - timedelta(days=7))].shape[0]
        num_bets = df[(df["Date"] >= today - timedelta(days=7))].shape[0]
    elif timeframe == "Monthly":
        wins = df[(df["Result"] == "Win") & (df["Date"] >= today - timedelta(days=31))].shape[0]
        num_bets = df[(df["Date"] >= today - timedelta(days=31))].shape[0]
    else:
        wins = df[(df["Result"] == "Win")].shape[0]
        num_bets = df.shape[0]
    
    # In case there are no bets placed
    if num_bets == 0:
        return 0
    
    # Calculate the win percentage
    win_percentage = (wins / num_bets) * 100

    # Return the win percentage
    return win_percentage


def PL(timeframe):
    """This function calculates the profit/loss over a given timeframe

        This function reads the betting history from an excel file, and calculates
        the profit/loss over a given timeframe. The function takes in a
        string argument, "timeframe", which determines the timeframe to calculate the
        profit/loss. The function returns the profit/loss over the timeframe.

        Args:
            timeframe: The timeframe to calculate the profit/loss
    """
    # Read the betting history from an excel file
    file = "Log.xlsx"
    df = pd.read_excel(file)

    # Convert the "Date" column to a datetime object
    df["Date"] = pd.to_datetime(df["Date"], format='mixed')

    # Calculate the profit/loss over the given timeframe
    stakes = 0
    returns = 0
    if timeframe == "Weekly":
        # Calculate the stakes and returns over the past week
        stakes = df[(df["Date"] >= datetime.now() - timedelta(days=7)) &
                          (df["Bonus Bet"] == "No")]["Stake"].sum()
        returns = df[(df["Date"] >= datetime.now() - timedelta(days=7))]["Return"].sum()
    elif timeframe == "Monthly":
        stakes = df[(df["Date"] >= datetime.now() - timedelta(days=31)) &
                          (df["Bonus Bet"] == "No")]["Stake"].sum()
        returns = df[(df["Date"] >= datetime.now() - timedelta(days=31))]["Return"].sum()
    elif timeframe == "All Time":
        stakes = df[(df["Bonus Bet"] == "No")]["Stake"].sum()
        returns = df["Return"].sum()
    
    # Calculate the profit/loss
    profit = returns - stakes

    # Return the profit/loss
    return profit



