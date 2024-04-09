import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, ConversationHandler, CommandHandler, MessageHandler, filters
from config import TOKEN_BOT
from telegram import ReplyKeyboardRemove


reply_keyboard = [['/aries', '/taurus', '/twins', '/cancer'],
                  ['/lion', '/virgo', '/scales', '/scorpion'],
                  ['/sagittarius', '/carpicorn', '/aquarius', '/fish']]
key = [['/information', '/compatibility'], ['/humor', '/back']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(key, one_time_keyboard=False)

#словарь для хранения файлов текстовых про совместимость и информацию
slovar = {1: ['OB/ХО.txt', 'OB/COV.txt'],
          2: ['TE/XAR.txt', 'TE/COV.txt'],
          3: ['BL/XAR.txt', 'BL/COV.txt'],
          4: ['RA/XAR.txt', 'RA/COV.txt'],
          5: ['LE/XAR.txt', 'LE/COV.txt'],
          6: ['DE/XAR.txt', 'DE/COV.txt'],
          7: ['VE/XAR.txt', 'VE/COV.txt'],
          8: ['SC/XAR.txt', 'SC/COV.txt'],
          9: ['ST/XAR.txt', 'ST/COV.txt'],
          10: ['KO/XAR.txt', 'KO/COV.txt'],
          11: ['VO/XAR.txt', 'VO/COV.txt'],
          12: ['RI/XAR.txt', 'RI/COV.txt']}


slovar2 = {1: 'Когда у папы Овна родилась девочка, а не мальчик:\n'
              '- Если тебя оскорбляют, унижают, бей обидчика лопатой по морде!\n'
              '- Ну, папа! Я же девочка!\n'
              '- Можешь взять розовую.',
           2: 'Когда муж - Телец.\n'
              '-Жена звонит мужу на работу:\n'
              '- Милый, вместо таблеток от поноса я положила тебе таблетки от нервов. Ты как?\n'
              '- Наложил в штаны, но абсолютно спокоен.',
           3: 'Пациент-Близнецы:\n'
              '- Доктор, мне кажется, что у меня раздвоение личности: будто меня много!\n'
              '- Повторите еще раз, только не все сразу!',
           4: 'Поймали людоеды двух мужиков и спрашивают:\n'
              '- Вы кто по знаку зодиака?\n'
              '- Я – Овен.\n'
              '- Я - Рак.\n'
              '- Тогда значит, баранина – основное блюдо, вареные раки – на десерт',
           5: 'Лев на собеседовании:\n'
              '-Назовите ваши сильные стороны.\n'
              '- Амбициозность.\n'
              '- Мы свяжемся с вами в понедельник.\n'
              '- Не надо, к тому времени у меня уже будет работа.',
           6: 'Про жен, рожденных под знаком Дева:\n'
              'Два опера звонят с докладом в убойный отдел.\n'
              '- Что у вас?\n '
              '- Покушение на убийство. Мужчина 37 лет. Его жена ударила 6 раз сковородой за то, что он наступил'
              ' на мокрый, только что вымытый пол. Мужчина в тяжелом состоянии в больнице.\n'
              '- Жену задержали?\n'
              '- Нет, пол еще мокрый!',
           7: 'Лучшая иллюстрация к характеру Весов: въехал в столб на велосипеде, не решив, с какой стороны его объехать.',
           8: 'Психолог спрашивает у женщины-Скорпионши:\n'
              '-Как бы вы себя назвали, если бы узнали, что муж вам изменяет?\n'
              '- Вдовой!',
           9: 'Стрелец на собеседовании:\n'
              '- Назовите Ваш главный недостаток.\n'
              '- Прямолинейность.\n'
              '- Ну, нам кажется, это достоинство.\n'
              '- А мне все равно, что вам там кажется!',
           10: 'Козерог читает гороскоп: "В августе Козерогов ждет финансовая стабильность"\n'
               '- Понятно… Денег так и не будет',
           11: '– Чё хмурый такой?\n'
              '– Да гороскоп фиговый… «Водолей может узнать об измене близкого человека».\n'
              '– Ты разве водолей?\n'
              '– Жена водолейка…',
           12: 'Мама ребенку, рожденному под знаком Рыбы:\n'
               '- Сынок, собери свои игрушки!\n'
               '- Да ну, мам, я лучше в углу постою!'}
count = 0


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


async def echo(update, context):
    sp = ['овен', 'телец', 'близнецы', 'рак', 'лев', 'дева', 'весы', 'скорпион', 'стрелец', 'козерог', 'водолей', 'рыбы']
    if update.message.text.lower() in sp:
        global count
        global slovar
        count = sp.index(update.message.text.lower()) + 1
        await update.message.reply_text(
            update.message.text.lower(), reply_markup=markup2)
        f = open(slovar[count][0], "r", encoding="utf-8")
        ff = f.readlines()
        itog = "\n".join(ff)
        await update.message.reply_text(
            itog, reply_markup=markup2)
    else: await update.message.reply_text('Ты шлёшадь!!!!')

#выгрузка информации про зз
async def a(update, context):
    global slovar
    global count
    f = open(slovar[count][0], "r", encoding="utf-8")
    ff = f.readlines()
    itog = "\n".join(ff)
    await update.message.reply_text(
        itog, reply_markup=markup2)

#выгрузка совместимости зз
async def b(update, context):
    global slovar
    global count
    f = open(slovar[count][1], "r", encoding="utf-8")
    ff = f.readlines()
    itog = "\n".join(ff)
    await update.message.reply_text(
        itog, reply_markup=markup2)


async def hum(update, context):
    global slovar2
    global count
    await update.message.reply_text(
        slovar2[count], reply_markup=markup2)


#овен
async def aries(update, context):
    await update.message.reply_text(
        "Овен", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('OB/aries.jpg', 'rb'))
    global count
    count = 1


#телец
async def taurus(update, context):
    await update.message.reply_text(
        "Телец", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('TE/taurus.jpg', 'rb'))
    global count
    count = 2


#близнецы
async def twins(update, context):
    await update.message.reply_text(
        "Близнецы", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('BL/gemini.jpg', 'rb'))
    global count
    count = 3


#рак
async def cancer(update, context):
    await update.message.reply_text(
        "Рак", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('RA/cancer.jpg', 'rb'))
    global count
    count = 4


#лев
async def lion(update, context, bot=None):
    await update.message.reply_text(
        "Лев", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('LE/lion.jpg', 'rb'))
    global count
    count = 5


#дева
async def virgo(update, context):
    await update.message.reply_text(
        "Дева", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('DE/virgo.jpg', 'rb'))
    global count
    count = 6


#весы
async def scales(update, context):
    await update.message.reply_text(
        "Весы", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('VE/libra.jpg', 'rb'))
    global count
    count = 7


#скорпион
async def scorpion(update, context):
    await update.message.reply_text(
        "Скорпион", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('SC/scorpio.jpg', 'rb'))
    global count
    count = 8


#стрелец
async def sagittarius(update, context):
    await update.message.reply_text(
        "Стрелец", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('ST/sagittarius.jpg', 'rb'))
    global count
    count = 9


#козерог
async def carpicorn(update, context):
    await update.message.reply_text(
        "Козерог", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('KO/capricorn.jpg', 'rb'))
    global count
    count = 10


#водолей
async def aquarius(update, context):
    await update.message.reply_text(
        "Водолей", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('VO/aquarius.jpg', 'rb'))
    global count
    count = 11


#рыбы
async def fish(update, context):
    await update.message.reply_text(
        "Рыбы", reply_markup=markup2)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('RI/pisces.jpg', 'rb'))
    global count
    count = 12


