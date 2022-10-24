from ast import Num
from xml.parsers.expat import model
import user_interface
import model_print
import model_dict
import model_find_lastname
import model_find_position


def button_click():
    user_interface.print_info()
    choose = int(input('выберите действие: '))
    print(choose)
    dict_1 = model_dict.make_list()
    if choose == 1:
        result = model_print.print_table()
        print(result)
    elif choose == 2:    
        result = model_find_lastname.find_by_last_name(dict_1)
        print(result)
    elif choose == 3:    
        result = model_find_position.find_by_position(dict_1)
        print(result)  
        
    
    
        