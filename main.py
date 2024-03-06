# This is a To Do List App made with Python and Tkinter

import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json

class To_do_list(tk.Tk):
    def __init__(self):

        #Initialize the View
        self.title("To Do List")
        self.geometry("600x600")

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
        ttk.Button(self, text="Done", style="success.TButton", command=self.done_task).pack(side=tk.LEFT, pady=10, padx=10)
        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task).pack(side=tk.RIGHT, pady=10,padx=10)

        #Button to display tast status
        ttk.Button(self, text="View Status", style="info.TButton", command=self.view_stats).pack(side=tk.BOTTOM, pady=10, padx=10)

        self.load_task()


        #Functions
        def view_stats(self):
            done_count = 0
            total_count = self.task_list.size()

            for i in range(total_count):
                if (self.task_list.itemget(i, "fg") == "green"):
                    done_count = done_count + 1

            messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

        def add_task(self):
            task = self.input_task.get()

            if ((task != "Add Task") and (task != "")):
                self.task_list.insert(tk.END, task)
                self.task_list.itemconfig(tk.END, fg="orange")
                self.input_task.delete(0, tk.END)
                self.save_task()

        def delete_task(self):
            task_position = self.task_list.curselection()

            if (task_position == True):
                self.task_list.delete(task_position)
                self.save_task()

        def clear_placeholder(self):

            if (self.input_task.get() == "Add Task"):
                self.input_task.delete(0, tk.END)
                self.input_task.configure(style="TEntry")

        def restore_placeholder(self):
            pass

        def load_task(self):
            pass

        def save_task(self):
            pass

if __name__ == '__main__':
    app = To_do_list()
    app.mainloop()