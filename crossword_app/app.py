# app.py
from flask import Flask, render_template
import os
from crossword_app.crossword import generate_crossword, get_crossword_data, GRID_SIZE, generate_clue_list

app = Flask(__name__)

# ---------------------------
# PRE-GENERATE A PUZZLE ON STARTUP
# ---------------------------
PREGENERATED_PUZZLE = None
PRE_ROW_CLUES = []
PRE_COLUMN_CLUES = []

try:
    wordlist_path = os.path.join(os.getcwd(), 'word_lists', 'word_list_with_clues.txt')
    word_clues, words, clue_dict, prefix_dict = get_crossword_data(wordlist_path)

    solution = generate_crossword(words, prefix_dict)
    if solution:
        PREGENERATED_PUZZLE = solution
        PRE_ROW_CLUES, PRE_COLUMN_CLUES = generate_clue_list(solution, clue_dict)
except Exception as e:
    print(f"Error pre-generating puzzle: {e}")

# ---------------------------
# ROUTES
# ---------------------------
@app.route("/")
def home():
    try:
        if PREGENERATED_PUZZLE is None:
            return "<h1>No puzzle available right now. Try again later.</h1>"

        return render_template(
            "crossword.html",
            grid=PREGENERATED_PUZZLE,
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