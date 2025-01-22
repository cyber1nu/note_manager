from datetime import datetime


def check_deadline(date: str) -> int:
    """
    Возвращает разницу между текущей и принимаемой датами

    Аргументы:
        date (string): дата в строковом виде, полученная от пользователя

    Возвращает:
        delta_days (int): целочисленная разница между датами (может быть отриц.)
        None: если дата не распознана, возвращает None
    """

    # Сначала было так, почитал, повспоминал, можно проще и красивее
    # while True:
    #     try:
    #         year, month, day = int(date[6:]), int(date[3:5]), int(date[:2])
    #         deadline = datetime(year, month, day)
    #         break
    #     except ValueError as e:
    #         print(f'Что-то не так с датой. Код ошибки: {e}. Попробуем по новой?')
    #         date = input('Пожалуйста, введите дату дедлайна (в формате ДД-ММ-ГГГГ): ')
    # стало так, как ниже

    date_formats = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d']

    for fmt in date_formats:
        try:
            deadline = datetime.strptime(date, fmt)
            delta_days = (datetime.now() - deadline).days
            return delta_days
        except ValueError as e:
            print(f'Обратите на формат даты. Код ошибки: {e}. Дата {date} не распознана')

    return None


current_day = datetime.now().strftime("%d-%m-%Y")
print(f'Сегодня у нас: {current_day}')

while True:
    issue_date = input('Пожалуйста, введите дату дедлайна (в формате ДД-ММ-ГГГГ): ')
    result = check_deadline(issue_date)
    if result is not None:
        if result > 0:
            print(f'До дедлайна остался(-лось) {result} день(дней)!')
        elif result == 0:
            print('Дедлайн сегодня!')
        else:
            print(f'Дедлайн просрочен на {result} день(дней)!')
        break
