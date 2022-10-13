#1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
#В тексте используется разделитель пробел.
#in Number of words: 10
#out
#авб абв бав абв вба бав вба абв абв абв
#авб бав вба бав вба

from os import remove
import random  

def fill_str(N: int):
    list_words = []
    for i in range(N):
        word = random.sample("абв", 3)
        list_words.append("". join(word))
    return list_words

def exept_some_words(list_words: list):
     list_words.remove("абв")
     str_1 = " ".join(list_words)
     return str_1 
      
    
list_words_1 = fill_str(int(input("Enter a number of words: ")))
print(list_words_1)
print(f"list without 'абв' combination: {exept_some_words(list_words_1)}")



