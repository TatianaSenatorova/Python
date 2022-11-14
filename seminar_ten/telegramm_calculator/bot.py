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

MENU, CHOICE_NUMBER, CHOICE_OPERATION, ADDITION_NUMS, SUBSTRACTION_NUMS, EXPONENTIATION_NUMS, SQRT_NUM, DIVISION_NUMS = range(9)

def start(update, _):
    update.message.reply_text("Calculator welcomes you! Enter any button to prolong. ")
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
        mark_key = ReplyKeyboardMarkup(operation_keybord_main, one_time_keyboard = True)
        update.message.reply_text('Chose mathematical action', reply_markup=mark_key)
        logger.info('User %s chose rational numbers', user.first_name)
        return CHOICE_OPERATION
    elif num == 'Complex':
        mark_key = ReplyKeyboardMarkup(operation_keybord_main, one_time_keyboard = True)
        update.message.reply_text('Chose mathematical action', reply_markup=mark_key)
        logger.info('User %s chose rational numbers', user.first_name)
        return CHOICE_OPERATION
    elif num == 'Exit':
        logger.info('User %s exited out', user.first_name)
        update.message.reply_text('Goodbye!', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        pass





    print("Calculator welcomes you!\n")
    while True:
        type_num = input("Working with:"
                         "\n1 - rational"
                         "\n2 - complex"
                         "\n3 - exit\n")
        match type_num:
            case "1" | "2":
                menu_calc(type_num)
            case "3":
                logging.info(f"Stop program.")
                print("Goodbye! See you soon sun!")
                break
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("The menu item is not recognized. Try again!")




def start(update, _):
   def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Вещественные числа', 'Комплексные числа']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Добро пожаловать в калькулятор. '
        'Команда /cancel, чтобы прекратить разговор.\n\n'
        'Выберите тип чисел для работы',
        reply_markup=markup_key,)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return GENDER

def choice(update, _):
    global player, count
    move = update.message.text
    move = int(move)
    if move not in fld:
        update.message.reply_text(f"Incorrect input{chr(9940)}\nTry again")
    else:
        fld.insert(fld.index(move), player)
        fld.remove(move)
        update.message.reply_text(show_field(fld))
        if check_win(fld):
            update.message.reply_text(f"{player} - CHAMPION{chr(127942)}{chr(127881)}")
            return ConversationHandler.END
        player = o if player == x else x
        count -= 1

    if count == 0:
        update.message.reply_text(f"Draw {chr(129309)}")
        return ConversationHandler.END


def cancel(update, _):
    update.message.reply_text('Bye', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(token)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.text, choice)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    print('server start')

    updater.start_polling()
    updater.idle()

# Определяем константы этапов разговора
GENDER, PHOTO, LOCATION, BIO = range(4)

# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Вещественные числа', 'Комплексные числа']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Добро пожаловать в калькулятор. '
        'Команда /cancel, чтобы прекратить разговор.\n\n'
        'Выберите тип чисел для работы',
        reply_markup=markup_key,)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return GENDER

# Обрабатываем пол пользователя
def gender(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Пол %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Хорошо. Пришли мне свою фотографию, чтоб я знал как ты '
        'выглядишь, или отправь /skip, если стесняешься.',
        reply_markup=ReplyKeyboardRemove(),
    )
    # переходим к этапу `PHOTO`
    return PHOTO

# Обрабатываем фотографию пользователя
def photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем фото 
    photo_file = update.message.photo[-1].get_file()
    # скачиваем фото 
    photo_file.download(f'{user.first_name}_photo.jpg')
    # Пишем в журнал сведения о фото
    logger.info("Фотография %s: %s", user.first_name, f'{user.first_name}_photo.jpg')
    # Отвечаем на сообщение с фото
    update.message.reply_text(
        'Великолепно! А теперь пришли мне свое'
        ' местоположение, или /skip если параноик..'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем команду /skip для фото
def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
        ' свое местоположение, или /skip если параноик.'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем местоположение пользователя
def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.location
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!' 
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу `BIO`
    return BIO

# Обрабатываем команду /skip для местоположения
def skip_location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем на сообщение с пропущенным местоположением
    update.message.reply_text(
        'Точно параноик! Ну ладно, тогда расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу `BIO`
    return BIO

# Обрабатываем сообщение с рассказом/биографией пользователя
def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text('Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("TOKEN")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            LOCATION: [
                MessageHandler(Filters.location, location),
                CommandHandler('skip', skip_location),
            ],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()