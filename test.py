# 5. Напишите программу, которая принимает на вход число и проверяет,
#    кратно ли оно 5 и 10 или 15, но не 30.

num = int(input("Input your number: "))
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
     print("Yes")
else:
     print("No")
