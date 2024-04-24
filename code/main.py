"""This file runs the code to open the main window of the application.

    This file imports the open_windows module and runs the MainWindow class
    to open the main window of the application. The rest of the code for this
    application is in the windows and statistics modules.
"""
import tkinter as tk
from tkinter import ttk
import windows

# Run the main window of the application
obj = windows.MainWindow()
obj.mainloop()