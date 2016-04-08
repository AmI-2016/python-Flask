
from flask import Flask, url_for, render_template, request, session, redirect
import datetime


app = Flask(__name__)
app.secret_key = "this is really secret, yeah!223"


@app.route('/')
def hello_world():
    # if no address is given, redirect to the index page
    return redirect(url_for('index'))

@app.route('/index.html')
def index():
    year = datetime.datetime.now().year # find current year
    return render_template('index.html', copy_year=year)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/login.html', methods=['POST'])
def login():
    # extract user data from the FORM
    # note: tu use request.form, the request MUST use the method POST
    # see: http://flask.pocoo.org/docs/0.10/quickstart/#the-request-object
    #      (To access parameters submitted in the URL (?key=value) you can use the args attribute)
    user = request.form['user']

    # initialize the session
    session['user'] = user
    session['valid'] = True

    return render_template('login.html', user=user)

@app.route('/logout.html')
def logout():
    # destroy the session information
    session['user']=""
    session['valid'] = False
    # back to the home page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
