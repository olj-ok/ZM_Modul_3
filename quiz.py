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

    def __init__(self, fragen):
        self.fragen         = fragen
        self.frage_aktuell  = None
        
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
        if auswahl == self.frage_aktuell["antwort"]:
            self.punkte += 1
            self.showinfo("Ergebnis", "Richtig!")
        else:
            self.showerror("Ergebnis", f"Falsch! Richtige Antwort: {self.frage_aktuell["antwort"]}")
            
        self.nexte_frage()
        
    def clear_buttons(self):
        for widget in self.frame_buttons.winfo_children():
            widget.destroy()

    def add_buttons(self, optionen):
        for option in optionen:
            antwort_char = option.split(")")[0]
            
            btn = tk.Button(self.frame_buttons, text=option, height=2, width=40, anchor="w", command=lambda a=antwort_char: self.überprüfe_antwort(a))
            btn.pack(pady=5)

    def showinfo(self, title, message):        
        messagebox.showinfo(title, message, master=self.root)

    def showerror(self, title, message):        
        messagebox.showerror(title, message, master=self.root)
            
    def result(self):
        
        self.frage_label.config(text="Quiz beendet")        
        self.clear_buttons()

        # 90% - grün, sonst rot        
        farbe = "green" if self.punkte / len(self.fragen) > 0.9 else "red"
        
        tk.Label(self.frame_buttons, text=f"Dein Punktestand: {self.punkte}/{len(self.fragen)}", font=("Arial", 12), fg=farbe).pack()
        
        tk.Button(self.frame_buttons, text="Neuer Test", width=20, command=self.new_test).pack(pady=(20, 0))
        tk.Button(self.frame_buttons, text="Beenden", width=20, command=self.root.quit).pack(pady=(10, 0))
                
    def frage_generator(self):
        for frage in self.fragen:
            yield frage
            
    def nexte_frage(self):
        
        try:            
            self.frage_aktuell = next(self.frage)
            self.frage_label.config(text=self.frage_aktuell["frage"])
            self.clear_buttons()
            self.add_buttons(self.frage_aktuell["optionen"])
        except StopIteration:
            self.result()
            return

    def new_test(self):        
        self.punkte = 0
        self.frage  = self.frage_generator()        
        self.nexte_frage()

    def start(self):
        self.new_test()
        self.root.mainloop()

Quiz(quiz_fragen).start()