from flask import Flask, render_template, request
from flask import url_for
import pymysql


application = app = Flask(__name__)


#Database utenti finto 
users = {"admin": "password", "andrea": "Masterxbox"}

def show_the_login_form():
    return render_template('login.html')
    
def do_the_login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password: 
        return render_template('benvenuto.html', username=username)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    return "<p> Hello World!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/username')
def profile(username):
    return f'{username}\'s profile'

'''
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
'''

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000) # Avvia l'applicazione Flask