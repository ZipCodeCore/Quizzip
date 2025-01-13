from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample questions and answers
quiz_data = []

@app.route('/')
def home():
    return render_template("home.html", questions=quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
