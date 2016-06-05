print("Ввод списка: ") 
spisok = input().split(',') 
for i in range(len(spisok)): 
   spisok[i] = int(spisok[i])
sp=max(spisok)
del spisok[sp]
second_max=max(spisok)

#for j in range(len(spisok)):
   #spisok[j] < max(spisok) and spisok[j] > :
     # second_max = spisok[j]
#if second_max != max(spisok):
print("Второй максимум списка: ")
print(second_max)
#else: 
   #print("Второго максимума нет.")
   
