import kullanıcı_kayıt 
from datetime import date

def kişisel_menu(kullanıcı_adı):
    while kullanıcı_kayıt.çevrimiçi_kullanıcı:
        kullanıcı_kayıt.os.system("cls")
        print("""
                
                [1] arkadaşlarım
                [2] arkadaş ekle
                [3] direkt mesaj gönder
                [4] mesaj kutusunu aç
                [5] çıkış
        """)

        secim=int(input("seçiminizi yapınız: "))
        if secim == 1:
            arkadaşlarım(kullanıcı_adı)
        elif secim ==2:
            arkadas=input("eklemek istediğiniz arkadaşınızı buraya yazınız: ")
            arkadasEkle(ben=kullanıcı_adı, arkadaş=arkadas)
        elif secim == 3:
            arkadaşın=(input("mesaj göndereceğin arkadaşını seç: "))
            mesaj=input("mesajını yazınız: ")
            mesajGönder(benim=kullanıcı_adı, arkadaşın=arkadaşın, mesaj=mesaj, tarih=date.today())
        
        elif secim == 4:
            mesaj_kutusunu_ac(kullanıcı_adı) # bu kullanıcı adının mesajlarını göstermek için, kullanıncı_adı parametresini girdik
        elif secim == 5:
            kullanıcı_kayıt.çevrimiçi_kullanıcı=False
            input("çıkışınız yapılmak üzere, kayıt menüsüne dönmek için enter tuşuna basınız" )            
        else:
            print("hatalı seçim yaptınız, lütfen tekrardan deneyiniz")

def mesaj_kutusunu_ac(kullanıcı_adı):
    kullanıcı_kayıt.os.system("cls")
    try:
        mesajVar=False
        dosya_r=open("mesaj gönderisi.txt","r")
        satırlar=dosya_r.readlines()
        for mesaj in satırlar:
            bölme=mesaj.split("||")
            gönderen= bölme[0]
            alıcı   = bölme[1]
            mesaj   = bölme[2]
            tarih   = bölme[3]

            if kullanıcı_adı == gönderen or kullanıcı_adı == alıcı:
                print(""" 
                        gönderen: {gönderici}   alıcı: {alıcı} 
                        
                        tarih: {gönderi_tarihi}
                        
                        mesaj {mesaj}  
                """.format(gönderici=gönderen, alıcı=alıcı, mesaj=mesaj, gönderi_tarihi=tarih))
                mesajVar=True
                print("="*90)
        if not mesajVar:
            print("mesajınız henüz daha gönderilmemiştir.")
    except FileNotFoundError:
        print("henüz daha mesajınız yok...")
    input("devam etmek için bir tuşa basınız")

        

def mesajGönder(**kwags):
    kullanıcı_kayıt.os.system("cls")
    dosya_m=open("mesaj gönderisi.txt","a")
    dosya_m.write(kwags["benim"].lower())
    dosya_m.write("||")
    dosya_m.write(kwags["arkadaşın"].lower())
    dosya_m.write("||")
    dosya_m.write(kwags["mesaj"].lower())
    dosya_m.write("||")
    dosya_m.write(str(kwags["tarih"]))
    dosya_m.write("\n")
    dosya_m.close()
    print("{benim} adlı kişi, {arkadaşın} adlı kişiye mesaj gönderdi ".format(benim=kwags["benim"].title(), arkadaşın=kwags["arkadaşın"].title()))
    input("devam etmek için bir tuşa basınız...")



def arkadaşlarım(kullanıcı_adı):
    kullanıcı_kayıt.os.system("cls")
    dosya=open("arkadaşlıklar.txt","r")
    arkadaşıvar= False 
    satırlar=dosya.readlines()
    for arkadaşlıklar in satırlar:
        böl=arkadaşlıklar.split()
        ark1=böl[0]
        ark2=böl[1]
        if kullanıcı_adı == ark1:
            print(ark2)
            arkadaşıvar=True
        elif kullanıcı_adı ==ark2:
            print(ark1)
            arkadaşıvar=True
    if not arkadaşıvar:
        print("arkadaşın şu an yok ama zamanla oladabilir, üzülme...")

def arkadasEkle(**kwargs): # hem sınırsız parametre alır hem de kelime hedefli alır ve parametreleri kelime hedefli gönderilir ve bir sözlüğe çevirir.
    kullanıcı_kayıt.os.system("cls")
    dosya=open("arkadaşlıklar.txt","a")
    dosya.write(kwargs["ben"].lower())
    dosya.write(" ")
    dosya.write(kwargs["arkadaş"].lower())
    dosya.write("\n")
    dosya.close
    print("{ben} isimli kişi, {arkadaş} adlı kullanıcıyı sisteme eklemiştir". format(ben=kwargs["ben"].title(), arkadaş=kwargs["arkadaş"].title()))






if __name__ =="__main__":
    while True:
        kullanıcı_kayıt.os.system("cls")
        print("""
            
            [1] kayıt ol
            [2] giriş yap
        
             """)


        secim=int(input("seçiminizi yapınız: "))
        if secim == 1:
            kullanıcı_kayıt.kayıt_ol()
        elif secim == 2:
            kullanıcı_kayıt.giriş_yap()

            if kullanıcı_kayıt.çevrimiçi_kullanıcı:
                kişisel_menu(kullanıcı_kayıt.çevrimiçi_kullanıcı)



