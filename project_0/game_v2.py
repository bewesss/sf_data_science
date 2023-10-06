import numpy as np
import random

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    start = 1  # минимальное число границы
    stop = 101  # максимальное число границы
    
    while True:
        y = (start + stop)//2 #сокращаем область поиска числа, от 1 до 50 и от 50 до 100
        count += 1
        if y == number:
            break  # выход из цикла если угадали (радуемся)
        elif number > y:
            start = y  # если загаданное число больше, то берем числа больше 50
        else:
            stop = y # если меньше, то берем числа меньше 50

    return count

print(f'Количество попыток: {random_predict()}')
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)