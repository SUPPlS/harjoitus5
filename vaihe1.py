import tkinter as tk
from PIL import Image, ImageTk
import os

# PÄÄIKKUNAN JUTSKAT
root = tk.Tk()
root.title("Höpö höpö maailma")

# FOTO_LOADER
def lataa_kuva(tiedostonimi):
    kuva_polku = os.path.join(os.path.dirname(os.path.abspath(__file__)), tiedostonimi) #khatgpt jeesas vähä täs
    
    if os.path.exists(kuva_polku):
        kuva = Image.open(kuva_polku)
        return ImageTk.PhotoImage(kuva)
    else:
        print(f"Tiedostoa ei löydy: {kuva_polku}")
        return None
    
# APINA UI
def apina_ui1():
    canvas.move(apina1, 8, 0)
    apina_pos1 = canvas.coords(apina1)

    if apina_pos1[0] < 1000:
        root.after(100, apina_ui1)

#APINA UI2
def apina_ui2():
    canvas.move(apina2, 8, 0)
    apina_pos2 = canvas.coords(apina2)

    if apina_pos2[0] < 1000:
        root.after(100, apina_ui2)

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
    apina2 = canvas.create_image(200, 770, image=apina_kuva)


#SAAREN NAPPULAT
nappi1 = tk.Button(root, text="Ernesti", command=apina_ui1)
nappi1.place(x=50, y=50)

nappi2 = tk.Button(root, text="Kernesti", command=apina_ui2)
nappi2.place(x=50, y=750)


#KÄYNNISTYS
root.mainloop()