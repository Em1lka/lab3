import time
import re

try:
    filePath = input('Введите путь к файлу: ') # Получаем путь к файлу.
    numWords = int(input('Введите требуемое количество слов: ')) # Получаем требуемое количество слов в предложении.
    with open(filePath, 'r', encoding='utf8') as file: # Безопасно открываем файл.
        print("Результат работы программы:")
        separators = ['.', '!', '?'] # Разделители текста на предложения.
        punctuationFlag = False # Флаг для отслеживания наличия знаков пунктуации в текстовом документе.
        text = file.read() # Чтение файла.
        if text == '': # Проверка файла на наличие символов.
            print('Файл является пустым!')
            print("Время выполнения: " + str(time.process_time()))
        for el in separators:
            if (text.find(el) != -1):
                punctuationFlag = True
                break
        if (punctuationFlag == False): # Проверка на содержание в тексте знаков препинания.
            if (len(text.split()) == numWords): # Проверка совпадения количества слов с требуемым количеством.
                print(text)
                print("Время выполнения: " + str(time.process_time()))
            else: # Если не совпадает, тогда выводим ошибку.
                print("Файл не содержит знаков препинания, предполагающих конец предложения!")
                print("Время выполнения: " + str(time.process_time()))
        else:
            sentences = re.split('([.|!|?])', text) # Получение списка предложений и разделителей.
            sentences2 = [] # Создание отдельного списка.
            for i in range(1, len(sentences), 2): # Прохождение списка 'sentences' для заполнения 'sentences2'.
                sentences2.append(sentences[i - 1].strip() + sentences[i].strip()) # Заполнение списка 'sentences2'.
            for el in sentences2: # Прохождение списка 'sentences' для проверки на совпадение количества слов.
                if (len(el.split()) == numWords): # Проверка совпадения количества слов с требуемым количеством.
                    print(el)
            print("Время выполнения: " + str(time.process_time()))
# Исключения
except FileNotFoundError: # Файл не обнаружен.
    print("Файл *.txt в директории проекта не обнаружен.")
    print("Время выполнения: " + str(time.process_time()))
except ValueError(): # Параметр 'numWords' некорректен.
    print("Вы ввели некорректное число.")
    print("Время выполнения: " + str(time.process_time()))
