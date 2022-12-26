import paddlehub as hub
from utils import readFiles
simnet_bow = hub.Module(name="simnet_bow")

def getPrompts(data_json):
    questions = readFiles.readFiles("q")
    answers = readFiles.readFiles("a")
    reqs = []
    for i in range(0, len(questions)):
        reqs.append(data_json["question"])
    inputs = {
        "text_1": reqs,
        "text_2": questions
    }
    results = simnet_bow.similarity(data=inputs, batch_size=2)
    results.sort(key=lambda k: (k.get('similarity')), reverse=True)
    prompts = []
    for i in range(0, len(results)):
        if(results[i]['similarity'] <= 0.8):
            break
        prompts.append({
            "question": results[i]['text_2'],
            "answer": answers[results[i]['text_2']]
        })

    return prompts