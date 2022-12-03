
# dosya ve klasör açma modülleri


%ls    # şuanki dosyanın içindeki diğer dosyalar


%pwd    # şuanki dosyanın konumu


import os

os.getcwd()     # şuanki dosyanın konumu


os.listdir()     # şuanki dosyanın içindeki dosyalar


os.mkdir("c:\\Users\\ASUS\\.ipython\\selammm")     # şuanki dosyanın içine dosya ekleme




os.listdir()


os.rmdir("c:\\Users\\ASUS\\.ipython\\selammm")   # şuanki dosyanın konumundan dosya silme


os.listdir()


#regex  re    ( normal ifade)


import re


sehirler= "bursa sakarya ankara bolu rize  sakarya "
istenen_sehir="sakarya"
re.search(istenen_sehir,sehirler)      


ifade =re.search(istenen_sehir,sehirler)
ifade.span()     #ifadenin açıklığı


ifade.start()  #ifadenin başladığı karakter  numarası


 ifade.end()      #ifadenin bttiği karakter numarası


for i in re.findall(istenen_sehir,sehirler):      # ifadedeki bütün sonuçları okut
    print(i)


for r in re.finditer(istenen_sehir,sehirler):
    print(r.span())     # ifadenin tüm spanlarını bulmak için "finditer" kullandık"

# %%
# \d  = rakam
# \w  = karakter
# \s  = boşluk

# \D  = rakam değil
# \W  = karakter değil
# \S  = boşluk değil


plaka_kodu= " bursanın plakası kodo : 16"
istenen_deger= "\d\d"
re.search(istenen_deger,plaka_kodu)


# {x}  =  x tane
# {x,y} =     x VEYA y tane
# {x,}   =  EN AZ x tane
# *  =   0 ya da fazla
# +   =  1 ya da fazla
# ?  =   ya 1 ya hiç



cumle = "bursa 16 istanbul 34 ankara 06"
istenen_ifade= r"\s\w{4,}"
for i in re.finditer(istenen_ifade,cumle):
    print(i.group(),i.span())


import re


def oparatör():
    numara=input("numara giriniz:")
    istenen__numara=r"(\d{3,4})-(\d{3})-(\d{4})"
    eslesme= re.search(istenen__numara,numara)
    if eslesme:         #eğer eslesme olayı gerçekleşirse

        print ("{} geçerli bir numara.".format(numara))   #bunu okut


    else:     # eğer eslesme olayı gerçekleşmesse 
        print("{} geçersiz  bir numara".format(numara))      # bunu okut

oparatör()


import re




def oparatör_bul():
    numara = input("numara giriniz:")
    istenen_numara = "(\d{3})-(\d{3})-(\d{4})"
    eslesme3=re.search(istenen_numara,numara)
    if eslesme3:
        baslangıc = eslesme3()[0]
        if baslangıc.startswith("530"): 
            return"a oparatörü"
        if baslangıc.startswith("540"):
            return"b oparatörü" 
        else:
            return "c oparatörü"       
        

    else:
        return"geçersiz numara"    
        
oparatör_bul()


# RANDOM


import random


random.random()


random.uniform(5,10)


random.randint(5,10)


random.choice(range(1,10))    # choice = seçim


random.sample(range(1,10),k=2)    # sample = örneklem


liste = [0,1,2,3,4,5]
print(liste) 
random.shuffle(liste)
print(liste)


#math
import math


math.sin(90)


math.ceil(8.5)    #tavan


math.floor(8.9)      #zemin


math.pow(3,2)    #pow = kuvvet


#Counter (tezgah)
from collections import Counter
import random


list1 =random.sample(range(1,10),k=4)
list2=random.sample(range(1,10),k=4)
list3=random.sample(range(1,10),k=4)
list4=random.sample(range(1,10),k=4)

listeler_toplam= list1+list2+list3+list4
listelerin_listesi=[list1,list2,list3,list4]

print (listeler_toplam)

print(listelerin_listesi)


for index,i in enumerate(listelerin_listesi):
    print("{}. liste: {}".format(index+1,i))
Counter(listeler_toplam)


Counter("fdbhfdjbhsvdbhvsdbjhdsbvhdbh")


enstrümanlar="gitar davul darbuka darbuka darbuka gitar davul davul davul davul klarnet"
Counter(enstrümanlar)


  a =enstrümanlar.split()
  print(a)

Counter(a).most_common()     # most common = en yaygın





