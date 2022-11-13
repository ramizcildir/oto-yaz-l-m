
a = 3
if a> 2:
    print ("büyüktür")




# # LOOPS - DÖNGÜLER


# while
a = 3
while a< 10:
    print(a)
    a= a+1
print("sona gelindi")


k = 0
while k< 5:
    print(k+ 1)
    k = k+1
    



k =0
while k< 5:
    print(k * "#")
    k=k+1
    


h =5
while h> 0:
    print(h)
    h=h-1



    


# faktoriyel 
sayi =5
sonuc =1
while sayi > 0:
    sonuc = sonuc*sayi
    sayi = sayi -1
print(sonuc)    



x = 0
#sonsuz döngü
#çalıştırma!!!!!!!!!!!
while True :
    print(x)


#sonsuz dögüyü dudurmak için
x = 0
while True:
    print(x)
    x =x+1
    if x>= 5:
        break


# iç içe döngüler
x , y = 5, 5
while x>0:
    while y>0:
        y =y-1
        x = x-1
        print("x:" , x , "y:", y )
        



x = 0
while x<5:
    x =x+1
    print(x)
    while y<5:
        y = y+1
        print(y)

    

c= ["2" ,"3",  "8" ,"5"]
for i in c:
    print(i)
  


for i in range(2,10):
    print (i)
while i >=5:
    print(i)
    i = i-1    


x= 0
while x<10:
    x=x+1

    print(x)
    





