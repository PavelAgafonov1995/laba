print('Введите строку') 
string=input()
text = '';
while string != '': # пока введеная строка не пустая
    text = string; # запоминаем строку
    string = input()# ищем пустую строку
words = text.split() # разбиваем на слова
words_frequency = {} 
max_frequency = 0;
for word in words:
    if word in words_frequency:
        words_frequency[word] += 1
    else:
        words_frequency[word] = 1
    if words_frequency[word] > max_frequency:
        max_frequency = words_frequency[word]
most_frequent_word = ''

for word in iter(words_frequency):
    if words_frequency[word] == max_frequency:
        if most_frequent_word == '':
            most_frequent_word = word
        else:
            most_frequent_word = '---'
            break;
print (most_frequent_word);
