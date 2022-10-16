# Напишите программу вычисления ариф выражения, заданного строкой. используйте операторы +, +, *, /.
# Приоритет операций стандартный. Добавьте скобк, приоритет операций меняется  

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}


# Ищем скобки, обосабливаем в списки
def parse(exp_1):
    pr_list = []
    i = 0

    while i < len(exp_1):
        if exp_1[i] == "(":
            # Если дальше, с текущего индекса,
            # есть ещё открывающая скобка
            # вызываем рекурсивно parse
            if "(" in exp_1[i + 1:]:
                exp_1 = exp_1[:i + 1] + parse(exp_1[i + 1:])
            n_2 = exp_1.index(")", i)
            pr_list.append(exp_1[i + 1: n_2])
            i = n_2
        else:
            pr_list.append(exp_1[i])
        i += 1
    return pr_list


# Результирующая функция
# TODO доработать
def decision(final_list: list):

    # Проверка на список, раскрытие скобок
    for i, v in enumerate(final_list):
        if isinstance(v, list):
            # Если список, вызываем рекурсивно decision
            final_list[i] = decision(v)

    # Получение индексов приоритетных операций
    ind_list = [i for i, v in enumerate(final_list) if v in "*/"]

    # Работа с приоритетными операциями
    while ind_list:
        k = ind_list[0]
        a, s, b = final_list[k - 1: k + 2]
        final_list.insert(k - 1, actions[s](a, b))
        del final_list[k:k + 3]
        ind_list = [i for i, v in enumerate(final_list) if v in "*/"]

    # Работа с оставшимися операциями
    while len(final_list) > 1:
        a, s, b = final_list[:3]
        del final_list[:3]
        final_list.insert(0, actions[s](a, b))
    
    return final_list[0]


# exp = "4 * 3 - 1 / 9 - 7 * -1".split()
# exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()
# exp = "( 12 + 8 ) * 3 - 11 / 2".split()
# exp = "11 / 2 - ( 12 + 8 ) * 3".split()
# exp = "5 + 11 / 2 - ( 12 + 8 ) * 3 - 12".split()
# exp = "4 * ( 3 - 1 ) / ( 9 - 7 ) * -1".split()
# exp = "8 + 2 * 4 + ( 6 + ( 2 - 3 * 7 + ( 77 - 11 ) ) * 2 )".split()

print(parse(exp))
print(decision(parse(exp)))