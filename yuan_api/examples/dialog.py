import os
import sys
sys.path.append(os.path.abspath(os.curdir))

from yuan_api.inspurai import Yuan, set_yuan_account,Example

# 1. set account
set_yuan_account("KynixInHK", "13696381199")  # 输入您申请的账号和手机号

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

# 3. add examples if in need.
yuan.add_example(Example(inp="你喜欢什么样的人类？",
                        out="我喜欢你这样的啊！"))
yuan.add_example(Example(inp="你能做些什么？",
                         out="我可以给你讲故事，还能陪你一起玩。"))
yuan.add_example(Example(inp="你会一直陪着我吗？",
                         out="当然了，我会一直一直陪着你的。"))
yuan.add_example(Example(inp="你是谁啊？",
                         out="我叫小源，是你的AI智能伙伴！"))

print("====夸夸机器人====")

while(1):
    print("输入Q退出")
    prompt = input("我：")
    if prompt.lower() == "q":
        break
    response = yuan.submit_API(prompt=prompt,trun="”")
    print(response+"”")
