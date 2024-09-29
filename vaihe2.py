import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import time
import winsound

# PÄÄIKKUNAN JUTSKAT
root = tk.Tk()
root.title("Höpö höpö maailma")

# APUHUUTO
lause = "Ernesti ja Kernesti tässä terve! Olemme autiolla saarella, voisiko joku tulla sieltä sivistyneestä maailmasta hakemaan meidät pois! Kiitos!"
sanat = lause.split()

apina1_sana = sanat[0] if len (sanat) > 0 else ""
apina2_sana = sanat[0] if len (sanat) > 0 else ""

# FOTO_LOADER
def lataa_kuva(tiedostonimi):
    kuva_polku = os.path.join(os.path.dirname(os.path.abspath(__file__)), tiedostonimi)
    
    if os.path.exists(kuva_polku):
        kuva = Image.open(kuva_polku)
        return ImageTk.PhotoImage(kuva)
    else:
        print(f"Tiedostoa ei löydy: {kuva_polku}")
        return None
    
# ERNESTIN APINA
def apina_ui1(apina, apina_teksti, canvas, start_x, start_y):
    def apina1_liikkuu():
        current_x = start_x
        kilometrin_vali = 8  # 1 km = 8 pikseliä (long math)
        total_distance = 800  # apina kulkee 800 pikseliä et tiiätte
        beep_count = total_distance // kilometrin_vali  # piip :D

        for _ in range(beep_count):
            time.sleep(0.1)
            current_x += kilometrin_vali
            canvas.move(apina, kilometrin_vali, 0)
            canvas.move(apina_teksti, kilometrin_vali, 0)

            # Kilometri piippaus
            winsound.Beep(1000, 100)

        # Apina saapui perille peep
        winsound.Beep(2000, 500)

    print("Ernestin apina lähtee matkalle.")
    threading.Thread(target=apina1_liikkuu).start()

# KERNESTIN APINA
def apina_ui2(apina, apina_teksti, canvas, start_x, start_y):
    def apina2_liikkuu():
        current_x = start_x
        kilometrin_vali = 8  # 1 km = 8 px
        total_distance = 800  # apina kulkee 800 px
        beep_count = total_distance // kilometrin_vali  # piip :D

        for _ in range(beep_count):
            time.sleep(0.1)
            current_x += kilometrin_vali
            canvas.move(apina, kilometrin_vali, 0)
            canvas.move(apina_teksti, kilometrin_vali, 0)

            # Kilometri piippaus
            winsound.Beep(1000, 100)

        # Apina saapui perille peep
        winsound.Beep(2000, 500)

    print("Kernestin apina lähtee matkalle.")
    threading.Thread(target=apina2_liikkuu).start()

# CANVAS
canvas = tk.Canvas(root, width=1200, height=800)
canvas.pack()

vedenkuva = lataa_kuva("vesi.png")
if vedenkuva:
    canvas.create_image(600, 400, image=vedenkuva)

saari_kuva = lataa_kuva("saari.png")
if saari_kuva:
    canvas.create_image(100, 400, image=saari_kuva)

manner_kuva = lataa_kuva("kaupunni.png")
if manner_kuva:
    canvas.create_image(1100, 400, image=manner_kuva)

# APINA
apina_kuva = lataa_kuva("apina.png")
if apina_kuva:
    apina1 = canvas.create_image(200, 30, image=apina_kuva)
    apina1_teksti = canvas.create_text(200, 60, text=apina1_sana, fill="black")

    apina2 = canvas.create_image(200, 770, image=apina_kuva)
    apina2_teksti = canvas.create_text(200, 730, text=apina2_sana, fill="black")

#SAAREN NAPPULAT
nappi1 = tk.Button(root, text="Ernesti", command=lambda: apina_ui1(apina1, apina1_teksti, canvas, 200, 30))
nappi1.place(x=50, y=50)

nappi2 = tk.Button(root, text="Kernesti", command=lambda: apina_ui2(apina2, apina2_teksti, canvas, 200, 770))
nappi2.place(x=50, y=750)

#KÄYNNISTYS
root.mainloop()