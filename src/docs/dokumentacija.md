# Programmatūras projekta dokumentācija
## Prasību izpēte

Ikdienā skolēniem ir daudz uzdevumu, kurus viegli aizmirst vai sajaukt. Arī man bieži gadījās, ka uzdevumi bija pierakstīti dažādās vietās vai netika pierakstīti vispār.

Tāpēc radās ideja izveidot vienkāršu uzdevumu plānotāju, kur visi uzdevumi būtu vienuviet.

Mērķauditorija ir skolēni, kuri vēlas vienkārši pierakstīt un pārskatīt savus uzdevumus.

Programmatūras prasības

### Funkcionālās prasības
- Pievienot uzdevumu
- Dzēst uzdevumu
- Atzīmēt uzdevumu kā izpildītu
- Saglabāt uzdevumus failā
- Ielādēt uzdevumus, atverot programmu

### Nefunkcionālās prasības
- Programmai jābūt vienkāršai un viegli lietojamai
- Programma darbojas Windows vidē
- Programma izstrādāta Python valodā


## Projekta sākotnējā izveide

Darbu pie projekta sāku ar vienkārša grafiskā loga izveidi lai pārbaudītu kā darbojas Tkinter un vai programma pareizi atveras. Šajā posmā tika izveidots tikai logs un teksta ievades lauks kur vēlāk būs iespējams ievadīt uzdevumus.

## Uzdevumu pievienošana

Nākamajā posmā programmai pievienoju  pogu “Pievienot”, kas ļauj ievadīto tekstu pievienot uzdevumu sarakstam.

## Uzdevumu dzēšana

Programmai tika pievienota poga “Dzēst” kas ļauj izdzēst izvēlēto uzdevumu no saraksta. Ja lietotājs nav izvēlējies nevienu uzdevumu programma parāda brīdinājumu.
## Datu saglabāšana un ielāde

Lai uzdevumi nepazust'u pēc programmas aizvēršanas tika pievienota saglabāšana failā. Programma automātiski saglabā uzdevumu sarakstu `tasks.json` failā pēc pievienošanas vai dzēšanas. Atverot programmu uzdevumi tiek ielādēti no šī faila.
## Uzdevumu atzīmēšana kā izpildīti

Tika pievienota poga “Izpildīts”, kas ļauj izvēlēto uzdevumu atzīmēt kā izdarītu. Izpildītajiem uzdevumiem priekšā parādās “✅”. Nospiežot pogu vēlreiz, atzīme tiek noņemta.
## Programmas izpildfaila izveide

tika izveidots izpildfails (.exe). 
## Projektēšana

Projektā tika izmantota pakāpeniska izstrāde, sākot ar vienkāršu programmas logu un pamazām pievienojot jaunas funkcijas.

Izstrādes soļi:
1. Programmas loga izveide
2. Uzdevumu pievienošana
3. Uzdevumu dzēšana
4. Datu saglabāšana failā
5. Uzdevumu atzīmēšana kā izpildīti
## Programmatūras projektējums

Izmantotās tehnoloģijas:
- Python
- Tkinter
- JSON fails
- GitHub

Programmas logs sastāv no:
- teksta ievades lauka
- pogām “Pievienot”, “Dzēst”, “Izpildīts”
- uzdevumu saraksta
## Lietotāja ceļvedis

1. Atver programmu.
2. Teksta laukā ieraksti uzdevumu.
3. Nospied pogu “Pievienot”, lai uzdevums parādītos sarakstā.
4. Izvēlies uzdevumu un:
   - nospied “Dzēst”, lai to izdzēstu;
   - nospied “Izpildīts”, lai atzīmētu kā izdarītu.
5. Aizverot programmu, uzdevumi tiek saglabāti automātiski.
6. Atverot programmu atkārtoti, saglabātie uzdevumi tiek ielādēti.
## Programmas kods
7. import tkinter as tk
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





