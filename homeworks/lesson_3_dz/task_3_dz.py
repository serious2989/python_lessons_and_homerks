# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Без использования встроенной функции преобразования, без строк.

def convert_num(a: int):
    my_list = []

    while a > 0:
        my_list.insert(0, a % 2)
        a //= 2

    print(*my_list, sep="")

convert_num(int(input()))