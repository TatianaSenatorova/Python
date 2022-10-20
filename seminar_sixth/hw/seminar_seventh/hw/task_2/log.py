from user_interface import get_info as gi

info = gi()
def button_click():
    file = 'phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.writelines(f'Фамилия;Имя;Номер телефона;Описание\n')
        data.writelines(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')
    
    file = 'phonebook.xml'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.writelines(f'Фамилия;Имя;Номер телефона;Описание\n')
        data.writelines(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')
    
    file = 'phonebook.txt'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')
    