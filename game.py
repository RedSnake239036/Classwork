import random


numb = random.randrange(10, 100, 1)


def start():
    inte = random.randrange(10, 100, 1)
    counter = 5
    print('Компьютер (я) загадал двузначное число, ваша задача угадать его, даётся 5 попыток')
    while counter > 0:
        counter -= 1
        x = int(input('Введите число: '))
        if x > inte:
            print('Много, осталось {} попыток'.format(counter))

        elif x < inte:
            print('Мало, осталось {} попыток'.format(counter))

        elif x == inte:
            print('Угадал, поздравляю! :-)')
            counter = -1

    if counter == 0: print('Попытки закончились, ты проиграл :-(')



