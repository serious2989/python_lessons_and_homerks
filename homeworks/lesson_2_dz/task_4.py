# * 4. Напишите программу, которая принимает на вход 2 числа.
#      Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#      Найдите произведение элементов на указанных позициях(не индексах).

numbers = int(input("Введите значение N: "))
a = int(input("Первая позиция: "))
b = int(input("Вторая позиция: "))

num_list = list(range(-numbers, numbers + 1))

print(num_list)
len_list = len(num_list)

if len_list >= a > 0 and len_list >= b > 0:
    print(num_list[a - 1] * num_list[b - 1])
else:
    print("Нет значений для этих индексов")
