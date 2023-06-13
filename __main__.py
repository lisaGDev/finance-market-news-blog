from flask import Flask
from pages.detail import str
from pages.index import lst
app = Flask(__name__)

@app.route('/')
def index():
    return lst

@app.route('/dog')
def detail():
    return str

@app.route('/<title>')
def article_page(title):
    return "Article: %s" % title

if __name__ == '__main__':
    app.run()