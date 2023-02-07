import re
with open(r"./config", "r") as f:
    tmpconfig = f.readlines()
out, isdata, config = "", 0, []
for i in tmpconfig:
    if i.startswith(";"):
        continue
    if i == "\n":
        continue
    config.append(i.strip())
for index in range(len(config)):
    if config[index] == "pass":
        config[index] = ""
    elif config[index] == "yes":
        config[index] = "1"
    elif config[index] == "no":
        config[index] = "0"
    elif config[index] == "none":
        config[index] = ""
    elif config[index] == "css":
        config[index] = "1"
    elif config[index] == "xpath":
        config[index] = "0"
    elif config[index] == "nextpage":
        config[index] = "0"
    elif config[index] == "scrolldown":
        config[index] = "1"
for i in config:
    if i == "":
        out += '""\n'
        continue
    if i[0] == "[":
        isdata = 1
        out += i[1:-1] + "="
        continue
    if isdata == 1:
        if i.isnumeric():
            out += i + "\n"
            continue
        out += 'r"' + i + '"' + "\n"
        isdata = 0
        continue
    if i == "{task}":
        break
taskindex = config.index("{task}")
tasks = config[taskindex + 1 :]
out += 'task="' + ",".join(tasks) + '"\n'
with open(r"./config.py", "w") as f:
    f.write(out)
