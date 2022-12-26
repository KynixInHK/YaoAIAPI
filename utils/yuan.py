import os
import sys
import json
sys.path.append(os.path.abspath(os.curdir))

from yuan_api.inspurai import Yuan, set_yuan_account,Example
from utils import similarity
from utils.memory import setMemory, getMemory
def communicateWithYuan(data_json, account):
    # 0. read the account and phone number
    current_path = os.path.dirname(__file__)
    account = ""
    phone = ""
    with open(current_path + '/../static/account.json', "r", encoding = 'utf-8') as fp:
        data = json.load(fp)
        account = data['account']
        phone = data['phone']
    fp.close()

    # 1. set account
    set_yuan_account(account, phone)  # 输入您申请的账号和手机号

    # 2. initiate yuan api
    # 注意：engine必需是['base_10B','translate','dialog','rhythm_poems']之一，'base_10B'是基础模型，'translate'是翻译模型，'dialog'是对话模型，'rhythm_poems'是古文模型
    yuan = Yuan(engine='dialog',
                input_prefix="问：“",
                input_suffix="”",
                output_prefix="答：“",
                output_suffix="”",
                append_output_prefix_to_query=True,
                topK=5,
                temperature=1,
                topP=0.8,
                frequencyPenalty=1.2)
    prompts = similarity.getPrompts(data_json)
    for i in range(0, len(prompts)):
        yuan.add_example(Example(inp=prompts[i]['question'],
                                 out=prompts[i]['answer']))
    lines = getMemory(account)
    if len(lines) != 0:
        for i in range(0, len(lines), 2):
            yuan.add_example(Example(inp=lines[i],
                                     out=lines[i + 1]))
    response = yuan.submit_API(prompt=data_json['question'], trun="”")
    memorySet = {
        "question": data_json['question'],
        "answer": response
    }
    setMemory(account, memorySet)
    return response