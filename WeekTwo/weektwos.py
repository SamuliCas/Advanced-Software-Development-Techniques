import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import winsound

# -laadi Ernestille yksi mustikkapiirakka, joka on 1000x1000 kokoinen matriisi, 
# jossa joka toisessa solussa on lukuarvo 1 mustikan merkiksi. 
# Voit käyttää myös jotakin muuta lukuarvoa mustikan merkkinä.
 
mustikkapiirakka = np.zeros((1000,1000))
mustikkapiirakka[::2, ::2] = 1
mustikkapiirakka[1::2, 1::2] = 1
# print("\n",mustikkapiirakka)

# -vastaavasti laadi Kernestille yksi puolukkapiirakka, joka on saman kokoinen 1000x1000, 
# mutta jossa joka kolmannessa on lukuarvo 2 puolukan merkiksi. 
# Samoin tässä voit käyttää muutakin lukuarvoa puolukan merkkinä.
puolukkapiirakka = np.zeros((100,100))
puolukkapiirakka[::3, ::3] = 2
puolukkapiirakka[1::3, 1::3] = 2
#print("\n",puolukkapiirakka)

# -näytä kuvaajana sekä Ernestin mustikkapiirakka että Kernestin puolukkapiirakka siten, 
# että Ernestin piirakka näyttää totta tosiaan siniseltä ja Kernestin punaiselta
# plt.matshow(mustikkapiirakka, cmap='Blues')
# plt.matshow(puolukkapiirakka, cmap='Reds') 
# plt.colorbar()
# plt.show()

# luo rakenne, joka tiputtaa Ernestin pulloon yksi tippa kerrallaan maitoa 10 sekunnin aikana. 
# Havainnollista vapaasti valitsemallasi tavalla sitä, miten pullossa pinnan korkeus kasvaa vaiheittain
# Alustetaan pullo ja maito
pullo_korkeus = 10  # Pullokorkeus (cm)
pullo_leveys = 5    # Pulloleveys (cm)
maidon_tippa_koko = 0.1 # Yhden tipan tilavuus (cm^3)
maidon_tippa_asteittain = np.linspace(0, maidon_tippa_koko, num=100)  # Simuloi maidon tippumista pienissä osissa
maidon_tippojen_maara = len(maidon_tippa_asteittain)

# Alustetaan kuva ja akselit
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * pullo_leveys)
ax.set_ylim(0, pullo_korkeus)
ax.set_xlabel('Pulloleveys (cm)')
ax.set_ylabel('Pullokorkeus (cm)')

# Alustetaan pinnan korkeus ja pullo
pinnan_korkeus = [0]  # Käytetään listaa, joka mahdollistaa muutokset sisällä funktion
pinnan_korkeus2 = [0]  # Pullon 2 pinnan korkeus

pullo = plt.Rectangle((0, 0), pullo_leveys, pullo_korkeus, fill=False, color='blue')
pullo2 = plt.Rectangle((pullo_leveys, 0), pullo_leveys, pullo_korkeus, fill=False, color='green', label='Pullo 2')

ax.add_patch(pullo)
ax.add_patch(pullo2)


# Alustetaan toiminta, joka päivittää animaation kehystä
def update(frame):
    if frame < maidon_tippojen_maara:
        pinnan_korkeus[0] += maidon_tippa_asteittain[frame]
        pullo.set_height(pinnan_korkeus[0])

        pinnan_korkeus2[0] += maidon_tippa_asteittain[frame]
        pullo2.set_height(pinnan_korkeus2[0])

        
        # Evästauon jälkeen matka jatkuu ja alkaa janottamaan.
        # -tee toiminto, joka kaataa tippa kerrallaan Ernestin maitopullosta maitoa Ernestin kurkkuun. 
        # Havainnollista asiaa jollakin tavalla, ja määritä toimintoon "nielaisun" ääni aina kun 100 tippaa on nautittu.
        # -tee sama Kernestin maidon nauttmisen havainnollistamiseksi.
        # Tarkista, onko juotu 10 tippaa, ja toista ääni
        if (frame + 1) % 10 == 0:
            winsound.Beep(440, 1000)
    
    return pullo, pullo2

# Luo animaatio
ani = FuncAnimation(fig, update, frames=range(maidon_tippojen_maara), repeat=False, blit=True)

# Näytä animaatio
plt.legend()
# plt.show()

# Seuraavaksi Ernesti ja Kernesti lähtevät kiipeämään ylämäkeen kohti näköalatornia. 
# Molemmat näkevät kaukana edessä siintelevän tornin, jonka huipulla liehuu lippu jossa on numero 5.
# Ernesti ja Kernesti ovat hyvällä tuulella, ja mennessään laskeskelevat yhdessä asioita jotka liittyvät numero viitoseen.
# -tee toiminto, joka tarkastelee järjestyksessä piin likiarvoa (desimaaleja) järjestyksessä sekunnin välein, 
# ja aina kun löytyy seuraava "viitonen", ohjelma soittaa äänimerkin


# # Laske pi:n desimaalit (tässä vain esimerkkidata)
# pi_desimaalit = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

# # Määritä aikaväli sekunneissa
# aikavali = 1

