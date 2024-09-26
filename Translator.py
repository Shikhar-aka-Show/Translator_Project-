from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text="type", src="English", dest="Hindi"):
    text1 = text 
    src1 = src 
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

def on_enter(e):
    button_change['background'] = 'purple'
    button_change['foreground'] = 'white'

def on_leave(e):
    button_change['background'] = '#4CAF50'
    button_change['foreground'] = 'white'

root = Tk()
root.title("Shikhar Trans")
root.geometry("500x700")
root.config(bg='GREY')

# Title label
lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"), bg="Grey")
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

# Source text label
lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), fg="purple", bg="grey")
lab_txt.place(x=100, y=100, height=20, width=300)

# Source text box
Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

# Language list
list_text = list(LANGUAGES.values())

# Source language combobox
comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("English")

# Translate button with style and hover effects
button_change = Button(frame, text="Translate", relief=RAISED, font=("Arial", 15, "bold"), bg="#4CAF50", fg="white", activebackground="blue", activeforeground="white", command=data)
button_change.place(x=170, y=300, height=40, width=150)
button_change.bind("<Enter>", on_enter)
button_change.bind("<Leave>", on_leave)

# Destination language combobox
comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("English")

# Destination text label
lab_txt = Label(root, text="Destination Text", font=("Time New Roman", 20, "bold"), fg="purple", bg="grey")
lab_txt.place(x=100, y=360, height=20, width=300)

# Destination text box
dest_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
