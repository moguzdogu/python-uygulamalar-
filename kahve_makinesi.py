print(""" 
       [1]çay [2] kahve [3] sıcak çikolata  [4] espresso """)

secim=int(input("seciminizi yapınız: "))
seker=input("şeker kullanıyor musunuz?: ")

if seker :
 if secim == 1:
    print("çayınız hazırlanıyor")
    if seker == "evet":
       print("çayınız şekerli hazırlanıyor")
    elif seker == "hayır":
        print("çayınız şekersiz hazırlanıyor")
 elif secim == 2:
    print("kahveniz hazırlanıyor")
    if seker == "evet":
        print("kahveniz şekerli olarak hazırlanıyor")
    elif seker == "hayır":
        print("kahveniz şekersiz olarak hazırlanıyor")
 elif secim == 3:
    print("sıcak çikolatanız hazırlanıyor")
    if seker == "evet":
        print("sıcak çikolatanız şekersiz olarak hazırlanıyor")
    elif seker == "hayır":
            print("sıcak çikolatanız şekersiz olarak hazırlanıyor")
 elif secim == 4:
    print("espressonuz hazırlanıyor")
    if seker == "evet":
        print("espressonuz şekerli olarak hazırlanıyor")
    elif seker == "hayır":
            print("espressonuz şekersiz olarak hazırlanıyor")
 else:
    print("makine bozuk...")
else:
    print("şeker seçeneğini lütfen seçiniz ")
        
