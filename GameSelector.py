import random
def addGame():
    while True:
        gameInfo = ""
        whichLibrary = input("Which library would you like to look at? The options are PC(0), PS4(1), Switch(2), Handheld(3), or quit(4)\n")
        if whichLibrary == "0":
            while True:
                whichService = int(input("Which service would you like to look at? Steam(0), Epic(1), or quit(2)\n"))
                if whichService == 0:
                    o = open("steamGames.txt", "a+")
                    newGame = input("What is the name of the game that you want to add?\n")
                    gameInfo = newGame
                    newGame = input("Have you beaten the game? Y/N\n")
                    gameInfo += " " + newGame
                    newGame = input("Have you gotten all the achievements for the game? Y/N\n")
                    gameInfo += " " + newGame + "\n"
                    o.write(gameInfo)
                    o.close()
                elif whichService == 1:
                    o = open("epicGames.txt", "a+")
                    newGame = input("What is the name of the game that you want to add?\n")
                    gameInfo = newGame
                    newGame = input("Have you beaten the game? Y/N\n")
                    gameInfo += " " + newGame
                    newGame = input("Have you gotten all the achievements for the game? Y/N\n")
                    gameInfo += " " + newGame + "\n"
                    o.write(gameInfo)
                    o.close()
                else:
                    break
        elif whichLibrary == "1":
            while True:
                o = open("ps4Games.txt", "a+")
                newGame = input("What is the name of the game that you want to add?\n")
                gameInfo = newGame
                newGame = input("Have you beaten the game? Y/N\n")
                gameInfo += " " + newGame
                newGame = input("Have you gotten all the achievements for the game? Y/N\n")
                gameInfo += " " + newGame + "\n"
                o.write(gameInfo)
                o.close()
                quitter = input("Would you like to quit?\n")
                if quitter == "Y":
                    break
        elif whichLibrary == "2":
            while True:
                o = open("switchGames.txt", "a+")
                newGame = input("What is the name of the game that you want to add?\n")
                gameInfo = newGame
                newGame = input("Have you beaten the game? Y/N\n")
                gameInfo += " " + newGame + "\n"
                o.write(gameInfo)
                o.close()
                quitter = input("Would you like to quit?\n")
                if quitter == "Y":
                    break
        elif whichLibrary == "3":
            while True:
                whichDevice = int(input("Which device would you like to look at? DS(0), Gameboy(1), or quit(2)\n"))
                if whichDevice == 0:
                    o = open("DSGames.txt", "a+")
                    newGame = input("What is the name of the game that you want to add?\n")
                    gameInfo = newGame
                    newGame = input("Have you beaten the game? Y/N\n")
                    gameInfo += " " + newGame + "\n"
                    o.write(gameInfo)
                    o.close()
                elif whichDevice == 1:
                    o = open("GameBoyGames.txt", "a+")
                    newGame = input("What is the name of the game that you want to add?\n")
                    gameInfo = newGame
                    newGame = input("Have you beaten the game? Y/N\n")
                    gameInfo += " " + newGame + "\n"
                    o.write(gameInfo)
                    o.close()
                else:
                    break
        else:
            break
def removeGame():
    #Method: write all the lines into a variable, then clear the file and write back all of the lines except for the one that needs to be removed.
    whichLibrary = int(input("Which library would you like to look at? The options are PC(0), PS4(1), Switch(2), Handheld(3)\n"))
    if whichLibrary == 0:
        whichService = int(input("Which service would you like to look at? Steam(0) or Epic(1)\n"))
        if whichService == 0:
            gameOut = input("What is the name of the game that you want to remove?\n")
            o = open("steamGames.txt", "r")
            lines = o.readlines()
            o.close()
            p = open("steamGames.txt", "w+")
            for line in lines:
                splitLine = line.split()
                if splitLine[0] != gameOut:
                    p.write(line)
            p.close()
        elif whichService == 1:
            gameOut = input("What is the name of the game that you want ta remove?\n")
            o = open("epicGames.txt", "r")
            lines = o.readlines()
            o.close()
            p = open("epicGames.txt", "w+")
            for line in lines:
                splitLine = line.split()
                if splitLine[0] != gameOut:
                    p.write(line)
            p.close()
    elif whichLibrary == 1:
        gameOut = input("What is the name of the game that you want to remove?\n")
        o = open("ps4Games.txt", "r")
        lines = o.readlines()
        o.close()
        p = open("ps4Games.txt", "w+")
        for line in lines:
            splitLine = line.split()
            if splitLine[0] != gameOut:
                p.write(line)
        p.close()
    elif whichLibrary == 2:
        gameOut = input("What is the name of the game that you want to remove?\n")
        o = open("switchGames.txt", "r")
        lines = o.readlines()
        o.close()
        p = open("switchGames.txt", "w+")
        for line in lines:
            splitLine = line.split()
            if splitLine[0] != gameOut:
                p.write(line)
        p.close()
    elif whichLibrary == 3:
        whichDevice = int(input("Which device would you like to look at? DS(0) or Gameboy(1)\n"))
        if whichDevice == 0:
            gameOut = input("What is the name of the game that you want to remove?\n")
            o = open("DSGames.txt", "r")
            lines = o.readlines()
            o.close()
            p = open("DSGames.txt", "w+")
            for line in lines:
                splitLine = line.split()
                if splitLine[0] != gameOut:
                    p.write(line)
            p.close()
        elif whichDevice == 1:
            gameOut = input("What is the name of the game that you want to remove?\n")
            o = open("GameBoyGames.txt", "r")
            lines = o.readlines()
            o.close()
            p = open("GameBoyGames.txt", "w+")
            for line in lines:
                splitLine = line.split()
                if splitLine[0] != gameOut:
                    p.write(line)
            p.close()
