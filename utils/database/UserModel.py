def createUsers(db):
    class Users(db.Model):
        __tablename__ = 'Users'
        id = db.Column(db.Integer, primary_key=True)
        account = db.Column(db.String(255))
        password = db.Column(db.String(255))
    return Users