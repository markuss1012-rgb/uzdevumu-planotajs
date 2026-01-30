import tkinter as tk

root = tk.Tk()
root.title("Uzdevumu plānotājs")
root.geometry("400x200")

label = tk.Label(root, text="Ievadi uzdevumu:")
label.pack(pady=(20, 5))

entry = tk.Entry(root, width=40)
entry.pack()

root.mainloop()
