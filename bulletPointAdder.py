##! python3
# bulletPointAdder.py - Добавляет маркеры в Википедии в начало
# каждой строки текста, скопированного в буфер обмена.

import sys, pyperclip

text = pyperclip.paste()  # Копирует текст из буфера обмена

# TODO: разделить строки и добавить звездочки.
lines = text.split("\n")  # Разделяет текст на строки по разделителю
for i in range(len(lines)):
    lines[i] = "* " + lines[i]  # Добавляет в каждую строку * и пробел
    print(lines[i])

text = "\n".join(lines)  # Собирает все строки из списка с разделителем в одну
pyperclip.copy(text)  # Копирует получившуюся строку в буфер обмена
