#Tehdään tkinteriä ja säikeistystä

print ("...")

import tkinter as tk
import time
import winsound
import threading
import numpy as np
import psutil

ikkuna=tk.Tk()
ikkuna.title("Käyttöliittymä, jossa on säikeytystoiminnallisuutta...")
ikkuna.geometry("650x300")

koriste={}
for i in range(10):
    koriste[i]=tk.Label(ikkuna,text="")
    koriste[i].grid(row=i,column=i)

ernestin_muuttuja_naytolla=tk.StringVar()
ernestin_muuttuja_naytolla.set("------")

kernestin_muuttuja_naytolla=tk.StringVar()
kernestin_muuttuja_naytolla.set("------")

cpu_muuttuja_naytolla=tk.StringVar()
cpu_muuttuja_naytolla.set("------")

pid=psutil.Process().pid

threads_naytolla=tk.StringVar()
threads_naytolla.set("------")

def paivita_threads():
    while True:
        threads_maara= psutil.Process(pid).num_threads()
        threads_naytolla.set(f"Threads maara: {threads_maara}")
        time.sleep(1)

threads = threading.Thread(target=paivita_threads)
threads.daemon = True
threads.start()

thread=tk.Label(ikkuna,textvariable=threads_naytolla,bg="yellow",width=30,anchor='w')
thread.grid(row=6,column=2)

def paivita_cpu_kuormitus():
    while True:
        cpu_kuorma = psutil.cpu_percent(interval=1)
        cpu_muuttuja_naytolla.set(f"CPU kuorma: {cpu_kuorma}%")
        time.sleep(1)

cpu_thread = threading.Thread(target=paivita_cpu_kuormitus)
cpu_thread.daemon = True
cpu_thread.start()

cpu_kuormitus=tk.Label(ikkuna,textvariable=cpu_muuttuja_naytolla,bg='blue',width=30,anchor='w')
cpu_kuormitus.grid(row=5,column=2)

def ernesti_heita_tomaatti():
    for i in range(8):
        print("o-",i)
        temp=np.random.randint(0,100)
        ernestin_muuttuja_naytolla.set(f"{temp}+{temp*'-'}->")
        # lisataan jokin raskas suoritusasia....
        A=np.ones((100,100))
        B=np.matmul(A,A)
        #...raskas osio loppuu
        time.sleep(0.1)
        winsound.Beep(500,100)
    print("...heit...heit")
    print(slider.get())
    winsound.Beep(300,500)

# tehdään funktio, joka luo tomaatinheittosäikeen Ernestiä varten ja myös ajaa sen...
def luo_ja_aja_saie_tomaatinheittoa_varten_ernestille():
    #luonti
    t=threading.Thread(target=ernesti_heita_tomaatti) 
    #käynnistys
    t.start()

ernesti_painike=tk.Button(ikkuna,text="Ernesti",command=luo_ja_aja_saie_tomaatinheittoa_varten_ernestille)
ernesti_painike.grid(row=1,column=1)

ernesti_teksti=tk.Label(ikkuna,textvariable=ernestin_muuttuja_naytolla,bg='green',width=80,anchor='w')
ernesti_teksti.grid(row=1,column=2)

# *******************************************************
# *******************************************************

def kernesti_heita_tomaatti():
    for i in range(8):
        print("o-",i)        
        temp=np.random.randint(0,100)
        kernestin_muuttuja_naytolla.set(f"{temp}+{temp*'-'}->")
        time.sleep(0.1)
        winsound.Beep(700,100)
    print("...heit...heit")
    winsound.Beep(300,500)

# tehdään funktio, joka luo tomaatinheittosäikeen Ernestiä varten ja myös ajaa sen...
def luo_ja_aja_saie_tomaatinheittoa_varten_kernestille():
    #luonti
    t=threading.Thread(target=kernesti_heita_tomaatti) 
    #käynnistys
    t.start()

kernesti_painike=tk.Button(ikkuna,text="Kernesti",command=luo_ja_aja_saie_tomaatinheittoa_varten_kernestille)
kernesti_painike.grid(row=3,column=1)

kernesti_teksti=tk.Label(ikkuna,textvariable=kernestin_muuttuja_naytolla,bg='red',width=80,anchor='w')
kernesti_teksti.grid(row=3,column=2)

slider = tk.Scale(ikkuna, from_=0, to=100, orient=tk.HORIZONTAL)
slider.grid(row=11, column=2)

#lisätään ohjauspainike

def ohjauskeskus():
    while 1:
        #tässä on koodia joka ohjaa tomaatinheittoa...
        print("...ohjati...ohjati...ohjati")
        #tarkastellaan montako threadia pitäisi olla...
        saie_tavoite_maara=slider.get()
        print(saie_tavoite_maara)
        cpu_kuormitus_str = cpu_muuttuja_naytolla.get()
        cpu_kuormitus_parts = cpu_kuormitus_str.split(":")
        
        if len(cpu_kuormitus_parts) > 1:
            cpu_kuormitus = float(cpu_kuormitus_parts[1].strip()[:-1])
        
        #jos tällä hetkellä säikeitä vähemmän kuin tavoite, niin...
            if saie_tavoite_maara<cpu_kuormitus:
                print("Nyt tulisi tehdä lisää kuormitusta...")
                luo_ja_aja_saie_tomaatinheittoa_varten_ernestille()
        
        time.sleep(1)

ohjaus=tk.Button(ikkuna,text="Ohjaa",command=ohjauskeskus)
ohjaus.grid(row=9,column=1)

ohjaus_saie=threading.Thread(target=ohjauskeskus)
ohjaus_saie.start()

ikkuna.mainloop()