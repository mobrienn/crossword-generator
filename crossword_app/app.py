# app.py
from flask import Flask, render_template
import os
from crossword import generate_crossword, get_crossword_data, GRID_SIZE, generate_clue_list

app = Flask(__name__)

# ---------------------------
# PRE-GENERATE A PUZZLE ON STARTUP
# ---------------------------
PREGENERATED_PUZZLE = None
PRE_ROW_CLUES = []
PRE_COLUMN_CLUES = []

try:
    # Absolute path to this script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    wordlist_path = os.path.join(BASE_DIR, 'word_lists', 'word_list_with_clues.txt')

    # Load crossword data
    word_clues, words, clue_dict, prefix_dict = get_crossword_data(wordlist_path)

    # Generate the crossword
    solution = generate_crossword(words, prefix_dict)
    if solution:
        PREGENERATED_PUZZLE = solution
        PRE_ROW_CLUES, PRE_COLUMN_CLUES = generate_clue_list(solution, clue_dict)
    else:
        print("Warning: No puzzle could be generated at startup.")
except FileNotFoundError:
    print(f"Error: Word list not found at {wordlist_path}")
except Exception as e:
    print(f"Error pre-generating puzzle: {e}")

# ---------------------------
# ROUTES
# ---------------------------
@app.route("/")
def home():
    try:
        # Empty grid displayed to user
        empty_grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        # Safe defaults for JS
        solution = PREGENERATED_PUZZLE or [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        row_clues = PRE_ROW_CLUES or []
        column_clues = PRE_COLUMN_CLUES or []

        return render_template(
            "crossword.html",
            grid=empty_grid,        # what user sees
            solution=solution,      # for checking letters
            row_clues=row_clues,    # clues for JS
            column_clues=column_clues,
            size=GRID_SIZE
        )
    except Exception as e:
        return f"<h1>Error loading crossword: {e}</h1>"

# ---------------------------
# RUN LOCAL (debugging)
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)
