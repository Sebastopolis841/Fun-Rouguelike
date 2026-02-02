import random
import lootTables
import loot.current as current

def loot(lootTable, lootExtraSpace, luck, luckModifier):
    return lootTable[((random.randint(0, (len(lootTable) - lootExtraSpace))) + (luck * luckModifier))]

def chest():
    return loot(lootTables.chestLoot.lootTable, lootTables.chestLoot.extraSpace, current.luck, lootTables.chestLoot.luckModifier)