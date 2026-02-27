import random
import lootTables
import loot.current as current
import base
import enemies
import sys

def goodbye():
    print("\n\n Goodbye!")
    sys.exit()

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

def friend():
    return lootTables.friends[random.randint(0,(len(lootTables.friends) - 1))]

def healthBoost(loot):
    return int(loot.boost * current.defence)

def lootScan(loot):
    print(loot.name)
    print(loot.type)
    if loot.type == "weapon":
        print("Damage = " + str(int(loot.damage * current.difficulty)))
        print("Incremental damage = " + str(int(loot.incDamage * current.difficulty)))
        print("Piercing = " + str(int(loot.piercing * current.difficulty)))

    elif loot.type == "boots":
        print("Defence = " + str(int(loot.defence * current.difficulty)))
        print("Dodge = " + str(int(loot.dodge * current.difficulty)))

    elif loot.type == "pants" or loot.type == "helmet":
        print("Defence = " + str(int(loot.defence * current.difficulty)))

    elif loot.type == "chestplate":
        print("Defence = " + str(int(loot.defence * current.difficulty)))
        print("Thorns = " + str(int(loot.thorns * current.difficulty)))

    elif loot.type == "amulet":
        try:
            print("Dodge = " + str(int(loot.dodge * current.difficulty)))
        except AttributeError:
            pass

        try:
            print("Incremental damage = " + str(int(loot.incDamage * current.difficulty)))
        except AttributeError:
            pass

        try:
            print("Damage = " +str(int(loot.damage * current.difficulty)))
        except AttributeError:
            pass

    elif loot.type == "health":
        print("Increases health by " + str(int(healthBoost(loot) * current.difficulty)))

def friendScan(friend):
    global current

    print("You found a " + str(friend.name) + "! \n")
    print("Strength: " + str(friend.strength))
    print("Health: " + str(friend.maxHealth))
    print("Accuracy: " + str(friend.accuracy))
    print("Dodge: " + str(friend.dodge))

def friendEquip(friend):
    current.friend = friend

    current.friend.name = input("What would you like to name this " + friend.name "? ") 

    print("\nSuccessfully befriended " + friend.name + "!\n")

def lootEquip(loot):
    global current
    global base

    if loot.type == "weapon":
        current.weapon.damage = int(loot.damage * current.difficulty)
        current.weapon.incDamage = int(loot.damage * current.difficulty)
        current.weapon.piercing = int(loot.piercing * current.difficulty)

    elif loot.type == "boots":
        current.boots.defence = int(loot.defence * current.difficulty)
        current.boots.dodge = int(loot.dodge * current.difficulty)

    elif loot.type == "pants":
        current.pants.defence = int(loot.defence * current.difficulty)

    elif loot.type == "helmet":
        current.helmet.defence = int(loot.defence * current.difficulty)

    elif loot.type == "chestplate":
        current.chestplate.defence = int(loot.defence * current.difficulty)
        current.chestplate.thorns = int(loot.thorns * current.difficulty)

    elif loot.type == "amulet":
        try:
            current.amulet.dodge = int(loot.dodge * current.difficulty)

        except AttributeError:
            current.amulet.dodge = 0

        try:
            current.amulet.incDamage = int(loot.incDamage * current.difficulty)

        except AttributeError:
            current.amulet.incDamage = 0

        try:
            current.amulet.damage = int(loot.damage * current.difficulty)

        except AttributeError:
            current.amulet.damage = 0

    elif loot.type == "health":
        boost = int(healthBoost(loot) * current.difficulty)
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

def friendAsk(friend):
    equip = "N/A"
    while equip.lower() != "n" and equip.lower() != "y":
        equip = input("Would you like to befriend this character? (You may only have 1 friend at a time) (y/n) ")

        if equip.lower() == "y":
            friendEquip(friend)

        elif equip.lower() == "n":
            print("You have chosen not to befriend this character. \n")

        else:
            print("Please use \'y\' for yes and \'n\' for no. \n")

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

def friendSet(friend):
    friendScan(friend)
    friendAsk(friend)

def lootRetrieve(loot):
    lootScan(loot)
    lootAsk(loot)

def randomizer(stat):
    randomizerLow = stat / 2
    randomizerHigh = stat * 2
    
    tempstat = random.randint(int(randomizerLow), randomizerHigh)

    return tempstat

