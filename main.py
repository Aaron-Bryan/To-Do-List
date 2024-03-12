import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json


class To_do_list_app(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo List")
        self.geometry("650x550")
        style = Style(theme="flatly")
        style.configure("Custon.TEntry", foreground="gray")

        # Create input field for adding tasks
        self.input_task = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custon.TEntry")
        self.input_task.pack(pady=10)

        # Set input field placeholder
        self.input_task.insert(0, "Add task")

        # Bind Event to clear placeholder when input field is clicked
        self.input_task.bind("<FocusIn>", self.clear_placeholder)
        # Bind Event to restore placeholder when input field loses focus
        self.input_task.bind("<FocusOut>", self.restore_placeholder)

        # Button to adding tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Create listbox to display added tasks
        self.task_list = tk.Listbox(self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Buttons for marking tasks as done or deleting them
        ttk.Button(self, text="Done", style="success.TButton", command=self.finish_task).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton",command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)

        # Create buttton for displaying task statistics
        ttk.Button(self, text="View Stats", style="info.TButton", command=self.view_status).pack(side=tk.BOTTOM, pady=10)

        self.load_tasks()

    #Functions
    #Function to view the current status of the task
    def view_status(self):
        done_count = 0
        total_count = self.task_list.size()

        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    #Function to add tasks
    def add_task(self):
        task = self.input_task.get()

        if task != "Add Task":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="orange")
            self.input_task.delete(0, tk.END)
            self.save_tasks()

    #Function to mark the tasks as done
    def finish_task(self):
        task_index = self.task_list.curselection()

        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()

    #Function to delete tasks
    def delete_task(self):
        task_index = self.task_list.curselection()

        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()

    #Function to clear the place holder text
    def clear_placeholder(self, event):

        if self.input_task.get() == "Add Task":
            self.input_task.delete(0, tk.END)
            self.input_task.configure(style="TEntry")

    #Function to restore the place holder
    def restore_placeholder(self, event):

        if self.input_task.get() == "":
            self.input_task.insert(0, "Add Task")
            self.input_task.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)

                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, fg=task["color"])

        except FileNotFoundError:
            pass

    def save_tasks(self):
        data = []

        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})

        with open("tasks.json", "w") as f:
            json.dump(data, f)


if __name__ == '__main__':
    app = To_do_list_app()
    app.mainloop()