from flask import Flask
from flask import render_template
from flask import request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    data = request.get_json(silent=True)

    login = data['login']
    password = data['password']

    client = MongoClient('localhost', 27017)
    db = client.mydb
    collection = db.users
    flag = collection.find_one({'login': login, 'pass': password})
    if flag == None:
        return render_template('registration.html')
    else:
        return render_template('hello.html', nickname=flag['name'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    data = request.get_json(silent=True)

    login = data['login']
    password = data['password']
    name = data['name']
    email = data['email']

    client = MongoClient('localhost', 27017)
    db = client.mydb
    collection = db.users
    collection.insert_one(data)

    return render_template('hello.html', nickname=name)