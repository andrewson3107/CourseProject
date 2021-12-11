from flask import Flask, render_template, jsonify, request
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/rank", methods=['POST'])
def rank():
    query = request.form['query']
    os.system(f"py ../src/ranker.py {query}")

    output = {'ranking': []}
    f = open('../data/ranked/links.txt', 'r', encoding='utf-8')
    for line in f:
        temp = line.split(" -> ")
        output['ranking'].append({temp[0]: temp[1][:-1]})
    f.close()

    return output, 200


@app.route("/scrape", methods=['POST'])
def scrape():
    scraping_query = request.form['scraping_query']
    os.system(f"py ../src/scraper.py {scraping_query}")

    return 200