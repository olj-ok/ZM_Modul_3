import tkinter as tk
from tkinter import ttk, messagebox
import random

# Quizfragen und Antworten
quiz_fragen = [
    {
        "frage": "Was bewirkt print()?",
        "optionen": ["A) Gibt den Text in () aus.", "B) Deaktiviert automatische Zeilenumbrüche", "C) Ermöglicht Umbruch bei Leerzeichen", "D) Schneidet Text am Rand ab"],
        "antwort": "A"
    },
    {
        "frage": "Welches Modul wird für GUI in Python verwendet?",
        "optionen": ["A) cowsay", "B) pandas", "C) pyqrcode", "D) tkinter"],
        "antwort": "D"
    },
    {
        "frage": "Welche Funktion wird für Benutzereingaben verwendet?",
        "optionen": ["A) open()", "B) input()", "C) print()", "D) read()"],
        "antwort": "B"
    },
    {
        "frage": "Wie setzt man die Fenstergröße in Tkinter auf 500x300 Pixel?",
        "optionen": ["A) root.resize(500, 300)", "B) root.dimensions(500, 300)", "C) root.geometry('500x300')", "D) root.size('500x300')"],
        "antwort": "C"
    },
    {
        "frage": "Wie kannst du mit pip das Paket pandas aus dem Python Package Index einrichten?",
        "optionen": ["A) pip get pandas", "B) pip add pandas", "C) pip import pandas", "D) pip install pandas"],
        "antwort": "D"
    },
]

# Initialisierung der App
root = tk.Tk()
root.title("Python Quiz")
root.geometry("500x400")

# Punkte-Tracker
punkte = 0
frage_index = 0
ausgewählte_fragen = random.sample(quiz_fragen, len(quiz_fragen))  # Fragen mischen

def überprüfe_antwort(auswahl):
    global frage_index, punkte
    richtige_antwort = ausgewählte_fragen[frage_index]["antwort"]
    
    if auswahl == richtige_antwort:
        punkte += 1
        messagebox.showinfo("Ergebnis", "✅ Richtig!")
    else:
        messagebox.showerror("Ergebnis", f"❌ Falsch! Richtige Antwort: {richtige_antwort}")
    
    frage_index += 1
    if frage_index < len(ausgewählte_fragen):
        lade_frage()
    else:
        messagebox.showinfo("Quiz beendet", f"Dein Punktestand: {punkte}/{len(quiz_fragen)}")
        root.quit()

def lade_frage():
    frage = ausgewählte_fragen[frage_index]
    frage_label.config(text=frage["frage"])

    for i in range(4):
        buttons[i].config(text=frage["optionen"][i], command=lambda opt=chr(65+i): überprüfe_antwort(opt))

# UI-Elemente
frage_label = ttk.Label(root, text="", font=("Arial", 14), wraplength=450)
frage_label.pack(pady=20)

buttons = []
for i in range(4):
    btn = ttk.Button(root, text="", width=40)
    btn.pack(pady=5)
    buttons.append(btn)

# Erste Frage laden
lade_frage()

# App starten
root.mainloop()
