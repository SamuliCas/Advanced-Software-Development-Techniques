import tkinter as tk
import winsound
from PIL import Image,ImageTk
import random

#-luo ohjelma, joka asemoi tkinter-ikkunaan Kernestin kuvan vasempaan reunaan 
#satunnaiseen sijaintiin ja maalitaulun kuvan oikeaan reunaan vakiosijaintiin

#-laadi tkinter-painike, joka sijoittaa aina sitä painettaessa Ernestin 
#kuvan vasempaan reunaan uudestaan satunnaiseen paikkaan

#-laadi painike, jota painettaessa Ernestin kuvan kohdalta lähteee tomaatti kohti maalitaulua. 
#Yksinkertaisimmillaan tomaatti lähtee Ernestin kuvan kohdalta vaakasuorassa oikealle kohti maalitaulua. 
#Halutessasi lisää jokin "heittokaari" -ilmiö asiaan. 
#Lisäksi - jos osaat - lisää sopiva ääniefekti kuvaamaan tomaatin lentoa.

#-laadi toiminto, joka ilmaisee osuiko tomaatti maalitauluun vai ei. 
#Mikäli osuma syntyi, luo ääniefekti ja tallenna osumatieto


#luodaan ikkuna
ikkuna=tk.Tk()
ikkuna.title("Ikkuna")
ikkuna.geometry("1000x800")

Kerne_image=Image.open('C:/ASDT/weekthree/kerne.png')
Kerne_photo=ImageTk.PhotoImage(Kerne_image)

Maalitaulu_image=Image.open('C:/ASDT/weekthree/maalitaulu.png')
Maalitaulu_photo=ImageTk.PhotoImage(Maalitaulu_image)

Erne_image=Image.open('C:/ASDT/weekthree/erne.png')
Erne_photo=ImageTk.PhotoImage(Erne_image)

Tomaatti_image=Image.open('C:/ASDT/weekthree/tomaatti.png')
Tomaatti_photo=ImageTk.PhotoImage(Tomaatti_image)

def place_kerne_randomly():
    random_x = random.randint(10, 400) 
    random_y = random.randint(10, 600)  
    Kernestin_kuva.place(x=random_x, y=random_y)

def place_erne_randomly():
    random_x = random.randint(10, 400)
    random_y = random.randint(10, 600) 
    Ernestin_kuva.place(x=random_x, y=random_y)

def move_tomato():
    x_start = Ernestin_kuva.winfo_x() + Erne_image.width // 2
    y_start = Ernestin_kuva.winfo_y() + Erne_image.height // 2
    x_target = Maalitaulu_kuva.winfo_x() + Maalitaulu_image.width // 2
    y_target = Maalitaulu_kuva.winfo_y() + Maalitaulu_image.height  // 2

    # Calculate the horizontal distance and the number of steps
    distance_x = x_target - x_start
    num_steps = abs(distance_x) // 10  # Adjust the step size as needed

    # Move the tomato horizontally
    for step in range(num_steps):
        x = x_start + (step * distance_x) // num_steps
        Tomaatti_kuva.place(x=x, y=y_start)
        ikkuna.update()  # Update the window to show the new position
        ikkuna.after(50)  # Delay for smoother animation (adjust as needed)

    # Ensure the tomato reaches the target
    Tomaatti_kuva.place(x=x_target, y=y_start)


Kernestin_kuva=tk.Label(ikkuna, image=Kerne_photo)
place_kerne_randomly()

Ernestin_kuva=tk.Label(ikkuna, image=Erne_photo)
place_erne_randomly()

Maalitaulu_kuva=tk.Label(ikkuna, image=Maalitaulu_photo)
Maalitaulu_kuva.place(x=500, y=50)

Tomaatti_kuva=tk.Label(ikkuna, image=Tomaatti_photo)

painike=tk.Button(ikkuna,text="Sijoita Erne",command=place_erne_randomly)
painike.grid(row=0,column=0)

painike2=tk.Button(ikkuna,text="Heitä tomaatti",command=move_tomato)
painike2.grid(row=1,column=0)


ikkuna.mainloop()