#Kullanıcı Kayıt/Giriş Uygulaması
import os,time

çevrimiçi_kullanıcı = False

def giriş_yap():
	global çevrimiçi_kullanıcı
	kullanıcı_adı= input("Kullanıcı adınızı girin: ")
	şifre= input("Şifrenizi girin: ")

	dosya= open("kullanıcı.txt","r")
	satırlar = dosya.readlines()
	çevrimiçi_kullanıcı = False
	for kullanıcı in satırlar:
		bölünmüş = kullanıcı.split()
		bölünmüş_k_adı= bölünmüş[0]
		bölünmüş_şifre= bölünmüş[1]
		if kullanıcı_adı == bölünmüş_k_adı and şifre == bölünmüş_şifre:
			çevrimiçi_kullanıcı= kullanıcı_adı
	if çevrimiçi_kullanıcı:
		print("Hoşgeldin: ",kullanıcı_adı)
	else:
		print("Kullanıcı adı veya şifre hatalı!")
	input("Devam etmek için bir tuşa basın")


def kayıt_ol():
	kullanıcı_adı= input("Kullanıcı adı girin: ")
	mail= input("Mail adresinizi girin: ")
	if not kontrol(kullanıcı_adı):
		#Kullanıcı adı müsait değilse
		print("Kullanıcı Adı Zaten Mevcut")
		time.sleep(1)
		os.system(temizle)
		return kayıt_ol()
	şifre= input("Şifrenizi giriniz: ")
	şifre_o= input("Şifrenizi tekrar giriniz: ")

	if şifre != şifre_o:
		print("Şifreniz uyumsuz")
		time.sleep(1)
		os.system(temizle)
		return kayıt_ol()

	dosya = open("kullanıcı.txt","a")
	dosya.write(kullanıcı_adı)
	dosya.write(" ")
	dosya.write(şifre)
	dosya.write(" ")
	dosya.write(mail)
	dosya.write("\n")
	dosya.close()
	print("Kullanıcı başarılı bir şekilde kaydedildi.")
	input("Devam etmek için bir tuşa basın")


def kontrol(kullanıcı_adı):
	try:
		if kullanıcı_adı not in open("kullanıcı.txt","r").read():
			return True
		else:
			return False
	except FileNotFoundError:
		return True


temizle = ("cls" if os.name == "nt" else "clear")


if __name__ == "__main__": # if __name__ metodu ekrana ilk buradan başlamamızı sağlar
	while True: 
		os.system(temizle)
		print("""

					[1] Kayıt Ol
					[2] Giriş Yap

			""")

		seçim= int(input("Seçiminizi yapınız: "))
		if seçim == 1:
			os.system(temizle)
			kayıt_ol()
		elif seçim == 2:
			os.system(temizle)
			giriş_yap()