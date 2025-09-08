# Crossword Generator + Web App  

This project generates 5x5 crossword puzzles from a word list and provides an interactive way to play them.  
The backend is written in Python and handles grid generation, clue assignment, and validation.  
A simple Flask web app serves the puzzles in the browser, letting users fill in answers and check their progress.  

### Features
- Generates valid crossword puzzles from customizable word lists  
- Assigns clues automatically to words  
- Interactive web-based interface (via Flask + HTML)  
- Expandable design for larger grids or different clue styles  

### Future Ideas
- Save/load puzzles  
- Add scoring or timer  
- Mobile-friendly interface


#### 
crossword.py        -> puzzle logic (data)
app.py              -> server logic (Flask routes)
crossword.html      -> structure/layout
crossword.js        -> user interaction
crossword.css       -> styling
