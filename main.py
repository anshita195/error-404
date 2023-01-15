from flask import Flask, render_template, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import csv

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

QUESTIONS = {
    "Genre": [
        "action", "adventure", "comedy", "crime","romantic", "drama", "fantasy","horror","scifi",
    ],
    "Mood": [
        "happy", "gloomy", "angry", "inspired", "bored"
    ],
    "Language preference": [
        "english", "hindi"
    ] 
}

QUESTIONSk=QUESTIONS.keys()
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/questions")
def questions():
    return render_template("questions.html", q=QUESTIONSk, o=QUESTIONS)

@app.route("/responses",methods=['POST'])
def handle_data():
    answers=[]
    for i in QUESTIONS.keys():
        response=request.form[i]
        answers.append(response)
    csv_filename = 'worksheet.csv'
    with open(csv_filename) as f:
        reader = csv.reader(f)
        lst = list(reader)    
    results=[]    
    for i in (lst):
        if str(i[0])==str(answers[0]) and str(i[1])==str(answers[1]) and str(i[2])==str(answers[2]):
            results.append(i[3])
            # print('<p>'+i[3]+'</p>')
    if results==[]:
        return '<p>'"No movies found for given set of filters :("'</p>'
    return results

if __name__ == "__main__":
    app.run(debug=True)