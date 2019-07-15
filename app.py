from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/search', methods=["POST"])
def do_search():
    print(request.form)
    # use request.form.url to search wikipedia
    # then kick off crawl
    return request.form['url']