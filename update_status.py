notes_collection = dict()
statuses = {'1': 'в процессе', '2': 'выполнено', '3': 'отложено'}
user_statuses = dict()


def add_own_status(note):
    status = input('Введите значение вашего собственного статуса: ')
    notes_collection[note] = status
    user_statuses.update({str(len(user_statuses) + 1): status})


def note_status_check(note):
    if note not in ['1', '2', '3', '4']:
        print('\nНеобходимо указать 1, 2, 3 или 4!\n')
        return False
    else:
        return True


print('Пока не было добавлено ни одной заметки.')

while True:
    for key, value in notes_collection.items():
        print(f'Название заметки: {key}, статус заметки: {value}')

    note_name = input('\nСтатус какой заметки вы хотите обновить сегодня? Введите название заметки'
                      '(Enter - завершение работы программы): ')

    if note_name not in notes_collection:
        if note_name == '':                 # для выхода из цикла
            break
        notes_collection[note_name] = statuses.get('1')
        print('\nТакой заметки раньше не было. Внесена в коллекцию, присвоено стандартное значение "в процессе".')
    else:
        note_status = input(f'\nВы выбрали заметку: {note_name} с текущим статусом: {notes_collection[note_name]}. '
                            f'Какой присваиваем статус? '
                            f'(1 - "в процессе", 2 - "выполненно", 3 - "отложено" или 4 - ваш собственный статус) ')

        if note_status_check(note_status) is False:
            continue

        if note_status == '4':
            add_own_status(note_name)
        else:
            notes_collection.update({note_name: statuses[note_status]})

        print(f'Успешно обновлен статус заметки: {note_name} на: {notes_collection[note_name]}\n')


print(user_statuses)    # печать нестандартных сохраненных заметок