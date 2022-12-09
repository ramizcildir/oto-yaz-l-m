# %%
import datetime

# %%
from datetime import date
from datetime import time

# %%
import time

# %% [markdown]
# 

# %%
zaman= time.time()
print(zaman)

# %%
baslangıc= time.time()    # baslangıç zamanı
liste = []
for i in range(10000):  
    liste.append(i)      # 10000 ' e kadar say
bitis = time.time()      # 10000 ' e kadar saydıktan sonra bitis süresi
print(bitis - baslangıc )    # aradaki geçen süre



# %%
ileriki_zaman = time.ctime(100)    # şuanki zamandan 100 saniye sonrası
print(ileriki_zaman)

# %%
ileriki_zaman2= time.localtime(100000)  # şuanki zamandan  100000 saniye sonrası
ileriki_zaman2    

# %%
print ("program başlatıldı")      # bunu yazdır
time.sleep(5)                  #  5 saniye bekle
print("program sonlandı")       # sonra bunu yazdır

# %%
import numpy as np

# %%
import random

# %%
data = np.random.randn(2,2)       #data = veri
data

# %%
import numpy as np

a = [random.randrange(0,1000) for x in range(10000)]
x = np.array(a)

baslangic_zamani = time.time()

b = x.sort()


print(f"np: Toplam gecen süre: {time.time()-baslangic_zamani}") 



