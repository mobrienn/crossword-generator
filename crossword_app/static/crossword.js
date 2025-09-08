let selectedCell = null;
let solution = window.solution || null;  // You can pass the real solution from Flask later

// Select a cell when clicked
function selectCell(cell) {
    if (selectedCell) {
        selectedCell.classList.remove("selected");
    }
    selectedCell = cell;
    selectedCell.classList.add("selected");

    // Optional: show clue
    const row = parseInt(cell.dataset.row);
    const col = parseInt(cell.dataset.col);
    let clueText = "";

    if (rowClues[row]) {
        clueText = `Row ${row + 1}: ${rowClues[row]}`;
    } else if (columnClues[col]) {
        clueText = `Column ${col + 1}: ${columnClues[col]}`;
    } else {
        clueText = "No clue for this cell.";
    }
    document.getElementById("current-clue").textContent = clueText;
}

// Add a letter to the selected cell
function addLetter(letter) {
    if (!selectedCell) return;

    const row = parseInt(selectedCell.dataset.row);
    const col = parseInt(selectedCell.dataset.col);

    selectedCell.textContent = letter;

    // Check correctness if solution exists
    if (solution && solution[row][col]) {
        if (letter === solution[row][col]) {
            selectedCell.style.color = "black";  // Correct
        } else {
            selectedCell.style.color = "red";    // Incorrect
        }
    } else {
        selectedCell.style.color = "black"; // Default
    }
}

// Delete last character (make cell empty)
function deleteLetter() {
    if (!selectedCell) return;
    selectedCell.textContent = "";
    selectedCell.style.color = "black";
}

// Clear cell completely
function clearCell() {
    deleteLetter();
}
