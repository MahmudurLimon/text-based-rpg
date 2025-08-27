import os
import re
from mazefall import *

def cave_file_func():
    p_name=str(input("Ener Your Name: "))
    p_name=p_name.lower()
    cur_dir=os.getcwd()
    src_dir=f"src/player/"
    comb_dir=f"{cur_dir}{src_dir}{p_name}"
    if os.path.exists(comb_dir):
        file_name=str(input("Do you Want to Play Saved Game?(y/n): "))
        if file_name == "y":
            p_name_num_max=0
            for i_file in os.listdir(comb_dir):
                if i_file.endswith(".txt") and p_name in i_file.lower():
                    p_name_seq=re.search(rf"{re.escape(p_name)}(\d*)\.txt", i_file.lower())
                    p_name_str=p_name_seq.group(1)
                    p_name_num=int(p_name_str) if p_name_str.isdigit() else 0
                    if p_name_num > p_name_num_max:
                        p_name_num_max=p_name_num
                else:
                    print(f"{p_name} Folder is Corrupted!") # If a player folder "messi" contains a .txt file with another name "ronaldo1.txt"
            p_name_file=f"{p_name}{p_name_num_max}.txt"
            p_name_file_dir=os.path.join(comb_dir,p_name_file)
            with open (p_name_file_dir, "a") as a:
                a.write("Continuing Previous Exploration...\n")
        elif file_name == "n":
            ""
        else:
            ""
    else:
        ""

cave_file_func()