# # Käy läpi pi:n desimaalit järjestyksessä
# for i in range(2, len(pi_desimaalit)):
#     if pi_desimaalit[i] == '5':
#         print("Löytyi viitonen!")
#         # Soita äänimerkki (Windows-käyttäjille)
#         winsound.Beep(1000, 500)  # Taajuus 1000 Hz, kesto 500 ms
#         # Unix-käyttäjille voit käyttää seuraavaa riviä äänimerkin soittamiseen:
#         # os.system('play --no-show-progress --null --channels 1 synth 0.5 sine 1000')  # Vaatii "sox"-paketin

#     # Nukutaan aikavälin verran sekunteja
#     time.sleep(aikavali)

# # -tee toiminto, jossa Ernesti leikkaa NxN kokoisen palasen (N=satunnaisluku väliltä 1-100) 
# # piirakasta jolloin piirakka-matriisin lukuarvot kyseisiltä kohdilta muuttuvat nolliksi. 
# # Näytä miltä piirakka näyttää yhden palasen leikkaamisen jälkeen.
# # -tee sama Kernestille. Näytä hänen piirakkansa vastaavasti palasen leikkaamisen jälkeen.

def leikkaa_palaa(piirakka, pelaaja):
    # Arvotaan satunnainen koko N
    N = np.random.randint(1, 101)
    
    # Valitaan satunnainen aloituspiste
    x = np.random.randint(0, piirakka.shape[0] - N + 1)
    y = np.random.randint(0, piirakka.shape[1] - N + 1)
    
    # Leikataan pala ja asetetaan arvot nolliksi
    leikattu_pala = piirakka[x:x+N, y:y+N]
    piirakka[x:x+N, y:y+N] = 0
    
    print(f"{pelaaja} leikkasi palan koko {N}x{N} koordinaateista ({x}, {y}).")
    
    return piirakka

def update_ernesti(piirakka):
    return leikkaa_palaa(piirakka, "Ernesti")

def update_kernesti(piirakka):
    return leikkaa_palaa(piirakka, "Kernest")

# Ernesti leikkaa palan
ernesti_leikkaus = leikkaa_palaa(mustikkapiirakka.copy(), "Ernesti")

# Kernest leikkaa palan
kernest_leikkaus = leikkaa_palaa(puolukkapiirakka.copy(), "Kernest")

# Näytä piirakat leikkaamisen jälkeen
# plt.matshow(ernesti_leikkaus, cmap='Blues')
# plt.matshow(kernest_leikkaus, cmap='Reds')
# plt.colorbar()
# plt.show()



# Matka jatkuu tasaisen väsyttävänä ja jotenkin tutun tuntoisena ylämäkenä.
# -jatka evästaukoja ja maidon juomista 10 sekunnin välein (tai nopeammin) kunnes molempien eväät ja maito on juotu
maksimi_maitotippojen_maara = maidon_tippojen_maara

# Evästauot ja maidon juonti
while (np.any(ernesti_leikkaus) or np.any(kernest_leikkaus)) or maksimi_maitotippojen_maara > 0:
    # Tehdään evästauko 1 sekunnin välein
    print("Evästauko!")
    time.sleep(1)

    if np.any(ernesti_leikkaus):
        ernesti_leikkaus = leikkaa_palaa(ernesti_leikkaus, "Ernesti")

    if np.any(kernest_leikkaus):
        kernesti_leikkaus = leikkaa_palaa(kernest_leikkaus, "Kernest")

    # Juodaan maito 1 sekunnin välein
    print("Maidon  juonti!")
    time.sleep(1)

    # Tarkista, onko juotu 100 tippaa, ja toista ääni
    for _ in range(1):  # 10 tippaa joka 10 sekunnissa
        for i in range(10):  # 10 tippaa kerrallaan
            ernesti_leikkaus = update_ernesti(ernesti_leikkaus)
            kernest_leikkaus = update_kernesti(kernesti_leikkaus)
            maksimi_maitotippojen_maara -= 1
        winsound.Beep(440, 1000)  # Äänimerkki joka 100 tipan jälkeen

print("Eväät ja maito on juotu!")

# Näytä lopuksi matriisit
plt.matshow(ernesti_leikkaus, cmap='Blues')
plt.matshow(kernest_leikkaus, cmap='Reds')
plt.colorbar()
plt.show()
# Kun kaikki eväät on syöty ja maito juotu, havaitsette saapuneenne mäellä olevan tornin juurelle. 
# Torniin menevät tikkaat, joissa on 5 askelmaa. Torniin kiipeäminen tulee suorittaa silmät kiinni - 
# eli Ernesti ja Kernesti eivät näe toisiaan.
# -Havainnollista Ernestin ja Kernestin torniin kiipeämistä seuraavasti seuraavasti:
# -Ensin Ernesti pohtii että nousiko ensin 1. vai 2. askelmalle ja sen hän sitten tekee
# -Tämän jälkeen Kernesti pohtii samaa ja nousee askelmalle
# -Jos Ernesti ja Kernesti osuvat samalle askelmalle, he putoavat molemmat alas ja homma alkaa alusta
# -Toista ylläolevaa niin kauan, että sekä Ernesti ja Kernesti pääsevät molemmat torniin perille. 
# Ilmaise montako sekuntia torniin pääsy oikein vaati - jos ajatellaan että yksi "nousuvuoro"  kestää aina yhden sekunnin.