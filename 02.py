def displayInventory(inventory):
    print("Снаряжение: ")
    total_item = 0
    for k, v in inventory.items():
        print(str(v) + " - " + k)
        total_item += v
    print("Общее количество предметов :" + str(total_item))


def addToInfentory(invent, loot):
    for a in loot:
        if a in invent.keys():
            invent[a] += 1


dragonLoot = [
    "gold coin",
    "gold coin",
    "rope",
    "torch",
    "gold coin",
    "torch",
    "gold coin",
    "rope",
    "gold coin",
    "rope",
    "gold coin",
]
inventory = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6, "dagger": 1}
addToInfentory(inventory, dragonLoot)

displayInventory(inventory)
