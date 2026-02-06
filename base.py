def statsBase():
    goodStats = False
    while goodStats == False:
        global strength
        global luck
        global defence
        global dodge
        global accuracy

        keepStats = "N/A"
        statPoints = 10
        strength = 1
        defence = 1
        dodge = 1
        accuracy = 1

        print()
        print()

        print("You have 14 stat points to spend.")
        print("These can be put into 5 attributes: Strength, Luck, Defence, Dodge and Accuracy \n")
        print("Each stat except for luck starts with one stat point, so you have 10 left to use.")

        print()

        while goodStats == False:
            try:
                strengthAdd = int(input("You have 10 points left. How many points to put into strength: "))
                strength += strengthAdd
                statPoints -= strengthAdd

                goodStats = True
            except ValueError:
                print("No integer selected. Try again. \n")
            
        goodStats = False    

        while goodStats == False:
            try:
                luck = int(input("You have " + str(statPoints) + " points left. How many points to put into luck: "))
                statPoints -= luck

                goodStats = True
            except ValueError:
                print("No integer selected. Try again. \n")

        goodStats = False

        while goodStats == False:
            try:
                defenceAdd = int(input("You have " + str(statPoints) + " points left. How many points to put into defence: "))
                defence += defenceAdd
                statPoints -= defenceAdd

                goodStats = True
            except ValueError:
                print("No integer selected. Try again. \n")
            
        goodStats = False

        while goodStats == False:
            try:
                dodgeAdd = int(input("You have " + str(statPoints) + " points left. How many points to put into dodge: "))
                dodge += dodgeAdd
                statPoints -= dodgeAdd
                
                goodStats = True
            except ValueError:
                print("No integer selected. Try again. \n")
            
        goodStats = False

        while goodStats == False:
            try:
                accuracyAdd = int(input("You have " + str(statPoints) + " points left. How many points to put into accuracy: "))
                accuracy += accuracyAdd
                statPoints -= accuracyAdd
                
                goodStats = True
            except ValueError:
                print("No integer selected. Try again. \n")
            
        goodStats = False

        if strengthAdd < 0 or luck < 0 or defenceAdd < 0 or dodgeAdd < 0:
            print("A negative value(s) has been detected. Please input valid stats.")

        elif statPoints == 0:
            print("You have chosen the stats: \n \n Strength = " + str(strength) + "\n Luck = " + str(luck) + "\n Defence = " + str(defence) + "\n Dodge = " + str(dodge) + "\n Accuracy = " + str(accuracy) + "\n")

            while keepStats == "N/A":

                keepStats = input("Keep stats? (y/n): ")

                if keepStats.lower() == "y":
                    goodStats = True
            
                    print("Your stats have been selected.")

                elif keepStats.lower() == "n":
                    print("Please select new stats: \n")
        
                else:
                    keepStats = "N/A"
                    print("You have not selected a valid value. please use \'y\' for \'yes\' and \'n\' for \'no\'. \n")

        else:
            print("Your stat points have been improperly distributed. Please redistribute stats.")

statsBase()

health = 10 + defence