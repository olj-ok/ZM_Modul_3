import tkinter as tk
from tkinter import ttk, messagebox
import random

# Quizfragen und Antworten (9 Fragen insgesamt)
quiz_fragen = [
    {
        "frage": "Was bewirkt wrap='none' in einem Tkinter Text-Widget?",
        "optionen": ["A) Aktiviert automatische Zeilenumbrüche", "B) Deaktiviert automatische Zeilenumbrüche", "C) Ermöglicht Umbruch bei Leerzeichen", "D) Schneidet Text am Rand ab"],
        "antwort": "B"
    },
    {
        "frage": "Welches Modul wird für QR-Codes in Python verwendet?",
        "optionen": ["A) qrtools", "B) qrcode", "C) pyqrcode", "D) barcode"],
        "antwort": "C"
    },
    {
        "frage": "Welche Funktion speichert ein QR-Code als PNG?",
        "optionen": ["A) qr.save()", "B) qr.generate()", "C) qr.png()", "D) qr.export()"],
        "antwort": "C"
    },
    {
        "frage": "Welches Widget wird für Scrollbars in Tkinter verwendet?",
        "optionen": ["A) ScrollFrame", "B) ttk.Scroll", "C) tk.Scrollbar", "D) tk.Scroll"],
        "antwort": "C"
    },
    {
        "frage": "Wie importiert man ein Modul in Python?",
        "optionen": ["A) include", "B) import", "C) require", "D) load"],
        "antwort": "B"
    },
    {
        "frage": "Was gibt die Funktion len() zurück?",
        "optionen": ["A) Die Länge eines Objekts", "B) Die Größe eines Objekts", "C) Beide", "D) Nichts"],
        "antwort": "A"
    },
    {
        "frage": "Welches Schlüsselwort wird zur Definition einer Funktion verwendet?",
        "optionen": ["A) func", "B) def", "C) function", "D) lambda"],
        "antwort": "B"
    },
    {
        "frage": "Wie schreibt man einen Kommentar in Python?",
        "optionen": ["A) # Kommentar", "B) // Kommentar", "C) <!-- Kommentar -->", "D) * Kommentar"],
        "antwort": "A"

    },
    {
        "frage": "Welches Statement beendet eine Schleife vorzeitig?",
        "optionen": ["A) exit", "B) break", "C) stop", "D) quit"],
        "antwort": "B"
    }
]

# Initialisierung der App
root = tk.Tk()
root.title("Python Quiz")
root.geometry("500x400")

# Punkte-Tracker und Index der aktuellen Frage
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
        # Aktualisiere den Text der Buttons und weise die entsprechende Antwort zu.
        buttons[i].config(text=frage["optionen"][i], command=lambda opt=chr(65+i): überprüfe_antwort(opt))

# UI-Elemente erstellen
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
