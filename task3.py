import random

import telebot

bot = telebot.TeleBot('1876668052:AAHH4gxDamEJSTOskL2k_lP-AAoatQ1WDhc')
spisok_slov = ['телефон', 'цепочка', 'мёд', 'сумка', 'плащ', 'мир', 'окно', 'обувь', 'кот', 'проектор', 'студент']

data = {}


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Чтобы сыграть введите: /play")
    if message.text == '/play':
        slovo = random.choice(spisok_slov)
        s = '_ ' * len(slovo)
        bot.send_message(message.from_user.id, f"{s}\nВведите букву")
        kwargs = {"slovo": slovo}
        data[message.from_user.id] = {'word': slovo, 'list_char': [], 'errors': 0}
        # bot.register_next_step_handler(message, start_game, slovo)
    else:
        print(data)
        if data.get(message.from_user.id):
            bukva = (message.text).lower()
            if len(bukva) == 1 and bukva.isalpha():
                data[message.from_user.id]['list_char'].append(bukva)
                 # list_char.append(bukva)
                spisok_res = []
                for item in data[message.from_user.id]['word']:
                    if item in data[message.from_user.id]['list_char']:
                        spisok_res += item
                    else:
                        spisok_res += '_'
                res = ' '.join(spisok_res)
                if bukva not in data[message.from_user.id]['word']:
                    data[message.from_user.id]['errors'] += 1
                bot.send_message(message.from_user.id, res)
                if '_' not in spisok_res:
                    bot.send_message(message.from_user.id, 'you win!')
                    del data[message.from_user.id]
                    return
                if data[message.from_user.id]['errors'] == 10:
                    bot.send_message(message.from_user.id, 'you lose')
                    del data[message.from_user.id]
                    return
            else:
                bot.send_message(message.from_user.id, "Введите только одну букву!")
        # bot.send_message(message.from_user.id, 'Напиши /start')


bot.polling(none_stop=True, interval=0)
