from flask import Flask, render_template, url_for, redirect
from firebase_data.data import get_data
app = Flask(__name__)

news_articles = get_data()

@app.route('/default')
def index():
    return render_template("layout.html")

@app.route('/', methods=['GET'])
def detail():
    return render_template("posts.html", news_articles=news_articles)

@app.route("/<string:post_id>", methods=['GET'])
def show_article(post_id):
    return render_template(post_id + ".html")

if __name__ == '__main__':
    app.run()