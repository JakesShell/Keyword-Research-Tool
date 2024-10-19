# app/app.py
from flask import Flask, render_template, request, send_file
import pandas as pd
import requests
from bs4 import BeautifulSoup
from utils import get_keywords  # Import the utility function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        seed_keyword = request.form['seed_keyword']
        keywords_data = get_keywords(seed_keyword)
        return render_template('index.html', keywords=keywords_data)
    return render_template('index.html', keywords=None)

@app.route('/download', methods=['POST'])
def download():
    keywords_data = request.form.getlist('keywords[]')
    df = pd.DataFrame(keywords_data)
    df.to_csv('keywords.csv', index=False)
    return send_file('keywords.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
