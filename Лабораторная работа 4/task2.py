# TODO импортировать необходимые молули


import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json" #Имена входного и выходного файлов

def task() -> None: #Читает CSV-файл и преобразует его в JSON с отступами, все значения остаются строками
    with open(INPUT_FILENAME) as file: #Открываем CSV на чтение
        stroki = [i for i in csv.DictReader(file)] #Преобразуем в список словарей
    with open(OUTPUT_FILENAME, "w") as file: #Перезаписываем JSON
        json.dump(stroki, file, indent=4)#Записываем список словарей в JSON с отступом 4 пробела

if __name__ == '__main__': #Выполняем основное преобразование CSV -> JSON
    task()
    with open(OUTPUT_FILENAME) as file:
        for i in file:
            print(i, end="")# Выводим содержимое полученного JSON-файла в консоль без лишнего перевода строки