async def back(update, context):
    await update.message.reply_text(
        "вернулись назад", reply_markup=markup)


async def start(update, context):
    await update.message.reply_text(
        "Выберите знак, про который хотите узнать больше\n"
        "aries - овен (21.03 - 20.04)\n"
        "taurus - телец (21.04 - 20.05)\n"
        "twins - близнецы (21.05 - 21.06)\n"
        "cancer - рак (22.06 - 22.07)\n"
        'lion - лев (23.07 - 23.08) \n'
        'virgo - дева (24.08 - 23.09)\n'
        'scales - весы (24.09 - 23.10)\n'
        'scorpion - скорпион (24.10 - 22.11)\n'
        'sagittarius - стрелец (23.11 - 21.12)\n'
        'carpicorn - козерог(22.12 - 20.01)\n'
        'aquarius - водолей (21.01 - 20.02)\n'
        'fish - рыбы (21.02 - 20.03)\n',
        reply_markup=markup)


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    application = Application.builder().token(TOKEN_BOT).build()
    application.add_handler(CommandHandler("aries", aries))
    application.add_handler(CommandHandler("taurus", taurus))
    application.add_handler(CommandHandler("twins", twins))
    application.add_handler(CommandHandler("cancer", cancer))
    application.add_handler(CommandHandler("lion", lion))
    application.add_handler(CommandHandler("virgo", virgo))
    application.add_handler(CommandHandler("scales", scales))
    application.add_handler(CommandHandler("scorpion", scorpion))
    application.add_handler(CommandHandler("sagittarius", sagittarius))
    application.add_handler(CommandHandler("carpicorn", carpicorn))
    application.add_handler(CommandHandler("aquarius", aquarius))
    application.add_handler(CommandHandler("fish", fish))
    application.add_handler(CommandHandler("information", a))
    application.add_handler(CommandHandler("compatibility", b))
    application.add_handler(CommandHandler("humor", hum))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("echo", a))
    text_handler = MessageHandler(filters.TEXT, echo)

    # Регистрируем обработчик в приложении.
    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()