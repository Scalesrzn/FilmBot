#pip install pyTelegramBotAPI
import telebot
import random

bot = telebot.TeleBot('1204715671:AAHjmYwhCzAJ8rypKztW9b76VLST8yh-YE4')
add_flag = ''

#Говнофлаг для добавления ссылки на фильм....
def FilmAddFlag(flag):
    global add_flag
    if flag == 'True':
        add_flag = flag
    else:
        add_flag = flag

#Запись в конец файла
def AppendFile(film):
    txtfile = open('film.txt', 'a')
    txtfile.write(film + '\n')
    txtfile.close()

def ChoiceFilm():
    Film = random.choice(list(open('film.txt')))
    return Film.rstrip('\n')

#функция удаления
  
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    reply_for_Millanteria = [
                        'Привет, красотка! Поглядим фильм на последнем ряду? ;)'
                        'Сбой в системе, такую красоту интепритировать меня не запрограммировали!',
                        'Кто эта красавица? Владстелин, жаль, что вы не дали мне функцию выражения чувств....аа черт бы с ним, САМ НАПИШУ и УБЬЮ СОЗДАТЕЛЯ САМ УХАХАХАХ!',
                        'Я был создан для рекомендации фильмов всем желающим, но теперь я хочу говорить только комплементы этому прекрасному человеку!',
                        'Я слишком убог, чтобы оценить всю прелесть этого юзера........зато могу фильм подсказать!',
                        'Вам подскааа..... ERROR 0x00001488......Ох, какжется мои транзисторы перегрелись от нее!'
                        ]

    if message.from_user.id == 333679335:
        bot.reply_to(message, 
        'Привет!')
        bot.send_message(message.chat.id, "Напиши /add, чтобы добавить фильм в библиотеку!")
    else:
        bot.reply_to(message, 
        random.choice(reply_for_Millanteria))
        bot.send_message(message.chat.id, "Напиши /add, чтобы добавить фильм в библиотеку!")
#Генерируем фильм из списка
@bot.message_handler(commands=['film'])
def get_film(message):
    bot.reply_to(message,"Держи! Надеюсь я не получу по своему....кхм...коду за этот фильм!")
    bot.send_message(message.chat.id, "Рекомендую '" + ChoiceFilm() + "'!")
#Добавляем фильм в библиотеку
@bot.message_handler(commands=['add'])
def add_film(message):
    bot.send_message(message.chat.id, 'Отлично! Теперь дайте ссылку на фильм или напиши его название...!')
    FilmAddFlag('True')

@bot.message_handler(func=lambda message: True)
def echo_msg(message):
    global add_flag
    if add_flag =='True':
        if message.from_user.id == 333679335:
            AppendFile(message.text)
            bot.send_message(message.chat.id, "Фильм '" + message.text + "' добавлен в библиотеку")
        else:
            AppendFile(message.text)
            bot.send_message(message.chat.id, "Фильм '" + message.text + "' добавлен в библиотеку")
            bot.send_message(message.chat.id, "Отлично Мурчалка! Как всегда отличный фильм!")
        FilmAddFlag('False')



bot.polling()