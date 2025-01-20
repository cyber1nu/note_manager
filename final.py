note = []

username = input('Введите имя пользователя: ')
content = input('Введите описание задачи: ')
status = False # мы же еще не приступили к выполнению задачи, пока будет False
created_date = input('Введите дату старта задачи в формате "ДД-ММ-ГГГГ" :')
issue_date = input('Введите дату окончания задачи в формате "ДД-ММ-ГГГГ" :')
title_one = input('Введите название заголовка 1: ')
title_two = input('Введите название заголовка 2: ')
title_three = input('Введите название заголовка 3: ')


note.extend([username, content, status, created_date, issue_date, [title_one, title_two, title_three]])

print(note)

note_dict = {
    'username': username,
    'content': content,
    'status': status,
    'created_date' : created_date,
    'issue_date': issue_date,
    'titles': [title_one, title_two, title_three],
}

for key, value in note_dict.items():
    if isinstance(value, list):
        print(f'{key}: {value[0]}, {value[1]}, {value[2]}')
    else:
        print(f'{key}:', value)
