def custom_write(file_name, strings):
    strings_positions = {}  # Словарь для хранения информации о строках
    file = open(file_name, 'w', encoding='utf-8')  # Открываем файл на запись с кодировкой utf-8
    line_number = 1  # Счётчик для отслеживания номера строки

    for string in strings:
        byte_position = file.tell()  # Получаем текущую позицию курсора в файле
        strings_positions[(line_number, byte_position)] = string  # Добавляем данные в словарь
        file.write(string + '\n')  # Записываем строку с переносом на новую строку
        line_number += 1  # Увеличиваем номер строки

    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)