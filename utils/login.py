from utils.database import database, UserModel
from utils import token

def login(account, password, db):
    # 2. Get model
    User = UserModel.createUsers(db)
    results = database.queryData(Model=User, type="user", user={"account": account, "password": password})
    if results != None:
        token_g = token.generate_token(account, 1)
        return {
            "token": token_g,
            "status": True
        }
    else:
        return {
            "status": False
        }