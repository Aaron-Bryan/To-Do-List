# This is a To Do List App made with Python and Tkinter

import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json

class To_do_list(tk.Tk):
    def __init__(self):

        #Initialize the View
        self.title("To Do List")
        self.geometry("400x400")

        style = Style(theme="flatly")
        style.configure("Test.Text", foreground="gray")