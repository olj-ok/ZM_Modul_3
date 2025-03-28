import tkinter as tk
from tkinter import ttk, messagebox
import random

# Quizfragen und Antworten
quiz_fragen = [
    {
        "frage": "Wie gibt man in Python etwas auf der Konsole aus?",
        "optionen": ["A) print ()", "B) get ()", "C) echo. ", "D) console.log"],
        "antwort": "A"
    },
    {
        "frage": "Welches Zeichen beginnt einen Kommentar in Python?",
        "optionen": ["A) --", "B) //", "C) #", "D) /*"],
        "antwort": "C"
    },
    {
        "frage": "Wie speichert man die Zahl 5 in einer Variable?",
        "optionen": ["A) int x = 5", "B) var x = 5", "C) x = 5", "D) 5 -> x"],
        "antwort": "C"
    },
    {
        "frage": "Was berechnet 3 + 2 * 4 in Python?",
        "optionen": ["A) 9", "B) 14", "C) 20", "D) 11"],
        "antwort": "D"
    },
    {"frage": "Wie erstellt man eine Liste mit den Zahlen 1, 2, 3?",
        "optionen": ["A) liste = [1, 2, 3]", "B) liste = (1, 2, 3) (Tuple)", "C) liste = {1, 2, 3} (Set)", "D) liste = 1, 2, 3 (Tuple ohne Klammern)"],
        "antwort": "A"}
    
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