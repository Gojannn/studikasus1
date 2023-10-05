from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')

def score():
    students = [
        {"name" : "Sandrine", "Score": 100},
        {"name" : "Gergeley", "Score": 87},
        {"name" : "Frieda", "Score": 92},
        {"name" : "Fritz", "Score": 40},
        {"name" : "Sirius", "Score": 75},
    ]
    
    return render_template("index.html", students=students)

