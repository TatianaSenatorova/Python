# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from os import path
from itertools import groupby
from itertools import starmap

def encod_text(t = "text_words.txt", t_d = "text_code_words.txt"):
    if path.exists(t):
        with open("text_words.txt", "r", encoding = 'utf-8') as f1,\
            open ('text_code_words.txt', "w", encoding="utf-8") as f2:
                for line in f1:
                    f2.writelines("".join([f"{len(list(num))}{sym}" for sym, num in groupby(line)]))

    else: print("file doesn't exist")

def decod_text(t_d = "text_code_words.txt"):
    with open("text_code_words.txt", "r", encoding = 'utf-8') as f3:
        str_num = ''
        rows = []
        for line in f3:
            for i in line.strip():
                if i.isdigit():
                    str_num = str_num + i
                else:
                    rows.append([str_num, i])
                    str_num = ''
                
    str_1 = " ".join(map(str, rows))
    removed_chars = [',', '[', ']', ' ', '\'', ]
    chars = set(removed_chars)
    res =  ''.join(filter(lambda x: x not in chars, str_1))
    print(res)      
        


encod_text(input("enter file with rows: "), input("enter file to write encode text "))
decod_text(input('enter file to decode '))
