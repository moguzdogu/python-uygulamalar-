# Hesap makinesi

print( """
           [1] toplama [2] çıkarma  [3] bölme  [4] çarpma [5] üs alma 
           """)
          
secenek= int(input("seciminizi yapın: "))
sayılar=input("sayı girerken boşluk bırakmayı ihmal etmeyiniz: ")
liste_boşluk=sayılar.split(" ")

if secenek == 1:
    birinci_sayı=float(liste_boşluk[0])
    ikinci_sayı=float(liste_boşluk[1])
    print ("{} + {} = {}".format(birinci_sayı,ikinci_sayı, birinci_sayı + ikinci_sayı))

elif secenek ==2:
    birinci_sayı=float(liste_boşluk[0])
    ikinci_sayı=float(liste_boşluk[1])
    print("{} - {} = {}".format(birinci_sayı, ikinci_sayı, birinci_sayı - ikinci_sayı))

elif secenek ==3:
    birinci_sayı=float(liste_boşluk[0])
    ikinci_sayı=float(liste_boşluk[1])
    print("{} / {} = {}".format(birinci_sayı, ikinci_sayı, birinci_sayı / ikinci_sayı))

elif secenek ==4:
    birinci_sayı=float(liste_boşluk[0])
    ikinci_sayı=float(liste_boşluk[1])
    print("{} * {} = {}".format(birinci_sayı, ikinci_sayı, birinci_sayı * ikinci_sayı))

elif secenek ==5:
    birinci_sayı=float(liste_boşluk[0])
    ikinci_sayı=float(liste_boşluk[1])
    print("{} ** {} = {}".format(birinci_sayı, ikinci_sayı, birinci_sayı ** ikinci_sayı))
else:
    print("hatalı girşi yaptınız...")
    