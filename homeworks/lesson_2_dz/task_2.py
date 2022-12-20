# 2. Напишите программу, которая принимает на вход число N
#    и выдает набор произведений чисел от 1 до N в виде списка.

num = int(input())
my_sum = 1
num_list = []

for i in range(num):
    my_sum *= i + 1
    num_list.append(my_sum)

print(num_list)    