from datetime import datetime


def add_note(some_list) -> None:
    """
    Ничего не возвращает, просто создает заметку в виде словаря и кладет ее в список для хранения

    Аргумент:
        some_list (list): список, куда мы кладем заметку в виде словаря

    """
    title = input('Введите название задачи: ')
    content = input('Введите описание/содержание задачи: ')
    status = input('Введите статус задачи (например, "новая", "в процессе", "отложено": ')
    created_date = datetime.now().strftime('%d-%m-%Y')
    issue_date = input('Введите дату окончания задачи в формате "ДД-ММ-ГГГГ" :')
    some_list.append(
        {
            'title': title,
            'content': content,
            'status': status,
            'created_date': created_date,
            'issue_date': issue_date
        }
    )

notes_list = []

while True:
    answer = input('Вы хотите добавить заметку? (введите "стоп", если нет): ')
    if answer == 'стоп':
        break
    else:
        add_note(notes_list)

print('Список заметок: \n')
for note in notes_list:
    print(f'Заметка: {note["title"]}; Содержание: {note["content"]}; '
          f'Статус: {note["status"]}; Срок выполнения - до {note["issue_date"]}.')
