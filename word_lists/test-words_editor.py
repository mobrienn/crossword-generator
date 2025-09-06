# Read the original word:clue file and generate new clues
input_file = "test_word_list.txt"    # your original file
output_file = "word_list_with_clues.txt"

with open(input_file, "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    word, _ = line.split(":")  # ignore old clue
    new_clue = f"clue for {word.lower()}"
    new_lines.append(f"{word}:{new_clue}")

with open(output_file, "w") as f:
    f.write("\n".join(new_lines))

print(f"Updated clues saved to {output_file}")
