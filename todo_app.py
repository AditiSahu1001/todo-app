import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")
root.config(bg="#1e1e2e")

tasks = []

# ---------- Functions ----------

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty")
        return
    tasks.append(task)
    listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def mark_done():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        listbox.delete(index)
        listbox.insert(index, f"✔ {task}")
    except:
        messagebox.showwarning("Warning", "Select a task")

# ---------- UI ----------

title = tk.Label(root, text="📝 My To-Do List",
                 font=("Segoe UI", 20, "bold"),
                 bg="#1e1e2e", fg="white")
title.pack(pady=15)

task_entry = tk.Entry(root, font=("Segoe UI", 12))
task_entry.pack(padx=20, pady=10, fill="x")

btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task",
                    command=add_task,
                    bg="#4CAF50", fg="white",
                    width=12)
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame, text="Mark Done",
                     command=mark_done,
                     bg="#2196F3", fg="white",
                     width=12)
done_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete",
                       command=delete_task,
                       bg="#f44336", fg="white",
                       width=12)
delete_btn.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root,
                     font=("Segoe UI", 12),
                     bg="#2a2a40",
                     fg="white",
                     selectbackground="#6c63ff",
                     height=12)
listbox.pack(padx=20, pady=20, fill="both", expand=True)

root.mainloop()
