# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def my_list(count: int):
    if count < 0:
        print("Не верное значение, введите положительное число")
        return []

    list_nums = sample(range(1,count * 2), count)
    return(list_nums)


def sum_posicion(list_nums: list):
    sum_numbers = 0
    for i in range(0, len(list_nums), 2):
        sum_numbers += list_nums[i]
    return sum_numbers

full_list = my_list(int(input("Количество элементов: "))) 
print(full_list)
print(sum_posicion(full_list))       
