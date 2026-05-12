from sys import exit

def statsBase():
    goodStats = False
    while goodStats == False:
        global strength
        global luck
        global defence
        global dodge
        global accuracy
        global health
        global room
        global difficulty

        keepStats = "N/A"
        statPoints = 20
        strength = 1
        defence = 1
        dodge = 1
        accuracy = 1

        maxPoints = statPoints - 4

        print()
        print()

        print("You have " + str(statPoints) + " stat points to spend.")
        print("These can be put into 5 attributes: Strength, Luck, Defence, Dodge and Accuracy \n")
        print("Each stat except for luck must be given 1 stat point.")

        print()

        while goodStats == False:
            try:
                strength = int(input("You have " + str(statPoints) + " points left. How many points to put into strength: "))
                if strength >= 1 and strength <= maxPoints:
                    statPoints -= strength

                    goodStats = True
                else:
                    print("Please select a number between 1 and " + str(maxPoints) +" inclusive. \n")
            except ValueError:
                print("No integer selected. Try again. \n")
            
        goodStats = False

        while goodStats == False:
            try:
                luck = int(input("You have " + str(statPoints) + " points left. How many points to put into luck: "))
                if luck >= 0 and luck <= maxPoints:
                    statPoints -= luck

                    goodStats = True
                else:
                    print("Please select a number between 1 and " + str(maxPoints) +" inclusive. \n")
            except ValueError:
                print("No integer selected. Try again. \n")

        goodStats = False

        while goodStats == False:
            try:
                defence = int(input("You have " + str(statPoints) + " points left. How many points to put into defence: "))
                if defence >= 1 and defence <= maxPoints:
                    statPoints -= defence

                    goodStats = True
                else:
                    print("Please select a number between 1 and " + str(maxPoints) +" inclusive. \n")
            except ValueError:
                print("No integer selected. Try again. \n")
            
        goodStats = False

        while goodStats == False:
            try:
                dodge = int(input("You have " + str(statPoints) + " points left. How many points to put into dodge: "))
                if dodge >= 1 and dodge <= maxPoints:
                    statPoints -= dodge
                
                    goodStats = True
                else:
                    print("Please select a number between 1 and " + str(maxPoints) +" inclusive. \n")
            except ValueError:
                print("No integer selected. Try again. \n")
            
        goodStats = False

        while goodStats == False:
            try:
                accuracy = int(input("You have " + str(statPoints) + " points left. How many points to put into accuracy: "))
                if accuracy >= 1 and accuracy <= maxPoints:
                    statPoints -= accuracy
                
                    goodStats = True
                else:
                    print("Please select a number between 1 and " + str(maxPoints) +" inclusive. \n")
            except ValueError:
                print("No integer selected. Try again. \n")
            
        goodStats = False

        if strength < 0 or luck < 0 or defence < 0 or dodge < 0:
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

        health = 10 + defence
        room = 1
        difficulty = 1

try:
    statsBase()
except KeyboardInterrupt:
    print("\n\n Goodbye!")
    exit()