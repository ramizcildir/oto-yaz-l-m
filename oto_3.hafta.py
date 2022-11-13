
d = 2
while d < 10:
    print("{} degeri 10 dan küçüktür".format(d))
    d = d+1


kitaplar = ["fizik", "kimya", "matematik" , "edebiyat" , "tarhih"]
istenen_kitap = "din"
if istenen_kitap in kitaplar:
    print("dogru kitap")
else:
    kitaplar.append(istenen_kitap)
    print("istenen kitap kitaplara eklendi ")
    print("güncel liste{}". format(kitaplar))   


sehirler = ["bursa" , "van", "ankara", "rize" ]
for x in sehirler:
    print(x) 


for c in range(2,10):
    print(c)


x =10
while x < 20:
    print("{} degeri 20 den küçüktür " . format(x))
    x = x+1
else:
    print("{} degeri 20 den  küçük degil".format(x))    


#faktoriyreel kavramı
sayi = 6
sonuc = 1
while sayi>0:
    sonuc = sonuc*sayi
    sayi = sayi -1
print(sonuc)    





