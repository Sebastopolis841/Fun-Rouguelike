import loot.chest as chest
import loot.skeleton as skeleton
import loot.stoneGolem as stoneGolem
import loot.library as library

class chestLoot:
    lootTable = [
            chest.rocks,
            chest.coal,
            chest.oldBoots,
            chest.glassShard,
            chest.oldHelmet,
            chest.flintShard,
            chest.catHeadband,
            chest.eliShoe,
            chest.pufferJacket,
            chest.brassKnuckles,
            chest.jeans,
            chest.amuletOfAgility,
            chest.fancyBoots,
            chest.bigRedBoots,
            chest.sneakers,
            chest.rustySword,
            chest.healthCrystal,
            chest.chainmailHelmet,
            chest.chainmailPants,
            chest.chainmailChestplate,
            chest.duelSteelDaggers,
            chest.amuletOfFire,
            chest.spikedBoots,
            chest.ironHelmet,
            chest.ironChestplate,
            chest.ironPants,
            chest.blowgun,
            chest.flamingStaff,
            chest.amuletOfTheFlamingStep
        ]
    
    extraSpace = 7

    luckModifier = 0.7

class skeletonLoot:
    lootTable = [
        skeleton.boneClub,
        skeleton.skull,
        skeleton.ribcage,
        skeleton.ribDagger,
        skeleton.bowAndArrow,
        skeleton.gildedHelmet,
        skeleton.cursedDagger,
        skeleton.amuletOfNecromancy,
        skeleton.staffOfTheUndead
    ]

    extraSpace = 3

    luckModifier = 0.3

class stoneGolemLoot:
    lootTable = [
        chest.rocks,
        stoneGolem.midStone,
        stoneGolem.stoneBlade,
        stoneGolem.boulder,
        stoneGolem.eyeOfTheGolem,
        stoneGolem.stoneWroughtHelmet,
        stoneGolem.stoneWroughtBoots,
        stoneGolem.stoneWroughtPants,
        stoneGolem.stoneWroughtChestplate
        ]
    
    extraSpace = 2

    luckModifier = 0.2

class libraryLoot:
    lootTable = [
        library.windTome,
        library.fisticuffsManual,
        library.fireTome,
        library.iceTome,
        library.rejuvinationManual,
        library.magicMissileTome,
        library.necromancyTome,
        library.healingTome,
        library.tomeOfTheShiftingTide,
        library.tomeOfTheDeepestUnderworld
    ]

    extraSpace = 3

    luckModifier  = 0.3