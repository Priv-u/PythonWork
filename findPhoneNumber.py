import re

message = "Мой телефонный номер +7-(747)-878-5160, который я хочу проверить"
phoneNumberRegex = re.compile(
    r"""(\+\d-    # Код страны
\(\d{3}\))-       # Код оператора связи
\d{3}-\d{4}""",  # Телефонный номе абонента
    re.VERBOSE,
)
mo = phoneNumberRegex.search(message)
try:
    print("Найден телефонный номер: " + mo.group())
except:
    print("Ни один номер не найден")
