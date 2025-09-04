"""
crossword.py
Crossword Puzzle Generator
Author: Madison Taylor
Date: September 2025

Description:

==================================================================="""
# ------------------------------------------
# IMPORTS
# ------------------------------------------

import random



# ------------------------------------------
# FUNCTION DEFINITIONS
# ------------------------------------------

def load_words(wordlist.txt):
    word_clues=[]
    with open(wordlist.txt,"r") as file:
        for line in file:
            parts=line.strip().split(":")
            if len(parts)==2 and len(parts[0])==5:
                word_clues.append((parts[0].upper(),parts[1]))
    return word_clues #print for testing

def generate_crossword(word_list):

def place_word(grid,word,row_index):

def fits_grid(grid,word,row_index):

def remove_word(grid,row_index):

def print_grid(grid):

def init_player_grid():
    return [['_']*5 for _ in range(5)]

def print_player_grid(grid):

def play_crossword(solution):

# ------------------------------------------
# MAIN CODE
# ------------------------------------------

def main():

if __name__ == "__main__":
    main()

## Greeting

print("Hello! This is the start of my crossword project.")

## Generate Crossword

words = load_words("wordlist.txt")
print(words)
