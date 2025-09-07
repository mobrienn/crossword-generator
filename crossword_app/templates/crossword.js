// ---------------------------
// Global Variables
// ---------------------------
let selectedCells = []; // currently selected word cells
let selectedClue = null;

// ---------------------------
// Grid Selection
// ---------------------------
function selectCell(cell) {
    // Remove previous selection
    selectedCells.forEach(c => c.classList.remove("selected"));
    selectedCells = [];

    const row = parseInt(cell.dataset.row);
    const col = parseInt(cell.dataset.col);

    // Determine across or down word (simple logic: across unless last column)
    const isAcross = col < cell.closest("table").rows.length - 1;

    if (isAcross) {
        for (let c = col; c < cell.closest("table").rows.length; c++) {
            let td = document.querySelector(`td[data-row='${row}'][data-col='${c}']`);
            selectedCells.push(td);
            td.classList.add("selected");
        }
        selectedClue = rowClues[row][2]; // from Flask
    } else {
        for (let r = row; r < cell.closest("table").rows.length; r++) {
            let td = document.querySelector(`td[data-row='${r}'][data-col='${col}']`);
            selectedCells.push(td);
            td.classList.add("selected");
        }
        selectedClue = columnClues[col][2];
    }

    document.getElementById("current-clue").innerText = selectedClue;
}

// ---------------------------
// Letter Input
// ---------------------------
function addLetter(letter) {
    for (let td of selectedCells) {
        if (!td.innerText || td.innerText === "_") {
            td.innerText = letter;
            break;
        }
    }
}

function deleteLetter() {
    for (let i = selectedCells.length - 1; i >= 0; i--) {
        if (selectedCells[i].innerText && selectedCells[i].innerText !== "_") {
            selectedCells[i].innerText = "_";
            break;
        }
    }
}

function clearWord() {
    selectedCells.forEach(td => td.innerText = "_");
}
