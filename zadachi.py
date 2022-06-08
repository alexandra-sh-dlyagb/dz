#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4
summa = 0
newarray = [1, 2, 3, 4, 5, 6, 7, 8, 46, 132]
len_array = len(newarray)
for i in range (len_array):
    if i%2==0:
        summa = summa + newarray[i]
print (summa)
