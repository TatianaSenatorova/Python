import logging
from math import sqrt



from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

operation_keybord_main = 'Addition|Subtraction|Multiply|Division|Exponentiation|Sqrt|Menu'

MENU, CHOICE_NUMBER, CHOICE_OPERATION, ADDITION_NUMS, SUBSTRACTION_NUMS, MULTIPLY, DIVISION, EXPONENTIATION_NUMS, SQRT_NUM = range(9)


def start(update, _):
    reply_keyboard = [['Start']]
    mark_key = ReplyKeyboardMarkup(reply_keyboard, True)
    update.message.reply_text('Calculator welcomes you! Press start to continue',
        reply_markup=mark_key)
    return MENU

def menu(update, _):
    user = Update.message.from_user
    logger.info('User %s begins to work with calculator', user.first_name)
    reply_keyboard = [['Rational', 'Complex', 'Exit']]
    mark_key = ReplyKeyboardMarkup(reply_keyboard, True)
    Update.message.reply_text('Working with', reply_markup=mark_key)
    return CHOICE_NUMBER


def choice_number(update, _):
    user = Update.message.from_user
    num = Update.message.text
    if num == 'Rational':
        mark_key = ReplyKeyboardMarkup(
            operation_keybord_main, one_time_keyboard=True)
        update.message.reply_text(
            'Chose mathematical action', reply_markup=mark_key)
        logger.info('User %s chose rational numbers', user.first_name)
        return CHOICE_OPERATION
    elif num == 'Complex':
        mark_key = ReplyKeyboardMarkup(
            operation_keybord_main, one_time_keyboard=True)
        update.message.reply_text(
            'Chose mathematical action', reply_markup=mark_key)
        logger.info('User %s chose rational numbers', user.first_name)
        return CHOICE_OPERATION
    elif num == 'Exit':
        logger.info('User %s exited out', user.first_name)
        update.message.reply_text(
            'Goodbye!', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        pass


def choice_operation(update, _):
    operation = Update.message.text
    if operation == 'Addition':
       update.message.reply_text('Enter two numbers divided by space')
       return ADDITION_NUMS
    elif operation == 'Subtraction':
       update.message.reply_text('Enter two numbers divided by space')
       return SUBSTRACTION_NUMS
    elif operation == 'Multiply':
       update.message.reply_text('Enter two numbers divided by space')
       return MULTIPLY
    elif operation == 'Division':
       update.message.reply_text('Enter two numbers divided by space')
       return DIVISION
    elif operation == 'Exponentiation':
       update.message.reply_text('Enter two numbers divided by space')
       return EXPONENTIATION_NUMS
    elif operation == 'Sqrt':
       update.message.reply_text('Enter a number')
       return SQRT_NUM
    elif operation == 'Menu':
       update.message.reply_text('Return to menu')
       return MENU
    else:
        pass
    
def addition(update, _):
    user = Update.message.from_user
    numbers = Update.message.text
    print(numbers)
    list_nums = numbers.split()
    try:
        a = float(list_nums[0])
        b = float(list_nums[1])
        update.message.reply_text(f'{a} + {b} = {a + b}')
        logger.info('Users %s operation: %s + %s = %s', user.first_name, a, b, a + b)
        return CHOICE_OPERATION
    except:
        update.message.reply_text('You are wrong, try again')
        return CHOICE_NUMBER

def subtraction(update, _):
    user = Update.message.from_user
    numbers = Update.message.text
    print(numbers)
    list_nums = numbers.split()
    try:
        a = float(list_nums[0])
        b = float(list_nums[1])
        update.message.reply_text(f'{a} - {b} = {a - b}')
        logger.info('Users %s operation: %s - %s = %s', user.first_name, a, b, a - b)
        return CHOICE_OPERATION
    except:
        update.message.reply_text('You are wrong, try again')
        return CHOICE_NUMBER
   
def multiply(update, _):
    user = Update.message.from_user
    numbers = Update.message.text
    print(numbers)
    list_nums = numbers.split()
    try:
        a = float(list_nums[0])
        b = float(list_nums[1])
        update.message.reply_text(f'{a} * {b} = {a * b}')
        logger.info('Users %s operation: %s * %s = %s', user.first_name, a, b, a * b)
        return CHOICE_OPERATION
    except:
        update.message.reply_text('You are wrong, try again')
        return CHOICE_NUMBER

def division(update, _):
    user = Update.message.from_user
    numbers = Update.message.text
    print(numbers)
    list_nums = numbers.split()
    try:
        a = float(list_nums[0])
        b = float(list_nums[1])
        if b != 0:
            update.message.reply_text(f'{a} / {b} = {a / b}')
            logger.info('Users %s operation: %s / %s = %s', user.first_name, a, b, a / b)
            return CHOICE_OPERATION
        else:
            update.message.reply_text('You can not divide on zero.Try again ')
            return CHOICE_NUMBER
    except:
        update.message.reply_text('You are wrong, try again')
        return CHOICE_NUMBER    
    
def exponentiation(update, _):
    user = Update.message.from_user
    numbers = Update.message.text
    print(numbers)
    list_nums = numbers.split()
    try:
        a = float(list_nums[0])
        b = float(list_nums[1])
        update.message.reply_text(f'{a} ^ {b} = {a ** b}')
        logger.info('Users %s operation: %s ^ %s = %s', user.first_name, a, b, a ** b)
        return CHOICE_OPERATION
    except:
        update.message.reply_text('You are wrong, try again')
        return CHOICE_NUMBER   
    
def sqrt(update, _):
    user = Update.message.from_user
    number = Update.message.text
    print(number)
    try:
        update.message.reply_text(f'√{number} = {sqrt(number)}')
        logger.info('Users %s operation: √%s = %s', user.first_name, number, sqrt(number))
        return CHOICE_OPERATION
    except:
        update.message.reply_text('You are wrong, try again')
        return CHOICE_NUMBER     

def cancel(update, _):
    user = update.message.from_user
    logger.info("User %s want to end calculator", user.first_name)
    update.message.reply_text('By ', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
    
    
if __name__ == '__main__':
    updater = Updater("5746019679:AAGkT6XD-DXxuMeQ_AMr2zcNE936FyWvdwY")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler( 
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [MessageHandler(Filters.regex('^(Start)$'), menu)],
            CHOICE_NUMBER: [MessageHandler(Filters.regex('^(Rational|Complex|Exit)$'), choice_number)],
            CHOICE_OPERATION: [MessageHandler(Filters.regex(f'^{operation_keybord_main}$'), choice_operation)],
            ADDITION_NUMS: [MessageHandler(Filters.text&~Filters.command, addition)],
            SUBSTRACTION_NUMS: [MessageHandler(Filters.text&~Filters.command, subtraction)],
            MULTIPLY: [MessageHandler(Filters.text&~Filters.command, multiply)],
            DIVISION: [MessageHandler(Filters.text&~Filters.command, division)],
            EXPONENTIATION_NUMS: [MessageHandler(Filters.text&~Filters.command, exponentiation)],
            SQRT_NUM: [MessageHandler(Filters.text&~Filters.command, sqrt)],
            
        },
        
        fallbacks=[CommandHandler('cancel', cancel)],
    )

dispatcher.add_handler(conv_handler)

   
updater.start_polling()
updater.idle()

    
    
