from mazefall import *

def textBasedMaze():
    cave = str(input("Do you want to Enter the Cave (y/n)?: "))
    if cave.lower() == "y":
        print(enterCave)
    elif cave.lower() == "n":
        print(exitCave)
    else:
        print("Error")

textBasedMaze()