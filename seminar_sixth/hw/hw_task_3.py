# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def Dict_names(list_names: list):
        d = {}
        for x in list_names:
                first_letter = x[0]
                if first_letter not in d:
                         d[first_letter] = [x]
                else:
                        d[first_letter] += [x]
        return(d)

list_names = input("enter names divided by space: ").split()
print(list_names)
print(Dict_names(list_names))