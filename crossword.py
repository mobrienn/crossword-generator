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
# DATA FUNCTIONS
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

# GET CROSSWORD DATA ------
def get_crossword_data(wordlist="word_lists/word_list_with_clues.txt"):
    word_clues = load_words(wordlist)
    clue_dict = dict(word_clues)
    words = list(clue_dict.keys())
    prefix_dict = build_prefix_dict(words)
    return word_clues, words, clue_dict, prefix_dict

# GENERATE CLUE LIST ------
def generate_clue_list(grid,clue_dict):
    '''

    '''
    row_clues = []
    column_clues = []
    for r in range(GRID_SIZE):
        word = ''.join(letter for letter in grid[r] if letter.strip())
        clue = clue_dict.get(word,"No clue found")
        row_clues.append((r+1,"Across",clue,word))

    for c in range(GRID_SIZE):
        word = ''.join(grid[r][c]for r in range(GRID_SIZE))
        clue = clue_dict.get(word,"No clue found")
        column_clues.append((c+1,"Down",clue,word))
    
    return row_clues, column_clues

# ------------------------------------------
# CROSS WORD GENERATION FUNCTIONS
# ------------------------------------------

# GENERATE CROSSWORD ------
def generate_crossword(words, prefix_dict):
    '''
        
    '''
    grid = [['']*GRID_SIZE for _ in range(GRID_SIZE)] 
    slots = [
        (0,0,True,"1-Across"),(0,0,False,"1-Down"),
        (1,0,True,"2-Across"),(1,1,False,"2-Down"),
        (2,1,True,"3-Across"),(2,2,False,"3-Down"),
        (3,2,True,"4-Across"),(3,3,False,"4-Down"),
        (4,3,True,"5-Across"),(4,4,False,"5-Down")
        ]

    solution = fill_slot(grid,words,slots,prefix_dict,0)
    
    return solution

# POSSIBLE WORDS ------
def possible_words(grid, prefix_dict, row_idx, column_idx, is_row=True, words=None):
    '''
        Returns possible words for a slot based on current grid state and prefixes.
        If prefix is empty, `words` must be provided (list of all candidate words).
    '''
    if is_row:
        prefix = ''.join(letter for letter in grid[row_idx] if letter.strip())

    else:
        prefix = ''.join(grid[r][column_idx] for r in range(GRID_SIZE) if grid[r][column_idx].strip())

    if prefix == '':
        if words is None:
            raise ValueError("possible_words() needs `words` when there is no prefix")
        words_list = words[:]
    else:
        words_list = prefix_dict.get(prefix,[])

    random.shuffle(words_list)
    return words_list

# CHECK PREFIXES ------
def check_prefixes(grid, prefix_dict):
    '''
        Check if all row and column prefixes are valid.
        Empty strings are considered valid (temporary empty slots).
    '''
    # Check all rows
    for i in range(GRID_SIZE):
        row_prefix = ''.join(letter for letter in grid[i] if letter.strip()) # join all letters in a row
        if row_prefix and row_prefix not in prefix_dict:
            return False
        
    # Check all columns
    for c in range(GRID_SIZE):
        column_prefix = ''.join(grid[r][c] for r in range(5) if grid[r][c].strip()) # join all letters in a column
        if column_prefix and column_prefix not in prefix_dict:
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
def fill_slot(grid,words,slots,prefix_dict,slot_idx=0):
    '''
        Recursively attempt to fill crossword slots with valid words.
    '''
    if slot_idx >= len(slots):
        return grid
    
    row_idx,column_idx,is_row,label = slots[slot_idx]

    if slot_idx == 0:
        first_word = random.choice(words)
        for i, letter in enumerate(first_word):
            grid[row_idx][i] = letter
        return fill_slot(grid,words,slots,prefix_dict,slot_idx+1)
    possible = possible_words(grid,prefix_dict,row_idx,column_idx,is_row, words)
    for word in possible:
        temp_grid = copy.deepcopy(grid)
        temp_grid = place_word(temp_grid,row_idx,column_idx,prefix_dict,word,is_row)
        if temp_grid is None:
                continue 
        if check_prefixes(temp_grid,prefix_dict):
            solution = fill_slot(temp_grid,words,slots,prefix_dict,slot_idx+1)
            if solution:
                return solution 
    return None

# ------------------------------------------
# DISPLAY FUNCTIONS
# ------------------------------------------

# PRINT GRID ------
def print_grid(grid):
    '''
    
    '''
    size = len(grid)

    # Print column numbers with fixed width
    print("    " + "  ".join(f"{c+1:>2}" for c in range(size)))

    # Print top border
    print("   " + "┌" + "───┬"* (size-1) + "───┐")
    
    for r, row in enumerate(grid):
        # Print row number with fixed width + row content
        print(f"{r+1}  │ " + " │ ".join(f"{cell}" for cell in row) + " │")
        # Print row separator
        if r < size - 1:
            print("   " + "├" + "───┼"* (size-1) + "───┤")
    
    # Print bottom border
    print("   " + "└" + "───┴"* (size-1) + "───┘")

# ------------------------------------------
# WELCOME & PLAY GAME
# ------------------------------------------

# WELCOME SCREEN ------
def welcome_screen():
    print("======================================")
    print("         Welcome to Crossword        ")
    print("======================================")
    print("Type 'yes' to start or 'quit' to exit.\n")

    choice = input ("Do you want to play?    ").strip().lower()
    return choice == "yes"

# START GAME ------
def start_game():

    # Load words and build dictionaries
    word_clues, words, clue_dict, prefix_dict = get_crossword_data(wordlist="word_lists/word_list_with_clues.txt")
    
    print("\nGenerating your crossword puzzle...\n")
    solution = generate_crossword(words,prefix_dict) 
    if not solution:
        print("No solution can be generated. Try again later.")
        return
    else:
        row_clues, column_clues = generate_clue_list(solution,clue_dict)


    play_crossword(solution,row_clues,column_clues)

# PLAY CROSSWORD ------
def play_crossword(solution, row_clues,column_clues):
    '''
        
    '''
    print("\nHere's your crossword!\n\n")
    player_grid = [['_']*5 for _ in range(GRID_SIZE)]
    print_grid(player_grid)
    print("Across:")
    for clue in row_clues:
        print(f"{clue[0]}. {clue[2]}")
    print("Down")
    for clue in column_clues:
        print(f"{clue[0]}. {clue[2]}")

# ------------------------------------------
#  
# ------------------------------------------

# CLUE LOOKUP ------
def clue_lookup(word, clue_dict):
    '''
        Return the clue associated with a word.
    '''
    if word in clue_dict:
        return clue_dict[word]
    return "No clue found"

############################################         

