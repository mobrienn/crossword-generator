let selectedCell = null;
let clueMode = "row"; // default

// Select a cell when clicked
function selectCell(cell) {
    if (selectedCell) {
        selectedCell.classList.remove("selected");
    }
    selectedCell = cell;
    selectedCell.classList.add("selected");

    // If clicking the same cell, toggle clue mode
    if (selectedCell === cell) {
        clueMode = (clueMode === 'row') ? "column" : "row";
    } else {

        clueMode = "row";
    }

    selectedCell = cell;
    selectedCell.classList.add("selected");

    // Get coordinates
    const row = parseInt(cell.dataset.row);
    const col = parseInt(cell.dataset.col);

    // Show clue based on clueMode
    let clueText = "";
    if (clueMode === "row" && rowClues[row]) {
        clueText = `Row ${row + 1}: ${rowClues[row][2]}`;  // [2] is the clue string
    } else if (clueMode === "column" && columnClues[col]) {
        clueText = `Column ${col + 1}: ${columnClues[col][2]}`;        
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
