from mazefall import *
import os
import re

def textBasedMaze():
    dirCurrent=os.getcwd()
    srcFolder=r"\src\playerInfo"
    dirSrc=dirCurrent+srcFolder
    if not os.path.exists(dirSrc):
        os.makedirs(dirSrc)

    playerName = str(input("Enter your name: "))
    playerDir=os.path.join(dirSrc, playerName)
    if not os.path.exists(playerDir):
        os.makedirs(playerDir)

    cave = str(input("Do you want to enter the cave? (y/n): "))

    nameFound=False
    maxNum=0
    playerNameLow=playerName.lower()
    for filename in os.listdir(playerDir):
        if filename.endswith(".txt") and playerNameLow in filename.lower():
            playerNameMatch = re.search(rf"{re.escape(playerNameLow)}(\d*)\.txt", filename.lower())
            if playerNameMatch:
                numString=playerNameMatch.group(1)
                num=int(numString) if numString.isdigit() else 0
                if num > maxNum:
                    maxNum=num
                    nameFound=True
    if nameFound:
        contPrev=str(input("Do yoy want to continue your previous exploration monseiur? (y/n): "))
        if contPrev == "n":
            playerFile= f"{playerName}{maxNum+1}.txt"
            playerFileDir=os.path.join(playerDir, playerFile)
            with open (playerFileDir, "w") as f:
                f.write(f"{cave}\n")
        else:
            playerFile=f"{playerName}{maxNum}.txt"
            playerFileDir=os.path.join(playerDir, playerFile)
            with open (playerFileDir, "a") as f:
                f.write(f"{cave}\n")
    else:
        playerFile= f"{playerName}{maxNum+1}.txt"
        playerFileDir=os.path.join(playerDir, playerFile)
        with open (playerFileDir, "w") as f:
            f.write(f"{cave}\n")

    if cave.lower() == "y":
        print(enterCave)
    elif cave.lower() == "n":
        print(exitCave)
    else:
        print("Error")

textBasedMaze()