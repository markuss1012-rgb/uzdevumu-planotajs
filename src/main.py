import tkinter as tk
from tkinter import messagebox


def add_task():
    text = entry.get().strip()
    if text == "":
        messagebox.showwarning("Brīdinājums", "Ievadi uzdevumu!")
        return
    listbox.insert(tk.END, text)
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Uzdevumu plānotājs")
root.geometry("400x300")

label = tk.Label(root, text="Ievadi uzdevumu:")
label.pack(pady=(15, 5))

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

add_button = tk.Button(root, text="Pievienot", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=8)
listbox.pack(pady=10)

root.mainloop()

