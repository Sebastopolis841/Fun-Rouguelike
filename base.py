def statsBase():
    while goodStats == False:
        global strength
        global luck
        global defence
        global dodge
        global accuracy

        goodStats = False
        keepStats = "N/A"
        statPoints = 10
        strength = 1
        luck = 1
        defence = 1
        dodge = 1
        accuracy = 1

        print("You have 15 stat points to spend.")
        print("These can be put into 4 attributes: Strength, Luck, Defence, Dodge and Accuracy")
        print("Each stat starts with one stat point, so you have 10 left to use.")

        print()

        strengthAdd = int(input("You have 10 points left. How many points to put into strength: "))
        strength += strengthAdd
        statPoints -= strengthAdd

        luckAdd = int(input("You have " + str(statPoints) + " points left. How many points to put into luck: "))
        luck += luckAdd
        statPoints -= luckAdd

        defenceAdd = int(input("You have " + str(statPoints) + " points left. How many points to put into defence: "))
        defence += defenceAdd
        statPoints -= defenceAdd

        dodgeAdd = int(input("You have " + str(statPoints) + " points left. How many points to put into dodge: "))
        dodge += dodgeAdd
        statPoints -= dodgeAdd

        accuracyAdd = int(input("You have " + str(statPoints) + " points left. How many points to put into accuracy: "))
        accuracy += accuracyAdd
        statPoints -= accuracyAdd

        if strengthAdd < 0 or luckAdd < 0 or defenceAdd < 0 or dodgeAdd < 0:
            print("A negative value(s) has been detected. Please input valid stats.")

        elif statPoints == 0:
            print("You have chosen the stats: \n \n Strength = " + str(strength) + "\n Luck = " + str(luck) + "\n Defence = " + str(defence) + "\n Dodge " + str(dodge) + "\n Accuracy " + str(accuracy) + "\n")

            while keepStats == "N/A":

                keepStats = input("Keep stats? (y/n): ")

                if keepStats == "y":
                    goodStats = True
            
                    print("Your stats have been selected.")
                
                    luck -= 1
                    dodge *= 5
                    accuracy *=3

                elif keepStats == "n":
                    print("Please select new stats: \n")
        
                else:
                    keepStats = "N/A"
                    print("You have not selected a valid value. please use \'y\' for \'yes\' and \'n\' for \'no\'. \n")

        else:
            print("Your stat points have been improperly distributed. Please redistribute stats.")