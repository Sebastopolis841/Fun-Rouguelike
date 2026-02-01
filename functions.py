import random

def loot(lootTable, lootExtraSpace, luck, luckModifier):
    return lootTable[((random.randint(0, (len(lootTable) - lootExtraSpace))) + (luck * luckModifier))]