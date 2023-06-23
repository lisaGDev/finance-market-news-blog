from flask import Flask, render_template, url_for, redirect
from firebase_data.data import get_data
app = Flask(__name__)

news_articles = get_data('/Users/lisagalva/Desktop/Python_Projects/finance-market-news-blog/firebase_data/articles.json')

@app.route('/default')
def index():
    return render_template("layout.html")

@app.route('/', methods=['GET'])
def detail():
    return render_template("posts.html", news_articles=news_articles)

@app.route('/my_dog_missin')
def my_dog_missin():
    return render_template("dog.html")

@app.route('/food_crisis')
def food_crisis():
    return render_template("crisis.html")

@app.route('/climate_change')
def climate_change():
    return render_template("climate.html")

@app.route("/<article>")
def articles(article):
    if article == 'climate':
        return redirect(url_for('my_dog_missin'))
    if article == 'crisis':
        return redirect(url_for('food_crisis'))
    if article == 'dog':
        return redirect(url_for('climate_change'))
    # return "404 Article Not Found"

if __name__ == '__main__':
    # print(get_data())
    # for news_article in get_data():
    # print(news_articles)
    app.run()