import random

def generate_wordsearch(words, grid_size=10):
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    word_positions = {}

    def place_word(word):
        word_len = len(word)
        placed = False

        while not placed:
            row, col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            direction = random.choice(['horizontal', 'vertical', 'diagonal'])

            positions = []
            if direction == 'horizontal' and col + word_len <= grid_size:
                if all(grid[row][col + i] == ' ' for i in range(word_len)):
                    for i in range(word_len):
                        grid[row][col + i] = word[i]
                        positions.append((row, col + i))
                    placed = True
            elif direction == 'vertical' and row + word_len <= grid_size:
                if all(grid[row + i][col] == ' ' for i in range(word_len)):
                    for i in range(word_len):
                        grid[row + i][col] = word[i]
                        positions.append((row + i, col))
                    placed = True
            elif direction == 'diagonal' and row + word_len <= grid_size and col + word_len <= grid_size:
                if all(grid[row + i][col + i] == ' ' for i in range(word_len)):
                    for i in range(word_len):
                        grid[row + i][col + i] = word[i]
                        positions.append((row + i, col + i))
                    placed = True

            if placed:
                word_positions[word] = positions

    for word in words:
        place_word(word)

    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] == ' ':
                grid[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    return grid, word_positions

def wordsearch_to_html(grid, highlight_positions=None):
    table_html = '<table class="wordsearch-grid">'
    for r, row in enumerate(grid):
        table_html += '<tr>'
        for c, cell in enumerate(row):
            style = ''
            if highlight_positions and (r, c) in highlight_positions:
                style = 'style="background-color: yellow;"'
            table_html += f'<td {style}>{cell}</td>'
        table_html += '</tr>'
    table_html += '</table>'
    return table_html

def get_wordsearch():
    words = ['PYTHON', 'PUZZLE', 'GENIE', 'COMPUTER', 'CODE', 'WEB', 'ALGORITHM', 'DEVELOPER', 'AI', 'ML']
    grid, word_positions = generate_wordsearch(words)
    table_html = wordsearch_to_html(grid)

    # Combine all word positions for highlighting
    all_positions = set(pos for positions in word_positions.values() for pos in positions)
    solution_html = wordsearch_to_html(grid, highlight_positions=all_positions)

    return {
        "rules": "Find the following words in the grid, horizontally, vertically, or diagonally. The words can be forward or backward.",
        "html": table_html,
        "words": ', '.join(words),
        "answer": ', '.join(words),
        "solution": words
    }

