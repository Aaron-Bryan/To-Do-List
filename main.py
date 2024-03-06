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

        #Input field for additional tasks the user ads
        self.input_task = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custon.TEntry")
        self.input_task.pack(pady=10, padx=10)

        #Place holder for the input field
        self.input_task.insert(0, "Enter the task you want to do: ")

        #Event to clear the placeholder when you click the input field
        self.input_task.bind("<FocusIN>", self.clear_placeholder)
        #Event to restore placeholder when the input field loses focus
        self.input_task.bind("<FocusOut>", self.restore_placeholder)

        #Button for adding the tasks onto the list
        ttk.Button(self, text="Add task", command=self.add_task).pack(pady=5, padx=5)

        #Listbox for the tasks.
        self.task_list = tk.Listbox (self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        #Buttons to mark the tasks as done.
        ttk.Button(self, text="Done", style="success.TButton", command=self.mark_done).pack(side=tk.LEFT, pady=10, padx=10)
        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task).pack(side=tk.RIGHT, pady=10,padx=10)

        #Button to display tast status
        ttk.Button(self, text="View Status", style="info.TButton", command=self.view_stats).pack(side=tk.BOTTOM, pady=10, padx=10)

        self.load_tasks()


        #Functions