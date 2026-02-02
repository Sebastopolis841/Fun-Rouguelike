import random
import lootTables
import loot.current as current

def loot(lootTable, lootExtraSpace, luck, luckModifier):
    return lootTable[((random.randint(0, (len(lootTable) - lootExtraSpace))) + int(luck * luckModifier))]

def chest():
    return loot(lootTables.chestLoot.lootTable, lootTables.chestLoot.extraSpace, current.luck, lootTables.chestLoot.luckModifier)

def lootScan(loot):
    print(loot.name)
    print(loot.type)
    if loot.type == "weapon":
        print("Damage = " + str(loot.damage))
        print("Incremental damage = " + str(loot.incDamage))
        print("Piercing = " + str(loot.piercing))
    elif loot.type == "boots":
        print("Defence = " + str(loot.defence))
        print("Dodge = " + str(loot.dodge))
    elif loot.type == "pants" or loot.type == "helmet":
        print("Defence = " + str(loot.defence))
    elif loot.type == "chestplate":
        print("Defence = " + str(loot.defence))
        print("Thorns = " + str(loot.thorns))
    elif loot.type == "amulet":
        print("Dodge = " + str(loot.dodge))