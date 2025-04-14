from flask import Flask, render_template, request
from puzzles.wordsearch import get_wordsearch
from puzzles.sudoku import get_sudoku
from puzzles.maze import get_maze
from puzzles.numbergrid import get_numbergrid

app = Flask(__name__)

puzzle_functions = {
    "wordsearch": get_wordsearch,
    "sudoku": get_sudoku,
    "maze": get_maze,
    "numbergrid": get_numbergrid
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/puzzle', methods=['GET', 'POST'])
def puzzle():
    puzzle_type = request.args.get('type') or request.form.get('type')
    if puzzle_type not in puzzle_functions:
        return "Invalid puzzle type."

    data = puzzle_functions[puzzle_type]()
    result = None
    solution = None
    show_solution = False

    if request.method == "POST":
        if 'reveal' in request.form:
            solution = data["solution"]
        else:
            user_answer = request.form.get("answer", "").strip().upper()
            correct_answer = data["answer"].strip().upper()
            if user_answer == correct_answer:
                result = "Correct!"
            else:
                result = "Wrong. Would you like to see the solution?"
                show_solution = True

    return render_template("puzzle.html",
                           puzzle_type=puzzle_type,
                           puzzle_html=data["html"],
                           rules=data["rules"],
                           result=result,
                           solution=solution,
                           show_solution=show_solution)

if __name__ == '__main__':
    app.run(debug=True)

