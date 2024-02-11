#!/usr/bin/env python
# coding: utf-8

# ### Ödev 1
# 
# liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
# 
# 1. Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.
# 
#    - "3" değerine ulaşmak için indexleme yapın.
#    - "Hi-Kod" değerine ulaşmak için indexleme yapın.
#    - 4.7 değerine ulaşmak için indexleme yapın.
#    - 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.
#    - 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.

# In[2]:


# "3" değerine ulaşmak için indexleme yapın.

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
deger1 = liste[3]
print(deger1)

# "Hi-Kod" değerine ulaşmak için indexleme yapın.
deger2 = liste[5]
print(deger2)

# 4.7 değerine ulaşmak için indexleme yapın.
deger3 = liste[-1]
print(deger3)

# 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.
slicing1 = liste[2:6]
print(slicing1)

# 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.
slicing2 = liste[4:]
print(slicing2)


# ### Ödev 2
# 
# Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.
# 
# liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

# In[1]:


liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
yeni_liste = []

for eleman in liste:
    if isinstance(eleman, str):
        yeni_liste.append(eleman)

print(yeni_liste)


# ### Ödev 3
# 
# Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.

# In[ ]:


for index in range(len(meyveler)):

    print("{}. indexte bulunan meyve: {}".format(index,meyveler[index]))


# 
