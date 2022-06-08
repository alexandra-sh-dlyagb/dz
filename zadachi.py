#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4
summa = 0
newarray = [1, 2, 3, 4, 5, 6, 7, 8, 46, 132]
len_array = len(newarray)
for i in range (len_array):
    if i%2==0:
        summa = summa + newarray[i]
print (summa)

#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
array_input = [2, 7, 45, 18, 38, 9, 80]
length_array = len(array_input)
if length_array%2==1:
    newarray = [0]*(length_array//2+1)
else:
    newarray =[0]*(length_array/2)
for i in range (len(newarray)):
    newarray[i] = array_input[i] * array_input [length_array - 1 - i]
print (newarray)

#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
array_input = [34.0, 2.6, 7.8, 345.5]
array_result = []
for i in range (len(array_input)):
    array_result.append(array_input[i] - array_input[i]//1)
print (array_result)
value_max = max(array_result)
value_min = min(array_result)
value_result = value_max - value_min
print (value_result)

#Написать программу преобразования десятичного числа в двоичное
value = int(input('Введите десятичное число => '))
newarray = []
while value != 0:
    newarray.append(value%2)
    value = value//2
lengthh = len(newarray)
for i in range (lengthh//2):
    temp = newarray[i]
    newarray[i] = newarray[lengthh - i - 1]
    newarray[lengthh - i - 1] = temp
print (newarray)