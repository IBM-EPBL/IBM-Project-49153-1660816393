  from flask import Flask
  from flask_db2 import DB2
  from flask import Flask, render_template, request, redirect, url_for, session

  app = Flask(__name__)

  app.config['DB2_DATABASE'] = 'flask'
  app.config['DB2_HOSTNAME'] = 'localhost'
  app.config['DB2_PORT'] = 3000
  app.config['DB2_PROTOCOL'] = 'TCPIP'
  app.config['DB2_USER'] = 'ajisha'
  app.config['DB2_PASSWORD'] = 'ajisha'

  db = DB2(app)



  @app.route('/login/logout')
  def logout():
      # Remove session data, this will log the user out
      session.pop('loggedin', None)
      session.pop('id', None)
      session.pop('username', None)
      # Redirect to login page
      return redirect(url_for('login'))

      @app.route("/")
  def hello_world():
      return render_template('home.html', name="Home")

  @app.route("/about")
  def about():
    return render_template('about.html', name="About")


  @app.route("/login")
  def login():
    return render_template('login.html', name="Login")

  @app.route("/register")
  def register():
    return render_template('register.html', name="Register")