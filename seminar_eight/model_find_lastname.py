
def find_by_last_name(dict):
    str_1 = input('Введите фамилию: ')
    for key, value in dict.items():
            for i in value:
                if i == str_1:
                    print(' '.join(value))
                
    
   