def dodge(accuracy,dodge):
    if randomizer(dodge) > randomizer(accuracy):
        return True
    
    else:
        return False

def playerAttack():
    global current

    tempStrength = randomizer(current.strength)

    if current.piercing == True or tempStrength == (current.strength * 2):
        damage = int(tempStrength - (current.enemy.defence / 2))

    else:
        damage = int(tempStrength - current.enemy.defence)
    
    if damage <= 0:
        damage = 1

    if dodge(current.accuracy,current.enemy.dodge) == True:
        print("The enemy dodged and took 0 damage")
        return "N/A"
    
    else:
        current.enemy.health -= damage

        if tempStrength == (current.strength * 2):
            print("You scored a critical hit against the enemy and dealt " + str(damage) + " damage!")

        else:
            print("You hit the enemy for " + str(damage) + " damage!")

        if current.enemy.incDamaged == 0:
            current.enemy.incDamaged = randomizer(current.incDamage)

        if current.enemy.health <= 0:
            return "victory"
        
        else:
            return "N/A"


def enemyAttack(counter):
    global current

    tempDodge = current.dodge
    target = random.randint(1,2)

    if target == 1 or current.friend.alive == False:
        damage = int(current.enemy.damage - current.defence)

        if damage <= 0:
            damage = 1
    
        if counter == True:
            current.dodge = int(current.dodge * 1.5)

        if dodge(current.enemy.accuracy,current.dodge) == True:
            print("You dodged the enemy's attack and took 0 damage!")

            if counter == True:
                return playerAttack()
        
            return "N/A"
    
        else:
            current.health -= damage

            if current.incDamaged == 0:
                current.incDamaged = randomizer(int(current.enemy.incDamage * current.difficulty))
    
            print("You got hit for " + str(damage) + " damage \n New health: " + str(current.health))

            current.dodge = tempDodge

            if current.health <= 0:
                return "loss"
            else:
                return "N/A"
            
    elif target == 2 and current.friend.alive == True:
        damage = int(current.enemy.damage / 2)
        name = current.friend.name

        if damage <= 0:
            damage = 1
        
        if counter == True:
            print("\nYou attempted a counterattack, but the enemy attacked " + name + " instead.")

        if dodge(current.enemy.accuracy,current.friend.dodge) == True:
            print(name + " dodged the enemy's attack and took 0 damage.")
            
            return "N/A"
        
        else:
            current.friend.health -= damage

            print(name + " got hit for " + str(damage) + " damage \n New Health: " + str(current.friend.health))

            if current.friend.health <= 0:
                return "friendLoss"
            else:
                return "N/A"


def friendAttack():
    global current

    name = current.friend.name
    damage = current.friend.strength

    if current.friend.alive == True:
        if dodge(current.friend.accuracy,current.enemy.dodge) == True:
            print("\nThe enemy dodged " + name + "\'s attack and took 0 damage.\n")
            return "N/A"

        else:
            current.enemy.health -= damage
            print()
            print(name + " hit the skeleton for " + str(damage) + " damage! \n")

            if current.enemy.health <= 0:
                return "victory"
        
            else:
                return "N/A"



def enemyIncDamage():
    current.enemy.health -= current.enemy.incDamaged

    print("The enemy took " + str(current.enemy.incDamaged) + " incremental damage.")

    current.enemy.incDamaged = int(current.enemy.incDamaged / 2)

    if current.enemy.health <= 0:
        return "victory"
    
    else:
        return "N/A"

def playerIncDamage():
    current.health -= current.incDamaged

    print("You took " + str(current.incDamaged) + " inmcremental damage.")

    current.incDamaged = int(current.incDamaged / 2)

    if current.health <= 0:
        return "loss"
    
    else:
        return "N/A"

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

def victory():
    global current

    print("You won the encounter!")
    regen()

    if current.friend.name != "N/A":
        current.friend.alive = True
        current.friend.health = current.friend.maxHealth

        print(current.friend.name + " was restored to full health!")

    return "victory"

