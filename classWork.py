#1 шаг считать данные и определить лучшего
#2 считать данные и распечатать список по убыванию суммарного балла
#3 удалить тех у кого балл меньше 50
#4 если сумма баллов одинаковая, то смотреть по первому, после 5 первых черта
#5 вывсти приказ о зачислении абитуриентов
import random


f = open('dataa.txt', 'r')
#for i in range(12):
#    f.write(str(i) + '\t' + 'Name' + str(i) + '\t' + 'Surname' + str(i) + '\t' + str(random.randrange(100)) +
#            '\t' + str(random.randrange(100)) + '\t' + str(random.randrange(100)) + ' ' + '\n')
best = (0, 0)
a = []
for i in range(12):
    strr = f.readline()
    strr = strr.split()
    summary = int(strr[3]) + int(strr[4]) + int(strr[5])
    a.append([strr[0], summary])
    if summary > best[1]:
        best = (int(strr[0]), summary)
print('Первый пункт', best)

#a = []
#for i in range(12):
#    for j in range(12-i-1):
#        if a[j][1] > a[j+1][1]:
#            a[j], a[j+1] = a[j+1], a[j]



#listt = []
#for i in range(12):
#    strr = f.readline()
#    strr = strr.split()
#    listt.append(strr)








f.close()