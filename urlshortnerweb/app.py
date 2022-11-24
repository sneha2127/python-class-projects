from flask import Flask,render_template,request
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    # return "Hello,world!"
    short_url = ""
    if request.method == "POST":
        url_link = request.form['url']
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url_link)
    return render_template('index.html',short_url_link = short_url)


@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET"])
def contact():
    return render_template('contact_page.html')

@app.route('/service', methods=["GET"])
def service():
    return render_template('service.html')

if __name__ == "__main__":
    app.run(debug = True)