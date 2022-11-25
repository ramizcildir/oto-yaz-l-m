
# map olmadan

list =[1,3,5,8,6] 

def karesini_al(x):
    print(x*x)

list2=[]
for i in list  :
    list2.append(karesini_al(i)) 

print(list2)     


list3= set(map(karesini_al,list))
print(list3)


#map

list= range(2,8)

def iki_katını_al(x):
    print(x*2)
    
list2 =set(map(iki_katını_al , list))    
print(list2)


#else None

def çift_sayi(x):
    return x if x%2 ==0 else None

listr= [2,5,8,11,14]
set(map(çift_sayi,listr))




#lambda

listf= [7,5,6,4,3]

set(map(lambda x : x*2, listf))


listc=[1,2,3,4,5,6,7,8,9]
set(map(lambda x :x if x%2==0 else None , listc))


input("isim girin:")


sayı  =  int(input("sayı gir:"))
if sayı %2 == 0:
    print("{} sayısı çift sayıdır".format(sayı))
if sayı %2==1:
    print("{} sayısı tek sayıdır".format(sayı))
  
    


def sayımı_degilmi():
    deger = input("deger giriniz :")
    if deger.isdigit():     # deger bir sayıya eşitken anlamı taşıyor
        print("{} degeri bir sayıya eşit".format(deger))

    else:
        print("{} degeri bir sayı degil".format(deger))


sayımı_degilmi()            


def sayıyı_bulma():
    ifade = input("ifaeyi yazınız :")
    while not ifade.isdigit():     #ifade bir sayıya eşit değilken anlamı taşıyor
        print("{} ifadesi bir sayıya eşit degil,tekrar deneyiniz.".format(ifade))
        ifade = input("ifadeyi yazınız :")

    else:
        print("{} ifadesi bir sayıya eşit".format(ifade)) 



sayıyı_bulma()           


  
   
    



# e-posta dogrulama
def e_posta_sorgulama():
    girdi = input("lütfen geçerli bir e-posta giriniz :")
     
    while not (("."in girdi) and ("@" in girdi)):
        print("üzgünüm , tekrar deneyiniz")
        girdi = input("lütfen geçerli bir e-posta giriniz :")

    else:
        print("tebrikler geçerli bir e-posta adresi")

e_posta_sorgulama()             


round(8.8)


def tam_sayıya_yuvarla():
    ifade = input("bir sayı giriniz :")
    print("{} ifadesi {} değerine yuvarlandı".format(ifade,round(float(ifade))))


tam_sayıya_yuvarla()    


def tam_sayıya_yuvarla():
    ifade = input("bir sayı giriniz :")
    try:   # bunu bir dene

        print("{} ifadesi {} değerine yuvarlandı".format(ifade,round(float(ifade))))

    except:   #yukardakinen bir sonuç alamazsan  yukardakinden "HARİÇ(except) olarak" bunuda bir dene
        print("{} ifadesi bir sayıya yuvarlanamıyor".format(ifade))

tam_sayıya_yuvarla()        


def tam_sayıya_cevir():
    deger = input("bir deger giriniz :")
    try:
        print("{} degeri {} degerine çevrildi.".format(deger,round(float(deger))))
        sonuç = "başarılı"
    except:
        print("{} degeri bir sayıya çevrilemedi.".format(deger))
        sonuç = "başarısız"
    finally:
        print("işlem {} bir şekilde gerçekleşti.".format(sonuç))

tam_sayıya_cevir()            

            


def tam_sayı_iste():
    while True:
        deger = input("bir deger giriniz")

        try:
            print("{} degeri {} degerine çevrildi.".format(deger,round(float(deger))))
            break
        
        except:
            print(" {} degeri bir sayıya çevrilemedi".format(deger))
            pass

tam_sayı_iste()        


try:
    5 +"a"
except TypeError:
    print("tip eroru var")
   




#class

class Ucus():
    havayolu= "pegasus"
    yer = "BURSA"

ucus1 = Ucus()

ucus1.havayolu
ucus1.yer




class yemek():
    yer ="mutfak"
    def __init__(self, corba,salata,tatlı, icecek):
        self.corba=corba
        self.salata=salata
        self.tatlı=tatlı
        self.icecek=icecek


öğün1 = yemek("yayla","çoban","baklava","su")
öğün2 = yemek("tavuk","mevsim","sütlaç","ayran")

öğün2.tatlı


    


class yemek():
    yer ="mutfak"
    def __init__(self, corba,salata,tatlı, icecek):
        self.corba=corba
        self.salata=salata
        self.tatlı=tatlı
        self.icecek=icecek


    def yemek_zamanı(self):
        return "yemekte : {} çorbası , {} salatası , {} tatlısı, {} iceceği vardır".format(self.corba,self.salata,self.tatlı,
        self.icecek)

öğün1= yemek("tavuk","çoban","baklava","su")
öğün2 =yemek("yayla","mevsim","sütlaç","ayran")


öğün1.yemek_zamanı()   # öğün 1' in kendisini(self) istedik.


