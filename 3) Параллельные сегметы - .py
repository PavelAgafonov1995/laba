print("Ввод координат X1, Y1, X2, Y2, X3, Y3, X4, Y4: ") 
coordinats = input().split(",") 
for i in range(len(coordinats)): 
   coordinats[i] = int(coordinats[i]) 
if len(coordinats) > 8:
   print('Значений больше 8!')
elif len(coordinats) < 8:
   print('Значений меньше 8!')
else:
   a1a2 = (coordinats[3]-coordinats[1])/(coordinats[2]-coordinats[0])
   a3a4 = (coordinats[7]-coordinats[5])/(coordinats[6]-coordinats[4])
   if a1a2 == a3a4:
      print('YES')
   else:
      print('NO')
