import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Ielādē uzdevumus no faila, ja fails eksistē."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except Exception:
        messagebox.showwarning("Brīdinājums", "Neizdevās ielādēt saglabātos uzdevumus.")
    return []


def save_tasks():
    """Saglabā visus uzdevumus failā."""
    data = list(listbox.get(0, tk.END))
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        messagebox.showerror("Kļūda", "Neizdevās saglabāt uzdevumus.")


def add_task():
    text = entry.get().strip()
    if text == "":
        messagebox.showwarning("Brīdinājums", "Ievadi uzdevumu!")
        return

    listbox.insert(tk.END, text)
    entry.delete(0, tk.END)
    save_tasks()


def delete_task():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("Brīdinājums", "Izvēlies uzdevumu, ko dzēst!")
        return

    listbox.delete(sel[0])
    save_tasks()


root = tk.Tk()
root.title("Uzdevumu plānotājs")
root.geometry("420x320")

tk.Label(root, text="Ievadi uzdevumu:").pack(pady=(15, 5))

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Pievienot", command=add_task, width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Dzēst", command=delete_task, width=12).grid(row=0, column=1, padx=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# ielādējam uzdevumus startā
for task in load_tasks():
    listbox.insert(tk.END, task)

root.mainloop()



