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
        print("⚠️ Warning: No puzzle could be generated at startup.")
except FileNotFoundError:
    print(f"❌ Error: Word list not found at {wordlist_path}")
except Exception as e:
    print(f"❌ Error pre-generating puzzle: {e}")

# ---------------------------
# ROUTE
# ---------------------------
@app.route("/")
def crossword():
    try:
        # Empty grid shown to the user
        empty_grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        return render_template(
            "crossword.html",
            grid=empty_grid,                             # what user sees
            solution=PREGENERATED_PUZZLE or empty_grid,  # for checking letters
            row_clues=PRE_ROW_CLUES,
            column_clues=PRE_COLUMN_CLUES,
            size=GRID_SIZE
        )
    except Exception as e:
        return f"<h1>Error loading crossword: {e}</h1>"

# ---------------------------
# RUN LOCAL (debugging)
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)
