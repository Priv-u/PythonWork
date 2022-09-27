tableData = [
    ["гвозди", "шурупы", "болты", "гайки", "шпильки"],
    ["яблоки", "груши-ягоды", "сливы", "виноградины", "маракуйя"],
    ["собаки", "кошки", "зяблики", "канарейки", "попугайчики"],
    ["Акулы", "Касатки", "Синие киты", "Караси", "Щуки"],
]


def tablePrint(listForTable):
    colWidths = [0] * len(listForTable)
    for i in range(len(listForTable)):
        colWidths[i] = len(max(listForTable[i], key=len))
    maxLen = max(colWidths)
    print()
    for i in range(len(listForTable)):
        for j in range(len(listForTable[i])):
            print(
                listForTable[i][j], end=" ".rjust(maxLen + 2 - len(listForTable[i][j]))
            )
        print()


tablePrint(tableData)
tablePrint(tableData)
tablePrint(tableData)
print()
