from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
import random


TOKEN = '5074265255:AAFxaqNg_2hNkf-DflbwNXN4rZkMIKGw3QM'

def zapis(update, context):
    try:
        a = (update.message.text).split()
        if len(a) > 1:
            w = open(f'slova//fraz.txt')
            q = w.readlines()
            w = open(f'slova//fraz.txt', mode='w')
            q = q + [' '.join(a)]
            w.write('$'.join(q))
        for i in a:
            if len(i) > 4:
                if i[len(i) - 2: len(i)] in ['ть', 'ли', 'ла', 'ло', 'ил']:
                    f = open('slova\glag.txt')
                    f = f.readline().split()
                    w = open('slova\glag.txt', mode='w')
                    w.write(' '.join(f + [i]))
                elif i[len(i) - 2: len(i)] in ['ый', 'ая', 'ые', 'ое', 'ую', 'ой', 'ом', 'ых', 'го']:
                    f = open('slova\pril.txt')
                    f = f.readline().split()
                    w = open('slova\pril.txt', mode='w')
                    w.write(' '.join(f + [i]))
                else:
                    f = open('slova\susch.txt')
                    f = f.readline().split()
                    w = open('slova\susch.txt', mode='w')
                    w.write(' '.join(f + [i]))
    except Exception:
        print(update.message.text)


def random_word(update, context):
    s = ('susch','glag','pril')
    f11 = open(f'slova\{s[random.randint(0, 2)]}.txt').readlines()[0].split()
    f22 = open(f'slova\{s[random.randint(0, 2)]}.txt').readlines()[0].split()
    f1 = f11[random.randint(0, len(f11) - 1)]
    s = []
    q = 4
    while s == [] and q > 0:
        for i in f22:
            if f1[len(f1) - q:len(f1)] ==  i[0:q]:
                s.append(f1[len(f1) - q:len(f1)] + i[0:q])
        q = q - 1
    if len(s) == 0:
        f2 = f22[random.randint(1, len(f22) - 1)]
        a = (f1[0:len(f1) - random.randint(1, len(f1) - 3)] +
                                  f2[random.randint(0, 2):len(f2) - random.randint(0, 3)])
    else:
        a = (s[random.randint(0, len(s) - 1)])
    update.message.reply_text(a)


def random_fraz(update, context):
    try:
        if context.args:
            dlin = int(context.args[0])
        else:
            dlin = 5
        if dlin <= 0 or dlin > 10:
            update.message.reply_text('Неа')
        else:
            s = []
            w1 = open('slova\susch.txt').readline().split()
            w2 = open('slova\glag.txt').readline().split()
            w3 = open('slova\pril.txt').readline().split()
            w4 = open('slova//fraz.txt').readline().split('$')
            s1 = 25
            s2 = 25
            s3 = 25
            s4 = 25
            while len(s) < dlin:
                q = random.randint(0,99)
                if q < s1:
                    a = w1[random.randint(0,len(w1) - 1)]
                    if len(s) == 0 or a != s[len(s) - 1]:
                        s.append(a)
                        s1 -= 3
                        s2 += 1
                        s3 += 1
                        s4 += 1
                elif q < s2 + s1:
                    a = w2[random.randint(0, len(w2) - 1)]
                    if len(s) == 0 or a != s[len(s) - 1]:
                        s.append(a)
                        s1 += 1
                        s2 -= 3
                        s3 += 1
                        s4 += 1
                elif q < s3 + s2 + s1:
                    a = w3[random.randint(0, len(w3) - 1)]
                    if len(s) == 0 or a != s[len(s) - 1]:
                        s.append(a)
                        s1 += 1
                        s2 += 1
                        s3 -= 3
                        s4 += 1
                else:
                    a = w4[random.randint(0, len(w4) - 1)]
                    if len(s) == 0 or not(a in s[len(s) - 1]):
                        a = a.split()
                        while len(s) + len(a) > dlin:
                            a = a[0:len(a) - 1]
                        s = s + a
                        s1 += 1
                        s2 += 1
                        s3 += 1
                        s4 -= 3
            update.message.reply_text(' '.join(s))
    except Exception:
        update.message.reply_text('Браво, бот сломалсяб')


def gadalka(update, content):
    q = ['Возможно', 'Вероятно', 'Меня в это не втягивай', 'Конечно', 'Yes', 'Kyllä', 'Нет', 'Алёёё',
         'хочу пиццу', 'Несомненно', 'даже не надейся', 'я ничего не нашла по данному запросу']
    update.message.reply_text(q[random.randint(0, len(q) - 1)])



def start(update, context):
    reply_keyboard = [['/random_word', '/random_fraz'], ['/gadalka'], ['/close']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text('1',reply_markup=markup)

def close_keyboard(update, context):
    update.message.reply_text("Ok", reply_markup=ReplyKeyboardRemove())

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("random_word", random_word))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('gadalka', gadalka))
    dp.add_handler(CommandHandler('random_fraz', random_fraz))
    text_handler = MessageHandler(Filters.text, zapis)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()