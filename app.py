from flask import Flask,render_template,request,url_for







app = Flask(__name__)








@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact-us")
def contact():
    return render_template('contact-us.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/forget-password")
def forget():
    return render_template('forget.html')












if __name__ == "__main__":
    app.run(debug=True)