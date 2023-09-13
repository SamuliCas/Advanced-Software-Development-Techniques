import tkinter
import winsound
from PIL import Image,ImageTk
import random

ikkuna=tkinter.Tk()

ikkuna.title("Ikkuna")
ikkuna.geometry("1000x800")

Kerne_image=Image.open('kerne.png')
Kerne_photo=ImageTk.PhotoImage(Kerne_image)

Maalitaulu_image=Image.open('maalitaulu.png')
Maalitaulu_photo=ImageTk.PhotoImage(Maalitaulu_image)

def sano_jotakin():
    print("Hepskukkuu!")
    winsound.Beep(440,500)

Kernestin_kuva=tkinter.Label(ikkuna, image=Kerne_photo)
Kernestin_kuva.place(random)

Maalitaulu_kuva=tkinter.Label(ikkuna, image=Maalitaulu_photo)
Maalitaulu_kuva.place(x=500, y=50)

painike=tkinter.Button(ikkuna,text="OK",command=sano_jotakin)
painike.grid(row=0,column=0)

ikkuna.mainloop()