import random
import lootTables
import loot.current as current
import base
import sys

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
        try:
            print("Dodge = " + str(loot.dodge))
        except NameError:
            pass
        try:
            print("Incremental damage = " + str(loot.incDamage))
        except NameError:
            pass
        try:
            print("Damage = " +str(loot.damage))
        except NameError:
            pass
    elif loot.type == "health":
        print("Increases health by " + str(loot.boost))

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
        try:
            current.amulet.dodge = loot.dodge
        except NameError:
            current.amulet.dodge = 0
        try:
            current.amulet.incDamage = loot.incDamage
        except NameError:
            current.amulet.incDamage = 0
        try:
            current.amulet.damage = loot.damage
        except NameError:
            current.amulet.damage = 0
    elif loot.type == "health":
        current.health += loot.boost
        base.health += loot.boost
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
    print("Max health: " + str(base.health))
    print("Health: " + str(current.health))

def lootAsk(loot):
    equip = "N/A"
    while equip.lower() != "n" and equip.lower() != "y":
        equip = input("Would you like to equip this item? (y/n) ")

        if equip.lower() == "y":
            lootEquip(loot)

        elif equip.lower() == "n":
            print("You have chosen not to equip this item. \n")
        else:
            print("Please use \'y\' for yes and \'n\' for no. \n")

def enemyAttack(enemy):
    global current

    damage = enemy.damage - current.defence
    current.health -= damage
    if current.health <= 0:
        return "loss"
    else:
        return "N/A"

def playerAttack(enemy):
    global current

    if current.weapon.piercing == True:
        damage = (current.strength - (enemy.defence / 2))
    else:
        damage = (current.strength - enemy.defence)
    
    if enemy.health <= 0:
        return "victory"
    else:
        return "N/A"
    

def chestRoom():
    action = "N/A"
    while action.lower() != "a" and action.lower() != "b":
        action = input("You have reached a chest room. What would you like to do? \n A. Open the chest. \n B. Go to the next room. \n\n")
        print()

        if action.lower() == "a":
            loot = chest()

            lootScan(loot)
            lootAsk(loot)

            print()

        elif action.lower() == "b":
            break

        else:
            print("Please select either \'A\' or \'B\'.")


def getroom():
    roomSelect = random.randint(1, 100)

    if roomSelect >= 1 and roomSelect <= 100:
        chestRoom()