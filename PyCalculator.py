import customtkinter
from pynput import keyboard
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def main():
    gui=customtkinter.CTk()
    gui.title("Calcolatrice") 
    gui.resizable(False,False)
    gui.geometry("320x502")

    righe=8
    colonne=4

    for riga in range(righe):
        gui.rowconfigure(riga, weight=1)

    for colonna in range(colonne):
        gui.columnconfigure(colonna, weight=1)

    display=tk.StringVar()
    display.set("")

    display_label=tk.Label(gui, textvariable=display, bg="#1B1A1B", fg="white", font=("Arial",24),anchor="e")
    display_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

    max_caratteri=15

    def aggiungi(valore):
        testo=display.get()

        if testo.startswith("Errore"):
            display.set("")
            return
        
        if len(testo)>=max_caratteri:
            return
        
        if valore in "+-*/":
            if testo.endswith(("+","-","*","/")):
                return 
            elif testo=="":
                return
            
        display.set(testo+valore)

    def calcola():
        try:
            testo=display.get().replace(",", ".")
            if "++" in testo or "--" in testo or "**" in testo or "//" in testo:
                display.set("Errore")
                return
            risultato=eval(testo)
            if isinstance(risultato, float) and risultato==float('inf'):
                display.set("Errore Matematico")
            else:
                display.set(str(risultato))
        except ZeroDivisionError:
            display.set("Errore Matematico")
        except Exception as e:
            display.set("Errore")

    def _cancella():
        testo=display.get()
        if testo.startswith("Errore"):
            display.set("")
        else: 
            testo_cancellato=testo[:-1]
            display.set(testo_cancellato)

    def premuto(key):
        try:
            if key.char in '0123456789+-*/=':
                if key.char=='=':
                    calcola()
                else:
                    aggiungi(key.char)
            elif key.char==',':
                aggiungi(',')
        except AttributeError:
            if key==keyboard.Key.backspace:
                _cancella()
            elif key==keyboard.Key.enter:
                calcola()

    listener=keyboard.Listener(on_press=premuto)
    listener.start()

    ######################################################################################################

    zero=customtkinter.CTkButton(gui, text="0",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("0"))
    zero.grid(row=7, column=0,columnspan=2, sticky="nsew")

    virgola=customtkinter.CTkButton(gui, text=",",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi(","))
    virgola.grid(row=7, column=2, sticky="nsew")

    uguale=customtkinter.CTkButton(gui, text="=",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: calcola())
    uguale.grid(row=7, column=3, sticky="nsew")

    ######################################################################################################

    uno=customtkinter.CTkButton(gui, text="1",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("1"))
    uno.grid(row=6, column=0, sticky="nsew")

    due=customtkinter.CTkButton(gui, text="2",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("2"))
    due.grid(row=6, column=1, sticky="nsew")

    tre=customtkinter.CTkButton(gui, text="3",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("3"))
    tre.grid(row=6, column=2, sticky="nsew")

    piu=customtkinter.CTkButton(gui, text="+",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("+"))
    piu.grid(row=6, column=3, sticky="nsew")

    ######################################################################################################

    quattro=customtkinter.CTkButton(gui, text="4",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("4"))
    quattro.grid(row=5, column=0, sticky="nsew")

    cinque=customtkinter.CTkButton(gui, text="5",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("5"))
    cinque.grid(row=5, column=1, sticky="nsew")

    sei=customtkinter.CTkButton(gui, text="6",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15,  font=("Arial", 18), command=lambda: aggiungi("6"))
    sei.grid(row=5, column=2, sticky="nsew")

    meno=customtkinter.CTkButton(gui, text="-",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("-"))
    meno.grid(row=5, column=3, sticky="nsew")

    ######################################################################################################

    sette=customtkinter.CTkButton(gui, text="7",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("7"))
    sette.grid(row=4, column=0, sticky="nsew")

    otto=customtkinter.CTkButton(gui, text="8",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A", corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("8"))
    otto.grid(row=4, column=1, sticky="nsew")

    nove=customtkinter.CTkButton(gui, text="9",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("9"))
    nove.grid(row=4, column=2, sticky="nsew")

    per=customtkinter.CTkButton(gui, text="x",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("*"))
    per.grid(row=4, column=3, sticky="nsew")

    ######################################################################################################

    cancellatutto=customtkinter.CTkButton(gui,text="CE",width=20, height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=50, font=("Arial", 18), command=lambda: display.set(""))
    cancellatutto.grid(row=3,column=0,columnspan=2, sticky="nsew")

    cancella=customtkinter.CTkButton(gui, text="⌫",width=10,height=10,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=35, font=("Arial", 18), command=lambda: _cancella())
    cancella.grid(row=3, column=2, sticky="nsew")

    diviso=customtkinter.CTkButton(gui, text="/",width=20,height=20,fg_color="#0D0D0D",hover_color="#3C3A3A",corner_radius=15, font=("Arial", 18), command=lambda: aggiungi("/"))
    diviso.grid(row=3, column=3, sticky="nsew")

    ######################################################################################################

    gui.mainloop()

if __name__ == "__main__":
    main()
