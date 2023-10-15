
import os
import csv

# Путь к папке с файлами
folder_path = 'C:/work/Net/HackSoch/PiTrainCo/Датасет для easyOCR'

# Создайте или откройте CSV-файл для записи
csv_file_path = "output.csv"

# Открываем CSV-файл для записи
with open(csv_file_path, mode='w', newline='') as csv_file:
    # Определите заголовки для CSV-файла
    fieldnames = ['filename', 'text']

    # Создайте объект записи CSV
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Запишите заголовки в CSV-файл
    writer.writeheader()

    # Пройдем по файлам в папке
    for filename in os.listdir(folder_path):
        # Извлеките первые 8 символов из названия файла
        text = filename[:8]

        # Запишите данные в CSV-файл
        writer.writerow({'filename': filename, 'text': text})

print(f"CSV файл {csv_file_path} успешно создан.")