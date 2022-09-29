#'''Находит телефонные номера и адреса
# электронной почты в буфере обмена '''

import email
import re, pyperclip

# Создает регулярное выражение для телефонного номера
# TODO Пересмотреть регулярное выражение
phoneRegex = re.compile(
    r"""(
        (\+\d{1,2} | \d{1,2})?           # Код страны
        (\s|-|.)?                        # Разрыв
        (\d{3}|\(\d{3}\))                # Код оператора
        (\s|-|.)?                        # Разрыв
        (\d{3})                          # Первые 3 цифры номера
        (\s|-|.)?                        # Разрыв
        (\d{4})                          # Оставшиеся 4 цифры номера
)""",
    re.VERBOSE,
)

# TODO Создать регулярное выражение для поиска электронной почты
eMailRegex = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+    # Имя пользователя
    @                    # Обязательный разделитель в адресе эл.почты
    [a-zA-Z0-9.-]+       # Имя домена эл.почты
    (\.[a-zA-Z]{2,5})    # Оставшаяся часть адреса после точки
) """,
    re.VERBOSE,
)


# TODO Найти соответствия в тексте из буфера обмена
text = str(pyperclip.paste())  # Копирует текст из буфера обмена

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = " ".join(
        [groups[1], groups[2], groups[3], groups[4], groups[5], groups[6], groups[7]]
    )
    # if groups[8] != "":
    #     phoneNum += "x " + groups[8]
    matches.append(phoneNum)

for groups in eMailRegex.findall(text):
    matches.append(groups[0])
try:
    print("Найдены телефонные номера и адреса электронной почты")
    # for i in range(len(matches)):
    #     print(matches[i])
    # TODO Скопировать результат в буфер обмена
    if len(matches) > 0:
        text = "\n".join(matches)
        pyperclip.copy(text)
        print(text)
        print("Скопировано в буфер обмена")
except:
    print("Ошибка обработки буфера обмена")
