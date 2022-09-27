# Новое приложение
import os, sys, math
from random import *

MyList = [2, 56, 89, 85, 456, 59]
for a in MyList:
    print("строка = " + str(a))

# Т.е. теперь я могу спокойно кодить на питоне и наверное добавлять новые скрипты в Dynamo
# А это проверка добавления изменений в Git
print("")
# print("Введитете новое число - количество строк")
# numbers = input()
# print("Напечатать " + numbers + " строк? y/n")
# yn = input()
# if str(yn) == "y":
#     for number in range(int(numbers)):
#         print(MyList)
# print("Готово!")
# print("")
# print("Десять случайных чисел в диапазоне от 1 до 100")
# for i in range(1, 10):
#     print(randint(1, 100))

listForPrint = ["И", "вновь", "продолжается", "бой"]
for word in listForPrint:
    print(word + ", ", end="")
print("")

grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]
print()
for n in range(0, len(grid[0])):
    for i in range(0, len(grid)):
        print(grid[i][n], end="")
    print()
print()

# Словари
newDict = {"номер": 1, "Площадь": 6, "Ед.Изм.": "кв.м"}
for k, v in newDict.items():
    print(str(k) + " - " + str(v))
