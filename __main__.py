from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

news_articles = [{ 
    "name": "My Dog Missin'",
    "url": "/my_dog_missin"
}]

@app.route('/default')
def index():
    return render_template("layout.html")

@app.route('/')
def detail():
    return render_template("posts.html", news_articles=news_articles)

@app.route('/my_dog_missin')
def my_dog_missin():
    return render_template("single.html")

@app.route("/<article>")
def articles(article):
    if article == 'single':
        return redirect(url_for('my_dog_missin'))
    return "404 Article Not Found"

if __name__ == '__main__':
    app.run()