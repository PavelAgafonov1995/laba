print("Ввод строки: ")
s = input()
t = {} #словарь 
k = 0
for i in range(len(s)):
   a = 0
   b  = s[i]
  
   while i+1 < len(s) and s[i] <= s[i+1]:
      a += 1
      i += 1
      b += s[i]
  # print(i)
  # print(b)
   t[a] = t.get(a,b) # получает значение по ключу
   k = max(t.keys()) # возвращает ключи в словаре
print("Наибольшее число вхождений: ")
print(s.count(t[k]))
print(t[a])
