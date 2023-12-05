from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resim Albümü")
pencere.geometry("550x600")

baslik = Label(pencere, text="Veri Bilimi Kitapları")
baslik.grid(row=0, column=0, padx= 10, pady=10)
baslik.config(font=("Arial", 30))

kapaklar = ["img/kitap_01.jpg", "img/kitap_02.jpg", "img/kitap_03.jpg", "img/kitap_04.jpg", "img/kitap_05.jpg"]

kapak = 0

def goster():
    gorsel = ImageTk.PhotoImage(Image.open(kapaklar[kapak]))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=1, column=0, padx= 10, pady=10)

goster()

def sonraki():
    global kapak
    if kapak < len(kapaklar)-1:
        kapak +=1
    else:
        kapak = 0
    print(kapak)
    goster()

def geriGit():
    global navigasyon
    navigasyon -=1
    print(navigasyon)

ileriButon = Button(pencere, text='İleri',command=ileriGit)
geriButon = Button(pencere, text='Geri', command=geriGit)


buton = Button(text="Diğer Kitapları", command=sonraki)
buton.grid(row=2, column=0, padx= 10, pady=10)
buton.config(font=("Arial", 20))

pencere.mainloop()