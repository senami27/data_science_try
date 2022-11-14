""""Игра угадай число
Компьютер сам загадывает и сам угадывает"""

import numpy as np

def random_predict(number:int=1) -> int:
    """"Рандомно угадываем число
    
    Args:
        number (int, optional): Загаданное число. Default to 1.
    
    Returns:
        int: Число попыток
    """
    count = 0
    min = 1
    max = 100
    
    while True:
        count += 1
        mid = round((min+max) / 2)
        predict_number = np.random.randint(min,max)
        #print(number,predict_number,mid)
        if number == predict_number:
            break
        elif mid > number:
            max = mid
        else:
            min = mid
    return(count)

#print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """Среднее количество попыток за 1000 подходов для угадывания

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        Среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 100, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == "__main__":
    #RUN
    score_game(random_predict)
