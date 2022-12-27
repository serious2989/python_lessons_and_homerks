# 2. Напишите программу, которая найдёт произведение пар чисел списка.
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def my_list(count: int):
    if count < 0:
        print("Не верное значение, введите положительное число")
        return []

    list_nums = sample(range(1,count * 2), count)
    return(list_nums)

def pairs_nums(list_nums: list):
    resuls_list = []
    len_list = len(list_nums)

    for i in range(len_list // 2):
        resuls_list.append(list_nums[i] * list_nums[len_list - i - 1])

    if len_list % 2:
        resuls_list.append(list_nums[len_list // 2])
    return resuls_list

full_list = my_list(int(input("Введи количество элементов: ")))
print(full_list)
print(pairs_nums(full_list))