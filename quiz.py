import tkinter as tk
from tkinter import ttk, messagebox

# Quizfragen und Antworten
quiz_fragen = (
    {
        "frage": "Was bewirkt wrap='none' in einem Tkinter Text-Widget?",
        "optionen": (
            "A) Aktiviert automatische Zeilenumbrüche", 
            "B) Deaktiviert automatische Zeilenumbrüche", 
            "C) Ermöglicht Umbruch bei Leerzeichen", 
            "D) Schneidet Text am Rand ab"
        ),
        "antwort": "B"
    },
    {
        "frage": "Welches Modul wird für QR-Codes in Python verwendet?",
        "optionen": (
            "A) qrtools", 
            "B) qrcode", 
            "C) pyqrcode", 
            "D) barcode",
            "F) qrcodes",
            "G) qrcodegenerator"
        ),
        "antwort": "C"
    },
    {
        "frage": "Welche Funktion speichert ein QR-Code als PNG?",
        "optionen": (
            "A) qr.save()", 
            "B) qr.generate()", 
            "C) qr.png()", 
            "D) qr.export()"
        ),
        "antwort": "C"
    },
    {
        "frage": "Welches Widget wird für Scrollbars in Tkinter verwendet?",
        "optionen": (
            "A) ScrollFrame", 
            "B) ttk.Scroll", 
            "C) tk.Scrollbar", 
            "D) tk.Scroll"
        ),
        "antwort": "C"
    }
)

class Quiz():

    def __init__(self, quiz_fragen):
        self.punkte      = 0
        self.frage_index = -1
        self.fragen = quiz_fragen
        
        self.init_gui()

    def init_gui(self):        
        self.root = tk.Tk()
        self.root.title("Python Quiz")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        self.frage_label = ttk.Label(self.root, text="", font=("Arial", 14), wraplength=450)
        self.frage_label.pack(pady=20)

        self.frame_buttons = ttk.Frame(self.root)
        self.frame_buttons.pack(pady=20)

    def überprüfe_antwort(self, auswahl):        
        richtige_antwort = self.fragen[self.frage_index]["antwort"]
        
        if auswahl == richtige_antwort:
            self.punkte += 1
            messagebox.showinfo("Ergebnis", "✅ Richtig!")
        else:
            messagebox.showerror("Ergebnis", f"❌ Falsch! Richtige Antwort: {richtige_antwort}")
            
        self.nexte_frage()
        
    def clear_buttons(self):
        for widget in self.frame_buttons.winfo_children():
            widget.destroy()

    def add_buttons(self, optionen):
        for option in optionen:
            antwort_char = option.split(")")[0]
            btn = ttk.Button(self.frame_buttons, text=option, width=40, command=lambda a = antwort_char: self.überprüfe_antwort(a))
            btn.pack(pady=5)

    def result(self):
        messagebox.showinfo("Quiz beendet", f"Dein Punktestand: {self.punkte}/{len(self.fragen)}")        
                
        if messagebox.askyesno("Noch einmal?", "Möchtest du neue Test machen?"):
            self.new_test()
        else:
            self.root.quit()
            
    def nexte_frage(self):
        self.frage_index += 1
        
        if self.frage_index == len(self.fragen):
            self.result()
            return
        
        frage = self.fragen[self.frage_index]        
        self.frage_label.config(text=frage["frage"])
        
        self.clear_buttons()
        self.add_buttons(frage["optionen"])

    def new_test(self):
        self.frage_index = -1
        self.punkte      = 0
        self.nexte_frage()

    def start(self):
        self.new_test()
        self.root.mainloop()

Quiz(quiz_fragen).start()