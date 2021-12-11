from flask import Flask, render_template, jsonify, request
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/rank", methods=['POST'])
def rank():
    query = request.form['query']
    print(query)

    output = {'ranking': []}
    # os.system("py ../src/ranker.py")

    f = open('../data/ranked/links.txt', 'r', encoding='utf-8')
    for line in f:
        temp = line.split(" -> ")
        output['ranking'].append({temp[0]: temp[1][:-1]})

    return output, 200
