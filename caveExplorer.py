import os
import re
from mazefall import *

arr=[]

def cave_file_func():
    player_name=str(input("Ener Your Name: "))
    player_name=player_name.lower()
    cur_dir=os.getcwd()
    src_dir=f"/data/player/"
    comb_dir=f"{cur_dir}{src_dir}{player_name}"
    if os.path.exists(comb_dir):
        file_name=str(input("Do you Want to Play Saved Game?(y/n): "))
        if file_name == "y":
            player_name_num_max=0
            for i_file in os.listdir(comb_dir):
                if i_file.endswith(".txt") and player_name in i_file.lower():
                    player_name_seq=re.search(rf"{re.escape(player_name)}(\d*)\.txt", i_file.lower())
                    player_name_str=player_name_seq.group(1)
                    player_name_num=int(player_name_str) if player_name_str.isdigit() else 0
                    if player_name_num > player_name_num_max:
                        player_name_num_max=player_name_num

                        # add else statement where it will create a new player file "player1"
                else:
                    print(f"{player_name} Folder is Corrupted!") # If a player folder "messi" contains a .txt file with another player's name "ronaldo1.txt"
            player_name_file=f"{player_name}{player_name_num_max}.txt"
            player_name_file_dir=os.path.join(comb_dir,player_name_file)
            with open (player_name_file_dir, "a") as a:

                # introduce keeping track of how many times this file was opened

                a.write("Continuing Previous Exploration...\n")
        elif file_name == "n":
            player_name_num_max=0
            for i_file in os.listdir(comb_dir):
                if i_file.endswith(".txt") and player_name in i_file.lower():
                    player_name_seq=re.search(rf"{re.escape(player_name)}(\d*)\.txt", i_file.lower())
                    player_name_str=player_name_seq.group(1)
                    player_name_num=int(player_name_str) if player_name_str.isdigit() else 0
                    if player_name_num > player_name_num_max:
                        player_name_num_max=player_name_num

                         # add else statement where it will create a new player file "player1"
                else:
                    print(f"{player_name} Folder is Corrupted!") 
                    # If a player folder "messi" contains a .txt file with another player's name "ronaldo1.txt"
            player_name_file=f"{player_name}{player_name_num_max+1}.txt"
            player_name_file_dir=os.path.join(comb_dir,player_name_file)
            with open (player_name_file_dir, "w") as w:
                w.write("You have Started Your First Cave Exploration.\n")
        else:
            print(error)
    else:
        os.makedirs(comb_dir)
        player_name_file=f"{player_name}1.txt"
        player_name_file_dir=os.path.join(comb_dir,player_name_file)
        with open (player_name_file_dir, "w") as w:
            w.write("You have Started Your First Cave Exploration.\n")

    return player_name_file_dir

""" def cave_exploration_func(player_name_file_dir):
    cave_input=str(input("Do you want to enter the cave? (y/n): "))
    if cave_input == "y":
        with open (player_name_file_dir, "a") as a:
            a.write(f"{cave_input}\n")
            print(enterCave)
    elif cave_input == "n":
        with open (player_name_file_dir, "a") as a:
            a.write(f"{cave_input}\n")
            print(exitCave)
    else:
        print(error) """

def cave_exploration_func(player_name_file_dir):
    while True:
        cave_input=str(input("Do you want to enter the cave? (y/n): "))
        arr.append(cave_input)
        if cave_input == "y":
            print(enterCave)
            while True:
                cave_input=str(input("Which Way do you want to Go? Left or Forward?(l/f): "))
                arr.append(cave_input)
                if cave_input == "l":
                    print(good["treasure"])
                    while True:
                        cave_input=str(input("There's only one Way to go, Right.(r): "))
                        arr.append(cave_input)
                        if cave_input == "r":
                            print(neutral)
                            break
                        else:
                            print(error)
                            arr.remove(cave_input)
                    break
                elif cave_input == "f":
                    print(harm["deadend"])
                else:
                    print(error)
                    arr.remove(cave_input)
            break
        elif cave_input == "n":
            print(exitCave)
        else:
            print(error)
            arr.remove(cave_input)
        with open(player_name_file_dir, "a") as a:
            for data in arr:
                a.write(str(data)+"\n")

player_name_file_dir=cave_file_func()
cave_exploration_func(player_name_file_dir)
