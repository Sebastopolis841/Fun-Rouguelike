import current

weapon = "weapon"
boots = "boots"
helmet = "helmet"
pants = "pants"
chestplate = "chestplate"
amulet = "amulet"
health = "health"

class rocks:
    name = "rock"
    type = weapon
    damage = 2
    incDamage = 0
    piercing = False

class coal:
    name = "lump of coal"
    type = weapon
    damage = 1
    incDamage = 1
    piercing = False

class oldBoots:
    name = "old boots"
    type = boots
    defence = 1
    dodge = -1

class glassShard:
    name = "glass shard"
    type = weapon
    damage = 2
    incDamage = 0
    piercing = True

class oldHelmet:
    name = "old helmet"
    type = helmet
    defence = 1

class flintShard:
    name = "flint shard"
    type = "weapon"
    damage = 2
    incDamage = 1
    piercing = True

class catHeadband:
    name = "cat headband"
    type = helmet
    defence = 0

class eliShoe:
    name = "Uncle Eli\'s stinky shoe"
    type = weapon
    damage = 1
    incDamage = 3
    piercing = False

class pufferJacket:
    name = "puffer jacket"
    type = chestplate
    defence = 2
    thorns = 0

class brassKnuckles:
    name = "brass knuckles"
    type = weapon
    damage = 2
    incDamage = 0
    piercing = False

class jeans:
    name = "jeans"
    type = pants
    defence = 1

class amuletOfAgility:
    name = "amulet of agility"
    type = amulet
    dodge = 2

class fancyBoots:
    name = "fancy boots"
    type = boots
    defence = 2
    dodge = -1

class bigRedBoots:
    name = "big red boots"
    type = boots
    defence = 3
    dodge = -1

class sneakers:
    name = "sneakers"
    type = boots
    defence = 2
    dodge = 1

class rustySword:
    name = "rusty sword"
    type = weapon
    damage = 3
    incDamage = 0
    piercing = True

class healthCrystal:
    name = "health crystal"
    type = health
    boost = int(current.defence * 1.5)

class chainmailHelmet:
    name = "chainmail helmet"
    type = helmet
    defence = 2

class chainmailPants:
    name = "chainmail pants"
    type = pants
    defence = 3

class chainmailChestplate:
    name = "chainmail chestplate"
    type = chestplate
    defence = 4
    thorns = 0

class duelSteelDaggers:
    name = "duel steel daggers"
    type = weapon
    damage = 4
    incDamage = 0
    piercing = True

class amuletOfFire:
    name = "amulet of fire"
    type = amulet
    incDamage = 3

class spikedBoots:
    name = "spiked boots"
    type = boots
    defence = 3
    dodge = 2

class ironHelmet:
    name = "iron helmet"
    type = helmet
    defence = 3

class ironChestplate:
    name = "iron chestplate"
    type = chestplate
    defence = 6
    thorns = 0

class ironPants:
    name = "iron pants"
    type = pants
    defence = 4

class blowgun:
    name = "blowgun"
    type = weapon
    damage = 1
    incDamage = 4
    piercing = True

class flamingStaff:
    name = "flaming staff"
    type = weapon
    damage = 3
    incDamage = 4
    piercing = False

class amuletOfTheFlamingStep:
    name = "amulet of the flaming step"
    type = amulet
    dodge = 2
    incDamage = 3