import time
import jwt
import jwt.exceptions as exceptions

def generate_token(account, user_id):
    payload = {
        "name": account,
        "role": "user",
        "user_id": user_id,
        "exp": int(time.time() + 86400)
    }
    token = jwt.encode(payload=payload, key="il0veyOuyUki", algorithm='HS256')
    return token

def verify_token(token):
    payload = None
    result = {
        "status": True,
        "msg": "Token is verified successfully!",
        "account": ""
    }
    try:
        payload = jwt.decode(jwt=token, key="il0veyOuyUki", algorithms=['HS256'])
    except exceptions.ExpiredSignatureError:
        result["status"] = False
        result["msg"] = "Token expired!"
    except jwt.DecodeError:
        result["status"] = False
        result["msg"] = "Wrong!"
    except jwt.InvalidTokenError:
        result["status"] = False
        result["msg"] = "Invalid token error!"
    return payload, result