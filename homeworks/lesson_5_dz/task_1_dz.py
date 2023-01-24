# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
#  in  ()
#  Number of words: 10
#  out
#  авб абв бав абв вба бав вба абв абв абв
#  авб бав вба бав вба

#  in
#  Number of words: 6

#  out
#  ваб вба абв ваб бва абв
#  ваб вба ваб бва

from random import sample

def list_rand(count: int,alp: str = "абв"):
    words_list = []
    for i in range(count):
        text = sample(alp, 3)
        words_list.append("".join(text))
    return " ".join(words_list)

def new_string(words: str):
    return " ".join(i for i in words.split()if i != "абв")

full_list = list_rand(int(input("How many words: ")))
print(full_list)
print(new_string(full_list))
