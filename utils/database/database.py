import os.path
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_


def connect(app):
    current_path = os.path.dirname(__file__)
    url = ""
    port = ""
    user = ""
    password = ""
    database = ""
    with open(current_path + "/../../static/database.json", "r", encoding="utf-8") as fp:
        data = json.load(fp)
        url = data["url"]
        port = data["port"]
        user = data["user"]
        password = data["password"]
        database = data["database"]
    fp.close()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + user + ':' + password + '@' + url + ':' + port + '/' + database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db = SQLAlchemy(app)
    return db

def addData(data, db):
    if type(data) == list:
        db.session.add_all(data)
    else:
        db.session.add(data)
    db.session.commit()
    return "success"

def queryData(Model, type, user):
    results = None
    if type == "all":
        results = Model.query.all()
    elif type == "user":
        results = Model.query.filter(and_(Model.account == user['account'], Model.password == user['password'])).all()
    return results

def updateData(db,Model, update, filter, type):
    if type == "user":
        Model.query.filter(Model.account == filter).update({"password": update})
        db.session.commit()
    return "success"

def deleteData(db, Model, filter, type):
    if type == "user":
        Model.query.filter(Model.account == filter).delete()
        db.session.commit()
    return "success"