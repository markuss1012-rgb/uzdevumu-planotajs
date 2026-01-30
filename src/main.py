import tkinter as tk
from tkinter import messagebox


def add_task():
    text = entry.get().strip()
    if text == "":
        messagebox.showwarning("Brīdinājums", "Ievadi uzdevumu!")
        return
    listbox.insert(tk.END, text)
    entry.delete(0, tk.END)


def delete_task():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("Brīdinājums", "Izvēlies uzdevumu, ko dzēst!")
        return
    listbox.delete(sel[0])


root = tk.Tk()
root.title("Uzdevumu plānotājs")
root.geometry("420x320")

label = tk.Label(root, text="Ievadi uzdevumu:")
label.pack(pady=(15, 5))

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_button = tk.Button(btn_frame, text="Pievienot", command=add_task, width=12)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(btn_frame, text="Dzēst", command=delete_task, width=12)
delete_button.grid(row=0, column=1, padx=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()


