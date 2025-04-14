import random

def generate_random_maze(rows=5, cols=5):
    # Create empty maze with all walls
    maze = [['1' for _ in range(cols)] for _ in range(rows)]

    # Carve a random path from (0, 0) to (rows-1, cols-1)
    x, y = 0, 0
    maze[x][y] = 'S'
    path = [(x, y)]
    
    while (x, y) != (rows - 1, cols - 1):
        direction = random.choice(['down', 'right'])
        if direction == 'down' and x < rows - 1:
            x += 1
        elif direction == 'right' and y < cols - 1:
            y += 1
        maze[x][y] = '0'
        path.append((x, y))

    maze[rows - 1][cols - 1] = 'E'

    return maze

def get_maze():
    maze_layout = generate_random_maze()
    table_html = '<table class="maze-grid">'
    for row in maze_layout:
        table_html += '<tr>'
        for cell in row:
            cell_class = ''
            if cell == '1':
                cell_class = 'wall'
            elif cell == 'S':
                cell_class = 'start'
            elif cell == 'E':
                cell_class = 'end'
            else:
                cell_class = 'path'
            table_html += f'<td class="{cell_class}">{cell}</td>'
        table_html += '</tr>'
    table_html += '</table>'

    return {
        "rules": "Navigate from S (Start) to E (End) without touching walls. Walls are black. Find a clear path!",
        "html": table_html,
        "answer": "Random — varies every time!",
        "solution": "Visually trace the 0s from S to E."
    }
