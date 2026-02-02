import random
import lootTables
import loot.current as current
import base

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

def lootEquip(loot):
    global current
    global base

    if loot.type == "weapon":
        current.weapon.damage = loot.damage
        current.weapon.incDamage = loot.damage
        current.weapon.piercing = loot.piercing
    elif loot.type == "boots":
        current.boots.defence = loot.defence
        current.boots.dodge = loot.dodge
    elif loot.type == "pants":
        current.pants.defence = loot.defence
    elif loot.type == "helmet":
        current.helmet.defence = loot.defence
    elif loot.type == "chestplate":
        current.chestplate.defence = loot.defence
        current.chestplate.thorns = loot.thorns
    elif loot.type == "amulet":
        current.amulet.dodge = loot.dodge
        current.amulet.incDamage = loot.incDamage
    else:
        print("There was an error loading your loot.")
    
    current.strength = (base.strength + current.weapon.damage)
    current.incDamage = (current.weapon.incDamage + current.amulet.incDamage)
    current.defence = (base.defence + current.boots.defence + current.pants.defence + current.helmet.defence + current.chestplate.defence)
    current.dodge = (base.dodge + current.boots.dodge + current.amulet.dodge)
    current.piercing = current.weapon.piercing
    current.thorns = current.chestplate.thorns

    print("\n Item successfully equipped. \n New stats: \n\n")

    print("Strength: " + str(current.strength))
    print("Incremental damage: " + str(current.incDamage))
    print("Defence: " + str(current.defence))
    print("Dodge: " + str(current.dodge))
    print("Piercing: " + str(current.piercing))
    print("Thorns: " + str(current.thorns))

def lootAsk(loot):
    equip = "N/A"
    while equip != "n" or equip != "y":
        equip = input("Would you like to equip this item? (y/n)")

        if equip == "y":
            lootEquip(loot)

        elif equip == "n":
            print("You have chosen not to equip this item. \n")
        else:
            print("Please use \'y\' for yes and \'n\' for no. \n")