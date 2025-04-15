import random

# Sudoku Solver (using backtracking)
def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

def find_empty_location(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def is_safe(board, row, col, num):
    # Check row
    for c in range(9):
        if board[row][c] == num:
            return False
    # Check column
    for r in range(9):
        if board[r][col] == num:
            return False
    # Check 3x3 grid
    start_row, start_col = row - row % 3, col - col % 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

# Sudoku Generator
def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_sudoku(board)
    return board

def fill_sudoku(board):
    for _ in range(12):  # Try filling 12 random cells
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_safe(board, row, col, num) or board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num

# Convert board to HTML table
def sudoku_to_html(board):
    table_html = '<table class="sudoku-grid">'
    for row in board:
        table_html += '<tr>'
        for cell in row:
            table_html += f'<td class="cell">{cell if cell != 0 else ""}</td>'
        table_html += '</tr>'
    table_html += '</table>'
    return table_html

# Get Sudoku puzzle and answer
def get_sudoku():
    board = generate_sudoku()
    table_html = sudoku_to_html(board)
    solution_board = [row[:] for row in board]  # Make a copy for solving
    solve_sudoku(solution_board)
    solution_html = sudoku_to_html(solution_board)
    
    return {
        "rules": "Fill in the grid with digits from 1 to 9. Each row, column, and 9x9 subgrid must contain each digit exactly once.",
        "html": table_html,
        "solution_html": solution_html,
        "solution": solution_board,
        "answer": "The correct Sudoku solution will be provided below."
    }

