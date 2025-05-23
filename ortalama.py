ogrenciOrtalamasi = float(input("Ortalamanızı girniz: "))
zayifSayisi = int(input("Zayıf sayınızı giriniz : "))

if zayifSayisi==0:
    if ogrenciOrtalamasi>=85 and ogrenciOrtalamasi<=100:
        print("Takdir belgesi almaya hak kazandınız.")
    elif ogrenciOrtalamasi>=70:
        print("Teşekkür belgesi almaya hak kazandınız.")
    elif ogrenciOrtalamasi>=50:
        print("Sorunsuz olarak sınıfı geçtiniz.")
    else:
        print("Ortalama yükseltme sınavlarına giriniz.")
else:
    if ogrenciOrtalamasi>=50:
        print("sorumlu olarak sınıfı geçtiniz")
    elif ogrenciOrtalamasi>25:
        print("Sorumluluk sınavlarına giriniz")
    else:
        print("Sınıf tekrarı")
