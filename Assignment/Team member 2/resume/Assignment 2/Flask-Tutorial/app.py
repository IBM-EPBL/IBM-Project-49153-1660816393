from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/blog")
def blog():
   return render_template('blog.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/signin')
def signin():
   return render_template('signin.html')
   