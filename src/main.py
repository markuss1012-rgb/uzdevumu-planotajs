import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"
DONE_PREFIX = "✅ "


def load_tasks():
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


def toggle_done():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("Brīdinājums", "Izvēlies uzdevumu, ko atzīmēt!")
        return

    index = sel[0]
    text = listbox.get(index)

    if text.startswith(DONE_PREFIX):
        new_text = text[len(DONE_PREFIX):]
    else:
        new_text = DONE_PREFIX + text

    listbox.delete(index)
    listbox.insert(index, new_text)
    listbox.selection_set(index)

    save_tasks()


root = tk.Tk()
root.title("Uzdevumu plānotājs")
root.geometry("460x340")

tk.Label(root, text="Ievadi uzdevumu:").pack(pady=(15, 5))

entry = tk.Entry(root, width=45)
entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Pievienot", command=add_task, width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Dzēst", command=delete_task, width=12).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Izpildīts", command=toggle_done, width=12).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

for task in load_tasks():
    listbox.insert(tk.END, task)

root.mainloop()
