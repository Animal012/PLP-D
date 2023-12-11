while True:
    try:
        import telebot
        from telebot import types

        bot = telebot.TeleBot('###')

        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            if message.text == "оценить":
                bot.send_message(message.from_user.id, "Привет, что ты хочешь оценить сегодня?")
                keyboard = types.InlineKeyboardMarkup()
                key_film = types.InlineKeyboardButton(text='Фильм', callback_data='film')
                keyboard.add(key_film)
                key_series = types.InlineKeyboardButton(text='Сериал', callback_data='series')
                keyboard.add(key_series)
                bot.send_message(message.from_user.id, text='Выбери, что хочешь оценить', reply_markup=keyboard)
                bot.register_next_step_handler(message, get_film_or_series)
            elif message.text == "/help":
                bot.send_message(message.from_user.id, 'Иди учи уроки, дебил, какая тебе помощь?')#"Напиши: оценить, рейтинг фильмов, рейтинг сериалов, поиск фильма, поиск сериала"
            elif message.text == 'рейтинг фильмов' or message.text == 'список фильмов':
                with open('films.txt', 'r') as f:
                    for n, line in enumerate(f, 1):
                        line = line.rstrip('\n')                                  
                        bot.send_message(message.from_user.id, line)
            elif message.text == 'рейтинг сериалов' or message.text == 'список сериалов':
                with open('series.txt', 'r') as f:
                    for n, line in enumerate(f, 1):
                        line = line.rstrip('\n')                                  
                        bot.send_message(message.from_user.id, line)
            elif message.text == 'поиск фильма' or message.text == 'найти фильм':
                bot.send_message(message.from_user.id, "Название фильма")
                bot.register_next_step_handler(message, search_film)
            elif message.text == 'поиск сериала' or message.text == 'найти сериал':
                bot.send_message(message.from_user.id, "Название сериала")
                bot.register_next_step_handler(message, search_series)
            elif message.text == 'списки':
                bot.send_message(message.from_user.id, "Выберите список")
                keyboard = types.InlineKeyboardMarkup()
                key_tar = types.InlineKeyboardButton(text='9 фильмов Тарантино', callback_data='Tarantino')
                keyboard.add(key_tar)
                key_guy = types.InlineKeyboardButton(text='Гай Ричи', callback_data='Ritchie')
                keyboard.add(key_guy)
                key_nol = types.InlineKeyboardButton(text='Нолан', callback_data='Nolan')
                keyboard.add(key_nol)
                bot.send_message(message.from_user.id, text='Что показать?', reply_markup=keyboard)                        
            else:
                bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

        flag = ''
        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            global flag
            if call.data == 'film':
                bot.send_message(call.message.chat.id, 'Какое название у фильма?')
                flag = True
            elif call.data == 'series':
                bot.send_message(call.message.chat.id, 'Какое название у сериала?')
                flag = False
            elif call.data == 'rating_film_1':
                bot.send_message(call.message.chat.id, film + ' 1/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 1/10\n')
            elif call.data == 'rating_film_2':
                bot.send_message(call.message.chat.id, film + ' 2/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 2/10\n')
            elif call.data == 'rating_film_3':
                bot.send_message(call.message.chat.id, film + ' 3/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 3/10\n')
            elif call.data == 'rating_film_4':
                bot.send_message(call.message.chat.id, film + ' 4/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 4/10\n')
            elif call.data == 'rating_film_5':
                bot.send_message(call.message.chat.id, film + ' 5/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 5/10\n')
            elif call.data == 'rating_film_6':
                bot.send_message(call.message.chat.id, film + ' 6/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 6/10\n')
            elif call.data == 'rating_film_7':
                bot.send_message(call.message.chat.id, film + ' 7/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 7/10\n')
            elif call.data == 'rating_film_8':
                bot.send_message(call.message.chat.id, film + ' 8/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 8/10\n')
            elif call.data == 'rating_film_9':
                bot.send_message(call.message.chat.id, film + ' 9/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 9/10\n')
            elif call.data == 'rating_film_10':
                bot.send_message(call.message.chat.id, film + ' 10/10')
                with open('films.txt', 'a') as f:
                    f.write(film + ' 10/10\n')
            elif call.data == 'rating_series_1':
                bot.send_message(call.message.chat.id, series + ' 1/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 1/10\n')
            elif call.data == 'rating_series_2':
                bot.send_message(call.message.chat.id, series + ' 2/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 2/10\n')
            elif call.data == 'rating_series_3':
                bot.send_message(call.message.chat.id, series + ' 3/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 3/10\n')
            elif call.data == 'rating_series_4':
                bot.send_message(call.message.chat.id, series + ' 4/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 4/10\n')
            elif call.data == 'rating_series_5':
                bot.send_message(call.message.chat.id, series + ' 5/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 5/10\n')
            elif call.data == 'rating_series_6':
                bot.send_message(call.message.chat.id, series + ' 6/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 6/10\n')
            elif call.data == 'rating_series_7':
                bot.send_message(call.message.chat.id, series + ' 7/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 7/10\n')
            elif call.data == 'rating_series_8':
                bot.send_message(call.message.chat.id, series + ' 8/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 8/10\n')
            elif call.data == 'rating_series_9':
                bot.send_message(call.message.chat.id, series + ' 9/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 9/10\n')
            elif call.data == 'rating_series_10':
                bot.send_message(call.message.chat.id, series + ' 10/10')
                with open('series.txt', 'a') as f:
                    f.write(series + ' 10/10\n')
            elif call.data == 'Tarantino':
                with open('Tarantino.txt', 'r') as f:
                    for n, line in enumerate(f, 1):
                        line = line.rstrip('\n')                                  
                        bot.send_message(call.message.chat.id, line)
            elif call.data == 'Ritchie':
                with open('Ritchie.txt', 'r') as f:
                    for n, line in enumerate(f, 1):
                        line = line.rstrip('\n')                                  
                        bot.send_message(call.message.chat.id, line)
            elif call.data == 'Nolan':
                with open('Nolan.txt', 'r') as f:
                    for n, line in enumerate(f, 1):
                        line = line.rstrip('\n')                                  
                        bot.send_message(call.message.chat.id, line)
          
        film = ''
        series = ''
        @bot.message_handler(content_types=['text'])
        def get_film_or_series(message):
            if flag:
                global film
                film = message.text
                keyboard = types.InlineKeyboardMarkup()
                key_1 = types.InlineKeyboardButton(text='1', callback_data='rating_film_1')
                keyboard.add(key_1)
                key_2 = types.InlineKeyboardButton(text='2', callback_data='rating_film_2')
                keyboard.add(key_2)
                key_3 = types.InlineKeyboardButton(text='3', callback_data='rating_film_3')
                keyboard.add(key_3)
                key_4 = types.InlineKeyboardButton(text='4', callback_data='rating_film_4')
                keyboard.add(key_4)
                key_5 = types.InlineKeyboardButton(text='5', callback_data='rating_film_5')
                keyboard.add(key_5)
                key_6 = types.InlineKeyboardButton(text='6', callback_data='rating_film_6')
                keyboard.add(key_6)
                key_7 = types.InlineKeyboardButton(text='7', callback_data='rating_film_7')
                keyboard.add(key_7)
                key_8 = types.InlineKeyboardButton(text='8', callback_data='rating_film_8')
                keyboard.add(key_8)
                key_9 = types.InlineKeyboardButton(text='9', callback_data='rating_film_9')
                keyboard.add(key_9)
                key_10 = types.InlineKeyboardButton(text='10', callback_data='rating_film_10')
                keyboard.add(key_10)                        
                bot.send_message(message.from_user.id, text='Какую оценку поставишь фильму?', reply_markup=keyboard)
            else:
                global series
                series = message.text
                keyboard = types.InlineKeyboardMarkup()
                key_1 = types.InlineKeyboardButton(text='1', callback_data='rating_series_1')
                keyboard.add(key_1)
                key_2 = types.InlineKeyboardButton(text='2', callback_data='rating_series_2')
                keyboard.add(key_2)
                key_3 = types.InlineKeyboardButton(text='3', callback_data='rating_series_3')
                keyboard.add(key_3)
                key_4 = types.InlineKeyboardButton(text='4', callback_data='rating_series_4')
                keyboard.add(key_4)
                key_5 = types.InlineKeyboardButton(text='5', callback_data='rating_series_5')
                keyboard.add(key_5)
                key_6 = types.InlineKeyboardButton(text='6', callback_data='rating_series_6')
                keyboard.add(key_6)
                key_7 = types.InlineKeyboardButton(text='7', callback_data='rating_series_7')
                keyboard.add(key_7)
                key_8 = types.InlineKeyboardButton(text='8', callback_data='rating_series_8')
                keyboard.add(key_8)
                key_9 = types.InlineKeyboardButton(text='9', callback_data='rating_series_9')
                keyboard.add(key_9)
                key_10 = types.InlineKeyboardButton(text='10', callback_data='rating_series_10')
                keyboard.add(key_10)                        
                bot.send_message(message.from_user.id, text='Какую оценку поставишь сериалу?', reply_markup=keyboard)

        @bot.message_handler(content_types=['text'])
        def search_film(message):
            require = message.text
            with open('films.txt', 'r') as f:
                s = f.readlines()
                flag1 = True
                for i in range(len(s)):
                    if require in s[i]:
                        flag1 = False
                        bot.send_message(message.from_user.id, s[i])
                if flag1:
                    bot.send_message(message.from_user.id, 'Такого фильма не найдено')

        @bot.message_handler(content_types=['text'])
        def search_series(message):
            require = message.text
            with open('series.txt', 'r') as f:
                s = f.readlines()
                flag1 = True
                for i in range(len(s)):
                    if require in s[i]:
                        flag1 = False
                        bot.send_message(message.from_user.id, s[i])
                if flag1:
                    bot.send_message(message.from_user.id, 'Такого сериала не найдено')

        bot.polling(none_stop=True, timeout=0)
    except:
        pass