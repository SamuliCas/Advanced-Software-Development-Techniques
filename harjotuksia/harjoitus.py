import tkinter
import winsound
from PIL import Image,ImageTk

print("... toimikohan tämän ollenkaan?")

ikkuna=tkinter.Tk()

#määritykset:
ikkuna.title("Oma ihan ensimmäinen käyttöliittymäni")
ikkuna.geometry("600x600")

erne_image=Image.open('erne.png')
erne_photo=ImageTk.PhotoImage(erne_image)

#määritellään funktiot
def sano_jotakin():
    print("Hepskukkuu!")
    winsound.Beep(440,500)

def sano_jotakin_muuta():
    print("...muuta..puuta")
    winsound.Beep(300,400)

#tähän väliin tärkeää omaa koodia
painike=tkinter.Button(ikkuna,text="OK",command=sano_jotakin)
painike.grid(row=0,column=0)

painike_2=tkinter.Button(ikkuna,text="Muuta",command=sano_jotakin_muuta)
painike_2.grid(row=1,column=1)

tekstijuttu=tkinter.Label(ikkuna,text="Otsikko tälle asialle...")
tekstijuttu.grid(row=0,column=1)

ernestin_kuva=tkinter.Label(ikkuna, image=erne_photo)
ernestin_kuva.place(x=200, y=200)

#tärkeä kohta loppuun...
ikkuna.mainloop()