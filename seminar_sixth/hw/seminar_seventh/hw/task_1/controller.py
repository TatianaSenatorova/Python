import user_interface as user
import model_sum as model
import model_div 
import model_mult
import model_sub

def button_click():
    print('1 = complex; 2 = float')
    value_item = int(input('выберите значение: '))
    print()
    if value_item == 1:
        value_a = user.input_complex()
        value_b = user.input_complex()
    if value_item == 2:
        value_a = user.input_data()
        value_b = user.input_data()
   
    print('1 = div; 2 = mult; 3 = sum; 4 = sub')
    print('выберите функцию: ')
    value_model = int(input('выберите значение: '))
    print()
   
    if value_model == 3: 
        model.init(value_a, value_b)
        result = model.do_it()
        user.view_data(result)
   
    
    if value_model == 1:
        model_div.init(value_a, value_b)
        result = model_div.do_it() 
        user.view_data(result)
   
    
    if value_model == 2:
        model_mult.init(value_a, value_b)
        result = model_mult.do_it() 
        user.view_data(result)
    if value_model == 4:
        model_sub.init(value_a, value_b)
        result = model_sub.do_it() 
        user.view_data(result)