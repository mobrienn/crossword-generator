"""===================================================================
Crossword Puzzle Generator - crossword.py
Author: Madison Taylor
Date: September 2025
Description: Generate 5x5 crossword puzzles using a word list and provides clues for each word.
==================================================================="""

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import random
import copy 

# ------------------------------------------
# CONSTANTS
# ------------------------------------------
GRID_SIZE = 5

# ------------------------------------------
# FUNCTION DEFINITIONS
# ------------------------------------------

# LOAD WORDS ------
def load_words(wordlist):
    '''
        Load 5-letter words and their clues from a text file.
        Returns list of tuples (word, clue).
        File format:   WORD:CLUE
    '''
    word_clues=[]
    with open(wordlist,"r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts)==2 and len(parts[0])==5:
                word_clues.append((parts[0].upper(),parts[1]))
    return word_clues

# BUILD PREFIX DICT ------
def build_prefix_dict(words):
    '''
        Build a prefix dictionary from a list of words.
        Keys: prefixes, Values: list of words starting with that prefix
    '''
    prefix_dict = {}
    for word in words:
        for i in range(1,len(word)+1):
            prefix = word[:i]
            prefix_dict.setdefault(prefix,[]).append(word)
    return prefix_dict

# CLUE LOOKUP ------
def clue_lookup(word, clue_dict):
    '''
        Return the clue associated with a word.
    '''
    if word in clue_dict:
        return clue_dict[word]
    return "No clue found"

# POSSIBLE WORDS ------
def possible_words(grid, prefix_dict, row_idx, column_idx, is_row=True):
    '''
        Returns possible words for a slot based on current grid state and prefixes.
    '''
    if is_row:
        prefix = ''.join(letter for letter in grid[row_idx] if letter.strip())

    else:
        prefix = ''.join(grid[r][column_idx] for r in range(GRID_SIZE) if grid[r][column_idx].strip())

    if prefix == '':
        words_list = list(clue_dict.keys())
    else:
        words_list = prefix_dict.get(prefix,[])

    shuffled = words_list[:]
    random.shuffle(shuffled)
    return shuffled
    
# CHECK PREFIXES ------
def check_prefixes(grid, prefix_dict):
    '''
        Check if all row and column prefixes are valid.
        Empty strings are considered valid (temporary empty slots).
    '''
    # Check all rows
    for i in range(GRID_SIZE):
        row_prefix = ''.join(letter for letter in grid[i] if letter.strip()) # join all letters in a row
        if row_prefix not in prefix_dict:
            if row_prefix == '':
                return True
            return False
        
    # Check all columns
    for c in range(GRID_SIZE):
        column_prefix = ''.join(grid[r][c] for r in range(5) if grid[r][c].strip()) # join all letters in a column
        if column_prefix not in prefix_dict:
            if column_prefix == '':
                return True
            return False
    
    return True

# PLACE WORD ------
def place_word(grid,row_idx,column_idx,prefix_dict,word,is_row=True):
    '''
        Place a word in a row or column on a temporary grid.
        Returns the new grid if valid, else None.
    '''
    temp = copy.deepcopy(grid)
    if is_row:
        for i, letter in enumerate(word):
            temp[row_idx][i] = letter
    else:
        for i, letter in enumerate(word):
            temp[i][column_idx] = letter

    if check_prefixes(temp,prefix_dict):
        return temp
    return None

# FILL SLOTS ------
def fill_slot(grid,words,slots,slot_idx=0):
    '''
        Recursively attempt to fill corssword slots with valid words.
    '''
    if slot_idx >= len(slots):
        return grid
    
    row_idx,column_idx,is_row,label = slots[slot_idx]

    if slot_idx == 0:
        first_word = random.choice(words)
        print("First word:", first_word) ### PRINT
      
    possible = possible_words(grid,prefix_dict,row_idx,column_idx,is_row)
    for word in possible:
        temp_grid = copy.deepcopy(grid)
        temp_grid = place_word(temp_grid,row_idx,column_idx,prefix_dict,word,is_row)
        if temp_grid is None:
                continue 
        if check_prefixes(temp_grid,prefix_dict):
            solution = fill_slot(temp_grid,words,slots,slot_idx+1)
            if solution:
                return solution 
    return None

# GENERATE CROSSWORD ------
def generate_crossword(words, prefix_dict):
    '''
        Generate 5x5 crossword grid and print the solution.
    '''
    grid = [['']*GRID_SIZE for _ in range(GRID_SIZE)] 
    slots = [
        (0,0,True,"1-Across"),(0,0,False,"1-Down"),
        (1,0,True,"2-Across"),(1,1,False,"2-Down"),
        (2,1,True,"3-Across"),(2,2,False,"3-Down"),
        (3,2,True,"4-Across"),(3,3,False,"4-Down"),
        (4,3,True,"5-Across"),(4,4,False,"5-Down")
        ]

    solution = fill_slot(grid,words,slots)
    if solution:
        print("Puzzle generated!")
        for row in solution:
                print(row)

    return solution

# INIT_PLAYER GRID ------
def init_player_grid():
    '''Generate a 5x5 player grid initialized with underscores.'''
    return [['_']*5 for _ in range(GRID_SIZE)]
            
# ------------------------------------------
# MAIN CODE
# ------------------------------------------

if __name__ == "__main__":
    word_clues = load_words("test_word_list.txt")
    clue_dict = dict(word_clues)
    words = list(clue_dict.keys())
    prefix_dict = build_prefix_dict(words)

    solution = generate_crossword(words,prefix_dict)

    if check_prefixes(solution,prefix_dict):
        print("Puzzle generated!)")
        for row in solution:
            print(row)
    else:
        print("No solution found.")