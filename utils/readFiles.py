import os
def readFiles(type):
    current_path = os.path.dirname(__file__)
    prompts = open(current_path + '/../static/prompts.txt', "r")
    lines = prompts.readlines()
    result = []
    if type == "q":
        questions = []
        for i in range(0, len(lines), 2):
            # if(i % 2 == 0):
            line = lines[i].rstrip('\n')
            questions.append(line)
        result = questions
    elif type == "a":
        answers = {}
        for i in range(0, len(lines), 2):
            answers[lines[i].rstrip('\n')] = lines[i + 1].rstrip('\n')
        result = answers
    prompts.close()
    return result