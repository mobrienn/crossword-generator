from flask import Flask, render_template
from crossword import generate_crossword, get_crossword_data, GRID_SIZE, generate_clue_list

app = Flask(__name__)

@app.route("/")
def home():
    # Get crossword data
    words, clue_dict, prefix_dict = get_crossword_data("word_list_with_clues.txt")
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
    app.run(debug=True,port=5001)
