import time
import string


def words_from_digits(filename):  # ФУНКЦИЯ ДЛЯ РАЗДЕЛЕНИЯ СЛОВ И ЦИФР
    text = open(filename, encoding='utf-8').read().split()  # открываем файл в режиме чтения и разбиваем на массив по пробелам
    text_to_extract = ' '.join(text)  # создаем переменную на выход из функции и собираем текст назад в строку для дальнейшей записи в файл
    text = [word.strip(string.punctuation) for word in text]  # убираем пунктуацию
    words = [word for word in text if word[0] in string.ascii_letters]  # отбираем слова  в массив
    digits_in_func = [int(digit) for digit in text if digit[0] in string.digits]  # отбираем цифры в массив
    len_for_words_in_func = [len(word) for word in words]  # создаём массив с длинами всех слов
    return len_for_words_in_func, digits_in_func, text_to_extract  # возвращаем из функции массив с длинами слов, массив цифр и исходный текст


def sorter(array):  # ФУНКЦИИ ДЛЯ СОРТИРОВКИ СЛИЯНИЕМ
    length = len(array)  # переменная для проверки длины
    if length < 2:   # если длина массива меньше двух, значит там один элемент, его и возвращаем
        return array
    left = sorter(array[:length // 2:])  # дробим массив от начала до половины его длины и передаём в функцию
    right = sorter(array[length // 2:])  # дробим массив от половины его длины до конца и передаём в функцию
    return merger(left, right)  # вызываем функцию merger для сортировки и слияния


def merger(left, right):
    result = []  # пустой массив для результата
    while len(left) > 0 and len(right) > 0:  # пока в обеих частях есть элементы
        if left[0] >= right[0]:  # если левый элемент больше либо равен правому, добавляем левый в результат и удаляем его из исходника
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])  # если правый элемент больше левого, добавляем правый в результат и удаляем его из исходника
            del right[0]
    if len(left) == 0:  # добавляем в результат оставшуюся непустую последовательность
        result += right
    if len(right) == 0:
        result += left
    return result  # возвращаем массив result


def writer(len_for_words, digits, text, time):  # ФУНКЦИЯ ДЛЯ ЗАПИСИ РЕЗУЛЬТАТА В ФАЙЛЫ
    separated_temp = ''  # временная переменная для элементов сортировки
    result = open('A:\\учеба\\для практики\\result.txt', 'w')  # открываем/создаем файл и переписываем его содержимое
    set_of_words = sorted(set(len_for_words), reverse=True)  # удаляем повторяющиеся элементы
    print(set_of_words)
    result.write('Длины слов:\n')  # для наглядности пишем пояснение в файл
    for each in set_of_words:  # идём по каждому уникальному элементу
        amount = len_for_words.count(each)  # считаем количество этого элемента в исходном массиве длин
        for i in range(amount):
            separated_temp += str(each) + ' '
        separated_temp += '\n'
        result.write(separated_temp)   # через пробел записываем в файл нужное количество элементов этого типа
        separated_temp = ''   # обновляем переменную
    set_of_digits = sorted(set(digits), reverse=True)   # проделываем то же самое с массивом цифр
    print(set_of_digits)
    result.write('Дальше идут числа:\n')
    for each in set_of_digits:
        amount = digits.count(each)
        for i in range(amount):
            separated_temp += str(each) + ' '
        separated_temp += '\n'
        result.write(separated_temp)
        separated_temp = ''
    analysis = open('A:\\учеба\\для практики\\analysis.txt', 'w', encoding='utf-8')   # открыли файл для записи анализа
    analysis.write('Введённый текст:\n' + text + '\n')   # вставляем исходный текст
    analysis.write(f"""
Вариант 18: латиница, по количеству символов в слове, по убыванию, учитывать числа, сортировка слиянием.
Количество слов: {len(len_for_words)}
Время сортировки: {time} сек
Статистика (количество слов каждой длины, числа после них):\n""")   # форматируемая строка, будет вставлять нужные значения под каждый конкретный случай
    for each in set_of_words:   # записываем уникальные элементы и их количество
        amount = len_for_words.count(each)
        analysis.write(f'{each} - {amount}\n')
    for each in set_of_digits:
        amount = digits.count(each)
        analysis.write(f'{each} - {amount}\n')


name = input('Введите абсолютный путь к файлу: ')
start_time = time.time()   # начало отсчёта времени
len_for_words, digits, text = words_from_digits(f'{name}.txt')   # открытие исходного файла и первый этап сортировки
len_for_words = sorter(len_for_words)   # сортировка слиянием для слов
digits = sorter(digits)   # сортировка слиянием для цифр
end_time = round((time.time() - start_time), 5)  # конец отсчёта времени сортировки
writer(len_for_words, digits, text, end_time)  # запись результата в файлы

