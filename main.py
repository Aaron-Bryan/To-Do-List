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
        style.configure("Custon.TEntry", foreground="gray")

        #Input field for additional tasks you want to add
        self.input_task = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custon.TEntry")
        self.input_task.pack(padx=10, pady=10)

        #Place holder for the input field
        self.input_task.insert(0, "Enter the task you want to do: ")