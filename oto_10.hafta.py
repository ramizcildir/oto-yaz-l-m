# %%
sayı = int(input("sayı giriniz"))
if sayı%2==0:
    print("{} değeri çift sayı".format(sayı))
else:
    print("{} değeri tek sayı".format(sayı))

    

# %%
def sayımı_degilmi():
    deger = input("deger giriniz :")
    if deger.isdigit():     # deger bir sayıya eşitken anlamı taşıyor
        print("{} degeri bir sayıya eşit".format(deger))

    else:
        print("{} degeri bir sayı degil".format(deger))


sayımı_degilmi()            

# %%
def tam_sayıya_yuvarla():
    ifade = input("bir sayı giriniz :")
    try:   # bunu bir dene

        print("{} ifadesi {} değerine yuvarlandı".format(ifade,round(float(ifade))))

    except:   #yukardakinen bir sonuç alamazsan  yukardakinden "HARİÇ(except) olarak" bunuda bir dene
        print("{} ifadesi bir sayıya yuvarlanamıyor".format(ifade))

tam_sayıya_yuvarla()        

# %%
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

# %%
try:
    5 +"a"
except TypeError:
    print("tip eroru var")

# %%



