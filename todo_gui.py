import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task:
            tasks[index] = new_task
            listbox.delete(index)
            listbox.insert(index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated task!")
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

def mark_completed():
    try:
        index = listbox.curselection()[0]
        listbox.itemconfig(index, fg="green")
        messagebox.showinfo("Done", "Task marked as completed!")
    except:
        messagebox.showwarning("Warning", "Select a task to mark completed!")

# GUI WINDOW
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.config(bg="#f0f0f0")

# ENTRY FIELD
entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.pack(pady=10)

# BUTTONS
frame = tk.Frame(root)
frame.pack()

btn_add = tk.Button(frame, text="Add Task", width=12, command=add_task)
btn_add.grid(row=0, column=0, padx=5)

btn_update = tk.Button(frame, text="Update Task", width=12, command=update_task)
btn_update.grid(row=0, column=1, padx=5)

btn_complete = tk.Button(frame, text="Mark Completed", width=12, command=mark_completed)
btn_complete.grid(row=1, column=0, padx=5, pady=5)

btn_delete = tk.Button(frame, text="Delete Task", width=12, command=delete_task)
btn_delete.grid(row=1, column=1, padx=5, pady=5)

# LISTBOX TO SHOW TASKS
listbox = tk.Listbox(root, height=12, width=45, font=("Arial", 12))
listbox.pack(pady=10)

root.mainloop()
