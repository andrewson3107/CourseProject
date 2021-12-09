from flask import Flask, render_template, jsonify
# import src.scraper as scraper
# import src.formatter as formatter
# import src.ranker as ranker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/rank/<query>", methods=['GET'])
def rank(query):
    output = format_output()
    return jsonify(output)

def format_output():
    output = {
        'Job Name': 'Application Link',
    }

    return output
