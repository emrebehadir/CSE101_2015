#-*-coding: utf-8-*-

import sys      #sys kütüphanesini importet					
import fnmatch  #fnmatch kütüphanesini importet

def yap(abc):	#Yap fonksiyonunu oluştur				
		
	if  fnmatch.fnmatch(abc, '*.exe'): 	 # Girilen dosya uzantısını .exe ile karşılatır doğruysa devam et
		dosya = open(abc,"r")      	 # abcye tanımlı veriyi aç ve dosya değişkenine ata
		karakter = dosya.read(1)         # dosya değişkenindeki ilk karakteri oku
		while karakter != "":            #Boş kararakteri bulana kadar devam et

			a = ord(karakter)        #Karakter değişkeninin decimal değerini a ye ata
			b = hex(ord(karakter))   #Karakteri değişkeninin hexadecimal değerini b ye ata
			c = bin(ord(karakter))   #Karakteri değişkeninin binary değerini c ye ata
			print karakter,">>","Decimal değer =",a,"Hexadecimal değer =" , b ,"Binary değer =", c
			karakter = dosya.read(1) #Bir sonraki karaktere geç
	
	else:
		print "!! Hata : Bu bir exe dosyası değildir."


yap(sys.argv[1])    #argüment 1 i yap fonksiyonunda kullan
