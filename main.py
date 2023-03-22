from random import randint


random_number = randint(1, 100)
counter = 1
starts = 'да'
print('Добро пожаловать в числовую угадайку!')


def is_valid(x):
    if x.isdigit():
        if 1 <= int(x) <= 100:
            return True
        else:
            return False
    else:
        return False


number = input('Введите число от 1 до 100: ')
while starts.lower() == 'да':
    if is_valid(number) == True:
        if int(number) < random_number:
            number = input('Ваше число меньше загаданного, попробуйте еще разок: ')
            is_valid(number)
            counter += 1
        elif int(number) > random_number:
            number = input('Ваше число больше загаданного, попробуйте еще разок: ')
            is_valid(number)
            counter += 1
        else:
            print('Вы угадали, c', counter, 'попытки, поздравляем!')
            starts = input('Если хотите сыграть ещё раз, напишите да: ')
            if starts.lower() == 'да':
                random_number = randint(1, 100)
                number = input('Введите число от 1 до 100: ')
                counter = 1
            else:
                break
    else:
        number = input('А может быть все-таки введем целое число от 1 до 100?) : ')
        is_valid(number)

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
