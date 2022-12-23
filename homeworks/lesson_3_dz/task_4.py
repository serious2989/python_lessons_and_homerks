# ** 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#       Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform

def list_randome(count: int):
    list_nums = []
    if count <= 0:
        print("Вы ввели не верное значение")
        return(0.0)

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2))
    return list_nums

def sum_nums(list_nums: list):
    min = max = list_nums[0] % 1

    for k in range(1,len(list_nums)):
        num = round(list_nums[k] % 1, 2)
        if num > max:
            max = num
        elif num < min:
            min = num
    result = round(max - min, 2)
    print(f"Минимальное: {min:.2f}, Максимальное:{max:.2f}. Результат: {result}")
    return result

full_list = list_randome(int(input("Введите количество элементов: ")))
print(full_list)
print(sum_nums(full_list))            
