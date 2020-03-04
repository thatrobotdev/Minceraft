import random


class bcolors:  # colors for console text
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    UNDERLINE = '\033[4m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


gameCount = 0
while True:
    respawn = None
    print(bcolors.GREEN + """
***************************************************************
Will you survive your first night of...
 __  __   _                                         __   _   
|  \/  | (_)                                       / _| | |  
| \  / |  _   _ __     ___    ___   _ __    __ _  | |_  | |_ 
| |\/| | | | | '_ \   / __|  / _ \ | '__|  / _` | |  _| | __|
| |  | | | | | | | | | (__  |  __/ | |    | (_| | | |   | |_ 
|_|  |_| |_| |_| |_|  \___|  \___| |_|     \__,_| |_|    \__|

Be careful! Many perils await.
***************************************************************
    """ + bcolors.ENDC)

    mobNum = random.randrange(1, 10)

    singularNiceMobNames = [
        "chicken", "horse", "cow", "sheep", "seahorse", "pig"
    ]
    pluralNiceMobNames = [
        "chickens", "horses", "cows", "sheep", "seahorses", "sheep"
    ]
    colors = ["purple", "rainbow", "gray", "brown", "white", "green"]

    if mobNum > 1:
        mob = pluralNiceMobNames[random.randrange(len(pluralNiceMobNames))]
        pluralMob = True
    else:
        mob = singularNiceMobNames[random.randrange(len(singularNiceMobNames))]
        pluralMob = False

    if mob == "sheep":
        sheepColor = colors[random.randrange(len(colors))]
        mob = sheepColor + " " + mob

    print("You've spawned in the world, and you see " + bcolors.ORANGE +
          str(mobNum) + " " + str(mob) + bcolors.ENDC + ".")

    killedInnocentAnimalorAnimalsThatIsorAreProbablyStarvingOrHadAVeryHardLifeOrSomething = None

    while killedInnocentAnimalorAnimalsThatIsorAreProbablyStarvingOrHadAVeryHardLifeOrSomething not in {
            "y", "n"
    }:
        killedInnocentAnimalorAnimalsThatIsorAreProbablyStarvingOrHadAVeryHardLifeOrSomething = input(
            bcolors.BLUE + "\nStart punching them? (y/n) " + bcolors.PURPLE)

        killedInnocentAnimalorAnimalsThatIsorAreProbablyStarvingOrHadAVeryHardLifeOrSomething.lower(
        )

        print(bcolors.ENDC)

    killedAnimals = False

    if killedInnocentAnimalorAnimalsThatIsorAreProbablyStarvingOrHadAVeryHardLifeOrSomething == "y":
        print(
            "Wow, your first act of life in this new world is to start killing inncoent animals. PETA would be proud."
        )
        print(
            bcolors.UNDERLINE + bcolors.ORANGE + "\nThe " + mob + bcolors.ENDC
            + bcolors.UNDERLINE + " fall",
            end='')

        if pluralMob == False:
            print("s", end='')
        print(" on the ground with a hard thud.\n" + bcolors.ENDC)

        killedAnimals = True
    elif killedInnocentAnimalorAnimalsThatIsorAreProbablyStarvingOrHadAVeryHardLifeOrSomething == "n":
        print("Good you're not a monster.\n")

    print("You continue through the world, ", end='')

    if killedAnimals == False:
        print("eager to enjoy more of the wildlife, when you realize ", end='')
    else:
        print(
            bcolors.ORANGE +
            "looking for things occupy yourself other than killing animals, when you realize "
            + bcolors.ENDC,
            end='')

    print(
        "the sun is already setting! You need to chop down some wood from the forest nearby, so you can build yourself a house to protect yourself from the monsters that come out at night!"
    )

    forestType = None

    while forestType not in {"1", "2", "3"}:
        forestType = input(
            bcolors.BLUE +
            "\nWhich forest would you like to chop wood from? The birch forest (1), spruce forest (2), or the cave (3). "
            + bcolors.PURPLE)
        print(bcolors.ENDC, end='')

    forests = ["birch", "spruce", "cave"]
    forest = forests[int(forestType) - 1]
    if forest == "cave":
        print(
            bcolors.FAIL +
            "Y'all, that's not a forest. That's a cave. You go into the cave, shockingly underprepared for the monsters within. You get hit in the head with an arrow from a skeleton and die. You did not survive your first night of Minceraft."
            + bcolors.ENDC)
    else:
        print("\nYou create a", end='')
        if forest == "birch":
            print("n albeit, UGLY ", end='')
        print(
            bcolors.ORANGE + forest + " house" + bcolors.ENDC +
            ", and hide through the night. No creepers knocking on your door tonight! :D"
        )
        print(
            bcolors.GREEN +
            "\nYou've survived your first night of Mincecraft! Congratulations! Try again for a different ending."
            + bcolors.ENDC)

    while respawn not in {"y", "n"}:
        respawn = input(bcolors.BLUE + '\nRespawn? (y/n): ' + bcolors.ENDC)
    if respawn == 'y':
        print("\033[H\033[J")
        gameCount = gameCount + 1
        print(bcolors.PURPLE + "You've respawned " + str(gameCount) +
              " times" + bcolors.ENDC)
    else:
        print('Thanks for playing!')
        break
