"""===================================================================
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

''' Load words and clues from a text file - store as list of tuples (word, clue)'''
def load_words(wordlist):
    word_clues=[]
    with open(wordlist,"r") as file:
        for line in file:
            parts=line.strip().split(":")
            if len(parts)==2 and len(parts[0])==5:
                word_clues.append((parts[0].upper(),parts[1]))
    return word_clues #print for testing

def build_prefix_dict(words):
    prefix_dict = {}
    for word in words:
        for i in range(1,6):
            prefix = word[:i]
            prefix_dict.setdefault(prefix,[]).append(word)
    return prefix_dict

''' Generate a 5x5 crossword solution grid and returns it with associated clues'''
def generate_crossword(word_clues):

    #Very basic random selection of 5 words from the list - to be improved later

    selected_words = random.sample(word_clues,5)

    solution = [list(word[0]) for word in selected_words]

    clues = [word[1] for word in selected_words]

    return solution, clues

#def place_word(grid,word,row_index):

#def fits_grid(grid,word,row_index):

#def remove_word(grid,row_index):

#def print_grid(grid):

'''Generate a 5x5 player grid initialized with underscores'''
def init_player_grid():
    return [['_']*5 for _ in range(5)]

#def update_player_grid(grid,solution,row_index):

#def print_player_grid(grid):

#def play_crossword(solution):

# ------------------------------------------
# MAIN CODE
# ------------------------------------------

#def main():

#if __name__ == "__main__":
    #main()

## Greeting

#print("Hello! This is the start of my crossword project.")

## Generate Crossword


words = load_words("test_word_list.txt")

print(len(words))
print(words[:40])

valid_word_set = set(word for word, clue in words)

prefix_dict = build_prefix_dict(valid_word_set)

print(len(prefix_dict))

solution, clues = generate_crossword(words)