import random

def generate_number_grid(rows=5, cols=5, min_value=1, max_value=100):
    # Create an empty grid with random numbers
    grid = [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]
    return grid

def numbergrid_to_html(grid):
    table_html = '<table class="numbergrid">'
    for row in grid:
        table_html += '<tr>'
        for cell in row:
            table_html += f'<td>{cell}</td>'
        table_html += '</tr>'
    table_html += '</table>'
    return table_html

def get_numbergrid():
    grid = generate_number_grid()
    table_html = numbergrid_to_html(grid)
    return {
        "rules": "Find the sum of all numbers in the grid. Enter the correct sum below.",
        "html": table_html,
        "answer": "Sum of all numbers in the grid.",
        "solution": "The sum can be calculated by adding up all the numbers in the grid."
    }
