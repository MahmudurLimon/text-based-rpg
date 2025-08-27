import os
import re
from mazefall import *

def cave_file_func():
    player_name=str(input("Ener Your Name: "))
    player_name=player_name.lower()
    cur_dir=os.getcwd()
    src_dir=f"src/player/"
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
                else:
                    print(f"{player_name} Folder is Corrupted!") # If a player folder "messi" contains a .txt file with another player's name "ronaldo1.txt"
            player_name_file=f"{player_name}{player_name_num_max}.txt"
            player_name_file_dir=os.path.join(comb_dir,player_name_file)
            with open (player_name_file_dir, "a") as a:
                a.write("Continuing Previous Exploration...\n")
        elif file_name == "n":
            ""
        else:
            ""
    else:
        ""

cave_file_func()
