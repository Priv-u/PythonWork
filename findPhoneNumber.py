import re

message = "Мой телефонный номер +7-(777)-782-3083"
phoneNumberRegex = re.compile(r"(\+\d-\(\d{3}\))?\d{3}-\d{4}")
mo = phoneNumberRegex.search(message)
try:
    print("Найден телефонный номер: " + mo.group())
except:
    print("Ни один номер не найден")
