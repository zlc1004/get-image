import json as JSON
import os
import threading
import v3

with open("./task.json") as f:
    json = JSON.load(f)

config=json["config"]
datas=json["data"]
for data in datas:
    folder_name=data["folder-name"]
    key_word=data["key-word"]
    end_page=data["end-page"]
    ###########################
    path="./images/"+folder_name+"/"
    os.system('mkdir -p "'+path+'"')
    ###########################
    if config["thread"]=="true":
        threading.Thread(target=v3.main,args=(path,key_word,end_page)).start()
    else:
        v3.main(key_word,end_page,path)