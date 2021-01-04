import telebot


bot = telebot.TeleBot('1438072382:AAEQFN78BeUbhmkqQyFmsmaRBO9dc0GSo-s')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('времена', 'слова', 'мод.глаголы')
keyboard1.row('герундий','relative clauses','вводные фразы')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('active', 'passive')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('simple', 'continous', 'perfect')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('аctive', 'pаssive')
keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('аctivе','pаssivе')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, это твой помошник по английскому языку!!! /start', reply_markup=keyboard1)
    bot.send_message(message.chat.id, 'Чуть ниже ты можешь выбрать себе нужный пункт.', reply_markup=keyboard1)
#Времена/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'времена':
        bot.send_message(message.chat.id, 'Привет, выбери время которое тебе надою.',reply_markup=keyboard3)

    elif message.text.lower() == 'simple':
        bot.send_message(message.chat.id, 'Теперь вам нужно выбрать активную или пасивную форму.',reply_markup=keyboard2)


    elif message.text.lower() == 'active':
        bot.send_photo(message.chat.id, open('24365629_173220069.pdf-14.jpg', 'rb'))

    elif message.text.lower() == 'passive':
        bot.send_photo(message.chat.id, open('Screenshot_240-1.jpg', 'rb'))



    elif message.text.lower() == 'continous':
        bot.send_message(message.chat.id, 'Теперь вам нужно выбрать активную или пасивную форму.',reply_markup=keyboard4)


    elif message.text.lower() == 'аctive':
        bot.send_photo(message.chat.id, open('tenses3.jpg', 'rb'))

    elif message.text.lower() == 'pаssive':
        bot.send_photo(message.chat.id, open('open-uri20150909-7816-jl9z.jpg', 'rb'))



    elif message.text.lower() == 'perfect':
        bot.send_message(message.chat.id, 'Теперь вам нужно выбрать активную или пасивную форму.',reply_markup=keyboard6)

    elif message.text.lower() == 'аctivе':
        bot.send_photo(message.chat.id, open('tenses4.jpg', 'rb'))



    elif message.text.lower() == 'pаssivе':
        bot.send_photo(message.chat.id, open('open-uri20150909-7816-zunw2r.jpg', 'rb'))
# Времена////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Герундий////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif message.text.lower() == 'слова':
        bot.send_photo(message.chat.id, open('c3fcd61b4b9e034098aad035f7c24538.jpg', 'rb'))
#Модальные глаголы ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif message.text.lower() == 'мод.глаголы':
        bot.send_photo(message.chat.id, open('60431cd573.jpg', 'rb'))
#Relative clauses///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif message.text.lower() == 'relative clauses':
        bot.send_photo(message.chat.id, open('Screenshot_777.png', 'rb'))
        bot.send_photo(message.chat.id, open('Screensh.png', 'rb'))
#Вводные фразы///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif message.text.lower() == 'вводные фразы':
        bot.send_photo(message.chat.id, open('8.jpg', 'rb'))
        bot.send_photo(message.chat.id, open('unnamed.png', 'rb'))
        bot.send_photo(message.chat.id, open('uplo.jpg', 'rb'))

    elif message.text.lower() == 'герундий':
        bot.send_photo(message.chat.id, open('gerund.jpg', 'rb'))
        bot.send_photo(message.chat.id, open('444.jfif', 'rb'))
        video=open('videoplayback.mp4', 'rb')
        bot.send_video(message.chat.id, video)

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()