from flask import Flask, render_template, request, jsonify
import ranker as ranker
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/rank", methods=['POST'])
def rank():
    query = request.form['query']
    ranker.main(query)
    f = open('../data/ranked/links.txt', 'w', encoding='utf-8')
    return f
