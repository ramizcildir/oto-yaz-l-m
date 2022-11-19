
def sayı_karşılaştır(e,r):
    if e>r:
        print("{} rakamı {} rakamından daha büyüktür".format(e,r))

    elif r>e:
        print("{} rakamı {} rakamından daha büyüktür".format(r,e))


    else:
        print("{} rakamı {} rakamına eşittir".format(e,r)) 

sayı_karşılaştır(3,5)                  


"ramiz çıldır".split()


  def isim_ayırma(ad_soyad):
    isim = ad_soyad.split()[0]
    soyisim = ad_soyad.split()[1]
    return isim , soyisim

isim_ayırma("ramiz çıldır")


"-_-".join(["ramiz","çıldır"])


def isim_birleştir(ad, soyad):
    return "_-_".join([ad ,soyad])

isim_birleştir("ramiz","çıldır")    


