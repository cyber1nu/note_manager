titles_list = []    # инициализация списка
count = 1           # для красивого вывода нумерации заголовков

while True:         # запуск бесконечного цикла (пока TRUE)
    title = input('Введите заголовок заметки (или оставьте поле ввода пустым, нажав Enter): ')  # ввод
    if title == '':                                                                             # если пусто - выход
        break
    if title not in titles_list:                                                                # проверка на уникальность
        titles_list.append(title)
    else:
        print('Такой заголовок уже был!')


titles_tuple = tuple(titles_list)   # переводим список в кортеж

for ttl in titles_tuple:            # вывод на печать заголовков по очереди
    print(f'Заголовок №{count}: ', ttl)
    count += 1

print('А вот и кортеж из заголовков: ', titles_tuple)