def changeCharacteristic():
    return 0
def viewLibrary():
    howBig = int(input("Would you like to view a specific game library(0), everything(1), or a random game(2)?\n"))
    if howBig == 0:
        specificLibrary = int(input("Which library would you like to view? PC(0), PS4(1), Switch(2), Handheld(3)\n"))
        if specificLibrary == 0:
            specificPCLibrary = int(input("Which PC library? Steam(0), Epic(1)\n"))
            if specificPCLibrary == 0:
                o = open("steamGames.txt", "r")
                lines = o.readlines()
                print("Here are the games in the Steam Library: \n")
                for line in lines:
                    print(line)
                o.close()
            else:
                o = open("epicGames.txt", "r")
                lines = o.readlines()
                print("Here are the games in the Epic Library: \n")
                for line in lines:
                    print(line)
                o.close()
        elif specificLibrary == 1:
            o = open("ps4Games.txt", "r")
            lines = o.readlines()
            print("Here are the games in the PS4 Library: \n")
            for line in lines:
                print(line)
            o.close()
        elif specificLibrary == 2:
            o = open("switchGames.txt", "r")
            lines = o.readlines()
            print("Here are the games in the Switch Library: \n")
            for line in lines:
                print(line)
            o.close()
        elif specificLibrary == 3:
            specificHHLibrary = int(input("Which Handheld library? DS(0), GameBoy(1)"))
            if specificHHLibrary == 0:
                o = open("DSGames.txt", "r")
                lines = o.readlines()
                print("Here are the games in the DS Library: \n")
                for line in lines:
                    print(line)
                o.close()
            else:
                o = open("GameBoyGames.txt", "r")
                lines = o.readlines()
                print("Here are the games in the GameBoy Library: \n")
                for line in lines:
                    print(line)
                o.close()
    elif howBig == 1:
        o = open("steamGames.txt", "r")
        lines = o.readlines()
        print("Here are the games in the Steam Library: \n")
        for line in lines:
            print(line)
        o.close()
        p = open("epicGames.txt", "r")
        lines = p.readlines()
        print("Here are the games in the Epic Library: \n")
        for line in lines:
            print(line)
        p.close()
        q = open("ps4Games.txt", "r")
        lines = q.readlines()
        print("Here are the games in the PS4 Library: \n")
        for line in lines:
            print(line)
        q.close()
        w = open("switchGames.txt", "r")
        lines = w.readlines()
        print("Here are the games in the Switch Library: \n")
        for line in lines:
            print(line)
        w.close()
        t = open("DSGames.txt", "r")
        lines = t.readlines()
        print("Here are the games in the DS Library: \n")
        for line in lines:
            print(line)
        t.close()
        u = open("GameBoyGames.txt", "r")
        lines = u.readlines()
        print("Here are the games in the GameBoy Library: \n")
        for line in lines:
            print(line)
        u.close()
    elif howBig == 2:
        bigFile = open("combinedGames.txt", "w+")
        o = open("steamGames.txt", "r")
        lines = o.readlines()
        for line in lines:
            bigFile.write(line)
        o.close()
        p = open("epicGames.txt", "r")
        lines = p.readlines()
        for line in lines:
            bigFile.write(line)
        p.close()
        q = open("ps4Games.txt")
        lines = q.readlines()
        for line in lines:
            bigFile.write(line)
        q.close()
        w = open("switchGames.txt", "r")
        lines = w.readlines()
        for line in lines:
            bigFile.write(line)
        w.close()
        t = open("DSGames.txt", "r")
        lines = t.readlines()
        for line in lines:
            bigFile.write(line)
        t.close()
        u = open("GameBoyGames.txt", "r")
        lines = u.readlines()
        for line in lines:
            bigFile.write(line)
        u.close()
        bigFile.close()
        randomFile = open("combinedGames.txt", "r+")
        lines = randomFile.readlines()
        rng = random.randint(0, len(lines)-1)
        print("Your random game is....." + lines[rng])
        randomFile.close()
while(True):
    question = input("What would you like to do today? The options are: AddGame(0), RemoveGame(1), ChangeCharacteristic(2), ViewLibrary(3), or quit(4) \n")

    if question == "0":
        addGame()
    elif question == "1":
        removeGame()
    elif question == "2":
        changeCharacteristic()
    elif question == "3":
        viewLibrary()
    else:
        break


