import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.resizable(width=False, height=False)

root.title("Žaidimas Kas? Kur? Kada?")

canvas = tk.Canvas(root, width=400, height=250)
canvas.grid(columnspan=3, rowspan=1)

#Logo
logo = Image.open('logo3.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

from tkinter import *

def zaisk():
    new3 = Toplevel(root)
    new3.title("Žaidimas Kas? Kur? Kada?")
    new3.geometry('400x220')

    label_1 = tk.Label(master=new3, text="Atsakykite į klausimus:")
    label_1.grid(column=2, row=0)

    label_kada = tk.Label(master = new3, text = "Kada?")
    label_kada.grid(column = 1, row = 1, sticky = "e")
    text_kada = tk.Entry(master = new3, width = 55)
    text_kada.grid(column=2, row=1)
    
    label_kas = tk.Label(master = new3, text = "Kas?")
    label_kas.grid(column = 1, row = 2, sticky = tk.E)
    text_kas = tk.Entry(master=new3, width = 55)
    text_kas.grid(column=2, row=2)

    lbl_ka = tk.Label(master = new3, text="Ką?")
    lbl_ka.grid(column=1, row=3, sticky="e")
    text_ka = tk.Entry(master=new3, width=55)
    text_ka.grid(column=2, row=3)

    import random
    a = (
        "Afrikoje", 
        "Šiaurės ašigalyje", 
        "didžiausiam pasaulio užpakalyje", 
        "geriau neklausk kur", 
        "Nikaragvoje", 
        "Pabezdūnų kaime", 
        "Sėdmaišių karalystėje", 
        "senos raganos trobelėje", 
        "svečiuose pas Talibaną", 
        "Putino bunkeryje", 
        "pragare", 
        "srutų duobėje"
        )
    Kur = random.choice(a)
    b = (
        "Vaivorykštiniu vienaragiu", 
        "jo didenybe Radžiu", 
        "tavo motina", 
        "Nitanu Gauseda", 
        "mažuoju Hitleriu Gražuliu", 
        "bomžu", 
        "Daukantu", 
        "Olegu", 
        "visų ertmių gydytoju", 
        "žmogumi šaldytuvu", 
        "Voodoo lėle"
        )
    Su_kuo = random.choice(b)
    c = (
        "medžioja", 
        "patruliuoja", 
        "hipnotizuoja", 
        "operuoja", 
        "galvoja", 
        "ovuliuoja", 
        "svajoja apie", 
        "klaidžioja po", 
        "myli", 
        "draugiškai nekenčia", 
        "tiesiog stovi", 
        "apsimeta pavasariu"
        )
    Ka_veikia = random.choice(c)
    txt ="{}, {} {} su {} {} {} \n"

    def ats():
        
        framet = tk.Frame(master=new3, height=5)
        framet.grid(column=2, row=6)

        frame4 = tk.Frame(
            master=new3, 
            width=320, 
            height=105, 
            )
        frame4.grid(column=2, row=8)

        browse_text.set("Jūsų žaidimo atsakymas:")

        label_ats = tk.Label(
            master=frame4, 
            text=txt.format(
                text_kada.get(), 
                Kur, 
                text_kas.get(), 
                Su_kuo, 
                Ka_veikia, 
                text_ka.get()), 
                borderwidth= 10, 
                font="Arial 12 bold", 
                fg="red",
                wraplength=300,
                justify='center'
                )
        label_ats.grid(column= 2, row=1, sticky="nsew")

        failas = open("Zaidimo_istorija.txt", "a", encoding='utf-8-sig')
        failas.write(txt.format(text_kada.get(), Kur, text_kas.get(), Su_kuo, Ka_veikia, text_ka.get()))
        failas.close()

    framet = tk.Frame(master=new3, height=5)
    framet.grid(column=2, row=4)

    browse_text = tk.StringVar()
    btn_submit = tk.Button(
        master=new3, 
        textvariable=browse_text,
        command=lambda:ats(),
        padx=5
        )
    browse_text.set("Pateikti atsakymus")
    btn_submit.grid(column=2, row=5)

def skaityk():
    import os
    if os.path.isfile("Zaidimo_istorija.txt"):
                with open("Zaidimo_istorija.txt", encoding='utf-8-sig') as file:
                    failas = file.read()
    else:
                failas = "Žaidimo istorija neegzistuoja, Jūs, greičiausiai, dar nežaidėte nei vieno žaidimo."
    
    new = Toplevel(root)
    new.title("Žaidimo istorija")
    
    label_skaityk = tk.Label(new, text = failas, padx=5, pady=5)
    label_skaityk.pack()

def trink():
    import os
    try:
        if os.path.isfile("Zaidimo_istorija.txt"):
            os.remove("Zaidimo_istorija.txt")
            failas1 = "Žaidimo istorija sėkmingai ištrinta!"
            new2 = Toplevel(root)
            new2.title("Žaidimas ištrintas?")
            label_skaityk = tk.Label(new2, text = failas1, padx=5, pady=5)
            label_skaityk.pack()
        else:
            failas3 = "Žaidimo istorija neegzistuoja, Jūs, greičiausiai, dar nežaidėte nei vieno žaidimo."
            new2 = Toplevel(root)
            new2.title("Žaidimas ištrintas?")
            label_skaityk = tk.Label(new2, text = failas3, padx=5, pady=5)
            label_skaityk.pack() 

    except OSError as error:
        failas2 = "Ištrinti žaidimo istorijos nepavyko, pabandykite perkrauti savo kompiuterį. Gerai, gerai, juokauju!"
        new2 = Toplevel(root)
        new2.title("Žaidimas ištrintas?")
        label_skaityk = tk.Label(new2, text = failas2, padx=5, pady=5)
        label_skaityk.pack()   
    
def iseik():
    root.destroy()

frame1 = tk.Frame(master=root, width=400, height=300, padx=5, pady=5)
frame1.grid(columnspan=3, rowspan=7)

frame2 = tk.Frame(master=frame1, width=5, height=5)
frame2.grid(column=2, row=1)

button1 = tk.Button(
    master=frame1, 
    text="Žaisti žaidimą", 
    command=lambda:zaisk(), 
    font="Arial 12", 
    width=18, 
    height=3, 
    fg="gray"
    )
button1.config(bd=10, relief=RAISED)
button1.grid(column=1, row=0)
button2 = tk.Button(
    master=frame1, 
    text="Peržiūrėti ankstesnių\nžaidimų rezultatus", 
    command=lambda:skaityk(), 
    font="Arial", 
    width=18, 
    height=3,
    fg="gray"
    )
button2.config(bd=10, relief=RAISED)
button2.grid(column=1, row=2)
button3 = tk.Button(
    master=frame1, 
    text="Ištrinti buvusių\nžaidimų istoriją", 
    command=lambda:trink(), 
    font="Arial", 
    width=18, 
    height=3, 
    fg="gray"
    )
button3.config(bd=10, relief=RAISED)
button3.grid(column=3, row=0)
button4 = tk.Button(
    master=frame1, 
    text="Išeiti iš žaidimo", 
    command=lambda:iseik(),
    font="Arial", 
    width=18, 
    height=3, 
    fg="gray"
    )
button4.config(bd=10, relief=RAISED)
button4.grid(column=3, row=2)

root.mainloop()