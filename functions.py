import random
import lootTables
import loot.current as current
import base
import enemies
import sys

def loot(lootTable, lootExtraSpace, luck, luckModifier):
    try:
        return lootTable[((random.randint(0, (len(lootTable) - lootExtraSpace))) + int(luck * luckModifier))]
    except IndexError:
        return lootTable[-1]

def chest():
    return loot(lootTables.chestLoot.lootTable, lootTables.chestLoot.extraSpace, current.luck, lootTables.chestLoot.luckModifier)

def skeleton():
    return loot(lootTables.skeletonLoot.lootTable, lootTables.skeletonLoot.extraSpace, current.luck, lootTables.skeletonLoot.luckModifier)

def stoneGolem():
    return loot(lootTables.stoneGolemLoot.lootTable, lootTables.stoneGolemLoot.extraSpace, current.luck, lootTables.stoneGolemLoot.luckModifier)

def library():
    return loot(lootTables.libraryLoot.lootTable, lootTables.libraryLoot.extraSpace, current.luck, lootTables.libraryLoot.luckModifier)

def healthBoost(loot):
    return loot.boost * current.defence

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
        except AttributeError:
            pass
        try:
            print("Incremental damage = " + str(loot.incDamage))
        except AttributeError:
            pass
        try:
            print("Damage = " +str(loot.damage))
        except AttributeError:
            pass
    elif loot.type == "health":
        print("Increases health by " + str(healthBoost(loot)))

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
        except AttributeError:
            current.amulet.dodge = 0
        try:
            current.amulet.incDamage = loot.incDamage
        except AttributeError:
            current.amulet.incDamage = 0
        try:
            current.amulet.damage = loot.damage
        except AttributeError:
            current.amulet.damage = 0
    elif loot.type == "health":
        boost = healthBoost(loot)
        current.health += boost
        base.health += boost
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

def lootRetrieve(loot):
    lootScan(loot)
    lootAsk(loot)

def enemyAttack():
    global current

    damage = current.enemy.damage - current.defence
    current.health -= damage

    if current.incDamaged == 0:
        current.incDamaged = current.enemy.incDamage
    
    print("You got hit for " + str(damage) + " damage \n New health: " + str(current.health))

    if current.health <= 0:
        return "loss"
    else:
        return "N/A"

def playerAttack():
    global current

    if current.piercing == True:
        damage = (current.strength - (current.enemy.defence / 2))
    else:
        damage = (current.strength - current.enemy.defence)

    current.enemy.health -= damage

    print("You hit the enemy for " + str(damage) + " damage!")

    if current.enemy.incDamaged == 0:
        current.enemy.incDamaged = current.incDamage

    if current.enemy.health <= 0:
        return "victory"
    else:
        return "N/A"

def incDamage(target):
    target.health -= target.incDamaged

    target.incDamaged = int(target.incDamaged / 2)

def rest():
    global current

    current.health += int(base.health * 0.15)
    if current.health > base.health:
        current.health = base.health
    
    print("Successfully healed. \n New health: " + str(current.health))

def regen():
    global base

    base.health += int(current.defence/2)

def flee():
    chance = random.randint(1,10)
    if chance <= current.dodge:
        return "escape"

def encounter():
    global current
    result = "N/A"

    while True:
        action = "N/A"

        action = input("Choose an action. \n A. Attack. \n B. Rest. \n C. Flee. \n\n")

        if action.lower() == "a":
            result = playerAttack()
            if result == "victory":
                print("You won the encounter!")
                regen()
                return "victory"
        elif action.lower() == "b":
            rest()
        elif action.lower() == "c":
            result = flee()
            if result == "escape":
                regen()
                return "escape"
        else:
            print("Please select either \'A\', \'B\', or \'C\'")
        
        result = enemyAttack()
        if result == "loss":
            print("You lost. ):")
            sys.exit()

        incDamage(current.enemy)
        incDamage(current)

def skeletonRoom():
    global current
    
    current.enemy = enemies.skeleton

    print("You entered a room with a skeleton in it.")

    result = encounter()

    if result == "victory":
        print("You got some loot! \n")
        loot = skeleton()
        lootRetrieve(loot)
    else:
        print("You managed to escape the room! You were unfortunately unable to retrieve any loot.")

def stoneGolemRoom():
    global current

    current.enemy = enemies.stoneGolem

    print("You entered a room with a stone golem in it.")

    result = encounter()

    if result == "victory":
        print("You got some loot! \n")
        loot = stoneGolem()
        lootRetrieve(loot)
    else:
        print("You managed to escape the room! You were unfortunately unable to retrieve any loot.")

def chestRoom():
    action = "N/A"
    while action.lower() != "a" and action.lower() != "b":
        action = input("You have reached a chest room. What would you like to do? \n A. Open the chest. \n B. Go to the next room. \n\n")
        print()

        if action.lower() == "a":
            loot = chest()
            lootRetrieve(loot)

            print()

        elif action.lower() == "b":
            break

        else:
            print("Please select either \'A\' or \'B\'.")

def libraryRoom():
    action = "N/A"
    while action.lower() != "a" and action.lower() != "b":
        action = input("You have reached a library. What would you like to do? \n A. Peruse the books \n B. Go to the next room. \n\n")
        print()

        if action.lower() == "a":
            loot = chest()
            lootRetrieve(loot)

            print()

        elif action.lower() == "b":
            break

        else:
            print("Please select either \'A\' or \'B\'.")


def getroom():
    roomSelect = random.randint(1, 100)

    if roomSelect >= 1 and roomSelect <= 25:
        chestRoom()
    elif roomSelect >=26 and roomSelect <= 20:
        skeletonRoom()
    elif roomSelect >= 51 and roomSelect <= 75:
        stoneGolemRoom()
    elif roomSelect >= 76 and roomSelect <= 100:
        libraryRoom()