import os.path


def getMemory(account):
    current_path = os.path.dirname(__file__)
    lines = []
    if os.path.exists(current_path + "/../static/memories/memory_" + account + ".txt"):
        with open(current_path + "/../static/memories/memory_" + account + ".txt", "r", encoding="utf-8") as mem:
            lines = mem.readlines()
            print(lines)
            for i in range(0, len(lines)):
                lines[i] = lines[i].strip("\n")
        mem.close()
    else:
        os.mknod(current_path + "/../static/memories/memory_" + account + ".txt")
    return lines

def setMemory(account, memory):
    memories = getMemory(account)
    memories.append(memory['question'])
    memories.append(memory['answer'])
    if len(memories) > 10:
        memories.pop(0)
        memories.pop(0)
    memorymemory = ""
    for i in range(0, len(memories)):
        memorymemory += (memories[i] + "\n")
    current_path = os.path.dirname(__file__)
    mem = open(current_path + "/../static/memories/memory_" + account + ".txt", "w", encoding="utf-8")
    mem.write(memorymemory)
    mem.close()