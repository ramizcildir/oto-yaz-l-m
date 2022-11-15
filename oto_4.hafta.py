
harfler = ["a","b","c","d"]
for i in harfler:
    print(i)


harfler2 = ["a","b","c","d"]
for i in enumerate (harfler2):
    print(i)


harfler3 =["a","b","c","d"]
for index ,i in  enumerate(harfler3):
    print(i, index )


harfler4 =["a","b","c","d"]
for index,i in enumerate(harfler4):
    print("{}. harf:{}".format(index,i))

# %%
markalar= ["BMW","KIA","MERCEDES","WV"]
sıralamalar = [1,2,3,4]
for i in zip(sıralamalar,markalar):
    print(i)

# %%
yemekler=["çorba","pilav","makarna","tatlı","köfte"]
for index,i in enumerate(yemekler):
    print(index+1,i)
    if i == "tatlı":
        print("{} yemeği {}.sırada".format(i,index+1))
        break

# %%
for r in range(1,8):
    if r %2 == 0:   # çift sayı bulma mantığı
        continue
    print(r)      
    


