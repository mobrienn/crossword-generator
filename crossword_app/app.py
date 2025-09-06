from flask import Flask, render_template
import sys
import os

# Add parent folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crossword import generate_crossword, get_crossword_data, GRID_SIZE, generate_clue_list

app = Flask(__name__)


@app.route("/")
def home():
    # Build absolute path to the word list
    wordlist_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'word_lists', 'word_list_with_clues.txt')
)
    
    # Get crossword data
    word_clues, words, clue_dict, prefix_dict = get_crossword_data(wordlist_path)
    solution = generate_crossword(words, prefix_dict)
    
    if not solution:
        return "No solution could be generated. Try again later."
    
    row_clues, column_clues = generate_clue_list(solution, clue_dict)

    return render_template(
        "crossword.html",
        grid=solution,
        row_clues=row_clues,
        column_clues=column_clues,
        size=GRID_SIZE
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)