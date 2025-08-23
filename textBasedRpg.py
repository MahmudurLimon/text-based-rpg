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
    
    nameFound=False
    maxNum=0
    playerNameLow=playerName.lower()
    for filename in os.listdir(playerDir):
        if filename.endswith(".txt") and playerNameLow in filename.lower():
            nameFound=True
            playerNameMatch = re.search(rf"{re.escape(playerNameLow)}(\d*)\.txt", filename.
            lower())
            if playerNameMatch:
                numString=playerNameMatch.group(1)
                num=int(numString) if numString.isdigit() else 0
                if num > maxNum:
                    maxNum=num

            break
        else:

    cave = str(input("Do you want to Enter the Cave (y/n)?: "))
    if cave.lower() == "y":
        #with open("", "")
        print(enterCave)
    elif cave.lower() == "n":
        print(exitCave)
    else:
        print("Error")

textBasedMaze()