def encounter():
    global current
    result = "N/A"

    while True:
        action = "N/A"
        help = True
        counter = False

        while help == True:
            action = input("\nChoose an action. Add -h to the end to get a help page. \n A. Attack. \n B. Rest. \n C. Flee. \n D. Counter \n\n")

            if action.lower() == "a":
                result = playerAttack()
                if result == "victory":
                    victory()
                
                help = False

            elif action.lower() == "a -h":
                print("\n Attack: Attacks the enemy. \n")

            elif action.lower() == "b":
                rest()
                help = False

            elif action.lower() == "b -h":
                print("\n Rest: Regenerates health.")

            elif action.lower() == "c":
                result = flee()
                if result == "escape":
                    regen()
                    return "escape"
                
                help = False

            elif action.lower() == "c -h":
                print("\n Flee: Makes an attempt to escape the encounter based off of dodge. \n")

            elif action.lower() == "d":
                result = "counter"
                counter = True
                help = False

            elif action.lower() == "d -h":
                print("\n Counter: Increases dodge for a turn. If you dodge successfully, then you get to counterattack. \n")

            else:
                print("Please select either \'A\', \'B\', or \'C\'")
        

        result = enemyAttack(counter)

        if result == "loss":
            print("You lost. ):")
            sys.exit()

        elif result == "victory":
                    victory()
        
        elif result == "friendLoss":
            print(current.friend.name + " was defeated. They will respawn next in the next room.")
        

        result = friendAttack()

        if result == "victory":
            victory()


        enemyIncDamage()
        playerIncDamage()

        counter = False
def summon(enemy):
    global current

    current.enemy = enemy
    current.enemy.damage *= int(current.difficulty)
    current.enemy.maxHealth *= int(current.difficulty)
    current.enemy.health *= int(current.difficulty)
    current.enemy.incDamage *= int(current.difficulty)
    current.enemy.accuracy *= int(current.difficulty)
    current.enemy.dodge *= int(current.difficulty)
    current.enemy.defence *= int(current.difficulty)

def cottage():
    action = "N/A"
    while action.lower() != "a" and action.lower() != "b":
        action = input("You entered a well-lit living space. What would you like to do? \n A. Look around. \n B. Leave. \n\n")
        print()

        if action.lower() == "a":
            NPC = friend()
            friendSet(NPC)

            print()

        elif action.lower() == "b":
            break

        else:
            print("Please select either \'A\' or \'B\'.")

def skeletonRoom():
    
    summon(enemies.skeleton)

    print("You entered a room with a skeleton in it.")

    result = encounter()

    if result == "victory":
        print("You got some loot! \n")
        loot = skeleton()
        lootRetrieve(loot)

    else:
        print("You managed to escape the room! You were unfortunately unable to retrieve any loot.")

def stoneGolemRoom():

    summon(enemies.stoneGolem)

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
            loot = library()
            lootRetrieve(loot)

            print()

        elif action.lower() == "b":
            break

        else:
            print("Please select either \'A\' or \'B\'.")


def getroom():
    global current
    print()
    print("You are on room " + str(current.room) + ".")
    current.room += 1
    current.difficulty += 0.1
    
    roomSelect = random.randint(1, 100)

    if current.room < 15:
        if roomSelect >= 1 and roomSelect <= 30:
            chestRoom()

        elif roomSelect >= 31 and roomSelect <= 60:
            skeletonRoom()
        
        elif roomSelect >= 61 and roomSelect <= 90:
            cottage()

        elif roomSelect >= 91 and roomSelect <= 95:
            stoneGolemRoom()

        elif roomSelect >= 96 and roomSelect <= 100:
            libraryRoom()


    elif current.room < 30:
        if roomSelect >= 1 and roomSelect <= 20:
            chestRoom()

        elif roomSelect >= 21 and roomSelect <= 40:
            skeletonRoom()
        
        elif roomSelect >= 41 and roomSelect <= 60:
            cottage()

        elif roomSelect >= 61 and roomSelect <= 80:
            stoneGolemRoom()

        elif roomSelect >= 81 and roomSelect <= 100:
            libraryRoom()


    else:
        if roomSelect >= 1 and roomSelect <= 10:
            chestRoom()

        elif roomSelect >= 11 and roomSelect <= 20:
            skeletonRoom()
        
        elif roomSelect >= 21 and roomSelect <= 30:
            cottage()

        elif roomSelect >= 31 and roomSelect <= 65:
            stoneGolemRoom()

        elif roomSelect >= 66 and roomSelect <= 100:
            libraryRoom()
