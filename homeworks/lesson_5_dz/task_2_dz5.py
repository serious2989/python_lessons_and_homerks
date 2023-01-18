# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.


from itertools import groupby, starmap
from os import path


def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text):
        with open(text) as file_1, \
                open(code_text, "a") as file_2:
            for i in file_1:
                file_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("Файлов в системе нет!")


def rle_decode(name):
    if path.exists(name):
        with open(name) as new_file:
            n = ""
            for k in new_file:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("Файлов в системе нет!")

rle_encode(input("Введите имя файла с текстом: "), input("Введите имя файла для записи: "))
rle_decode(input("Введите имя файла для декодирования: "))
