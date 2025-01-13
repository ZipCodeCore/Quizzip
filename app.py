from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample questions and answers
quiz_data = [
    {"question": "What is the output of `print(2**3)`?", "options": ["6", "8", "9", "12"], "answer": "8"},
    {"question": "Which data type is mutable in Python?", "options": ["tuple", "string", "list", "int"], "answer": "list"},
    {"question": "What does `len()` do in Python?", "options": ["Finds length", "Sorts list", "Checks type", "Converts type"], "answer": "Finds length"},
    {"question": "Which keyword is used to create a function in Python?", "options": ["function", "define", "def", "lambda"], "answer": "def"},
    {"question": "What is the time complexity of accessing an element in a dictionary?", "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "answer": "O(1)"},
]

@app.route('/')
def home():
    return render_template("home.html", questions=quiz_data)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = request.form
    score = 0

    for i, question in enumerate(quiz_data):
        if user_answers.get(f"q{i}") == question["answer"]:
            score += 1

    return render_template("result.html", score=score, total=len(quiz_data))

if __name__ == '__main__':
    app.run(debug=True)
