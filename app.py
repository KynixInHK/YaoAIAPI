# -*- coding: utf-8 -*-
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import paddlehub as hub
from utils import yuan, memory, login
from utils.database import database
from utils.token import verify_token

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

# Connect
db = database.connect(app)

simnet_bow = hub.Module(name="simnet_bow")

@app.route('/')
def hello_world():  # put application's code here
    return "Hello World"

@app.post('/answer')
def getAnswer():
    data = request.data
    data_json = json.loads(data)
    token = request.headers.get("Authorization")
    print(token)
    verify = verify_token(token)
    result = {
        "code": 0,
        "reply": ""
    }
    if verify[1]["status"]:
        account = verify[0]["name"]
        result["reply"] = yuan.communicateWithYuan(data_json, account)
    else:
        print(verify[1]["msg"])
        result["code"] = 1
        result["reply"] = "Token wrong!"
    return result

@app.route('/yao')
def helloYao():
    message = {
        "simplifiedChinese": "2022年12月24日，普萘洛尔生态人工智能伙伴“苏乐瑶”进入开发周期。",
        "traditionalChinese": "2022年12月24日，普萘洛爾生態人工智能夥伴“蘇樂瑤”進入開發週期。",
        "English": 'On December 24, 2022, Propranolol AI partner "Yuki" entered the development cycle.',
        "Russian": "24 декабря 2022 года в цикл разработки вступил партнер по экологическому искусственному интеллекту пропранолола «Yuki».",
        "Japanese": "2022 年 12 月 24 日、プロプラノロールの生態系人工知能パートナー「ユキ」が開発サイクルに入りました。",
        "Korean": '2022년 12월 24일, 프로프라놀롤 생태 인공지능 파트너인 "Yuki"가 개발 주기에 들어갔습니다.'
    }
    return message

@app.post('/login')
def loginP():
    data = request.data
    data_json = json.loads(data)
    result = login.login(data_json["account"], data_json["password"], db)
    if result["status"]:
        return {
            "msg": "Login successfully!",
            "token": result["token"],
            "code": 0
        }
    else:
        return {
            "msg": "Login failed!",
            "code": 1
        }

if __name__ == '__main__':
    app.run()
