# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

number = input()
sum_digits = 0

power = len(number) - 2
number = float(number)
number *= int(10 ** power)

while number:
    sum_digits += int(number % 10)
    number //= 10

print (int(sum_digits))  