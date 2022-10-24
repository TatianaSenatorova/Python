def find_by_position(dict):
    str_1 = input('Должность: ')
    for key, value in dict.items():
            for i in value:
                if i == str_1:
                    print(' '.join(value))
                
    