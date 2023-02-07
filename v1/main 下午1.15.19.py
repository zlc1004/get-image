#! python3
# exit()
import requests
import json as JSON
import os
import base64
import threading

json = {}

with open('./task/task') as f:
    readdata = f.read()
    # print(readdata)                                 /////////// debug ///////////
    if readdata == '':
        print('No task')
        exit()
    tasks = readdata.split(",")
# print(tasks)                                        /////////// debug ///////////
for taskindex in range(len(tasks)):
    tasks[taskindex] = tasks[taskindex].replace(" ", "-")

print("Tasks:", ",".join(tasks))
# print(tasks)                                        /////////// debug ///////////
# exit()                                              /////////// debug ///////////

for i in tasks:
    with open('./task/data/'+i) as f:
        infile = f.read()
        if infile.startswith("'") and infile.endswith("'"):
            infile = infile[1:-1]
        datajson = JSON.loads(infile)
    json[i] = datajson
def func___(imageurl,data,k,path,imageurli):
    if imageurl.startswith("data:image/png;base64,"):
        print("base64 decodeing number:", imageurli +
                1, " of ", len(data), " in ", k)
        imageurl = imageurl.replace("data:image/png;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl == "":
        return
    elif imageurl.startswith("data:image/jpeg;base64,"):
        print("base64 decodeing number:", imageurli +
                1, " of ", len(data), " in ", k)
        imageurl = imageurl.replace("data:image/jpeg;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/jpg;base64,"):
        print("base64 decodeing number:", imageurli +
                1, " of ", len(data), " in ", k)
        imageurl = imageurl.replace("data:image/jpg;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/gif;base64,"):
        print("base64 decodeing number:", imageurli +
                1, " of ", len(data), " in ", k)
        imageurl = imageurl.replace("data:image/gif;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/bmp;base64,"):
        print("base64 decodeing number:", imageurli +
                1, " of ", len(data), " in ", k)
        imageurl = imageurl.replace("data:image/bmp;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/webp;base64,"):
        print("base64 decodeing number:", imageurli +
                1, " of ", len(data), " in ", k)
        imageurl = imageurl.replace("data:image/webp;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/svg+xml;base64,"):
        print("base64 decodeing number:", imageurli +
                1, " of ", len(data), " in ", k)
        imageurl = imageurl.replace("data:image/svg+xml;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/tiff;base64,"):
        print("base64 decodeing number:", imageurli +
                1, " of ", len(data), " in ", k)
        imageurl = imageurl.replace("data:image/tiff;base64,", "")
        r = base64.b64decode(imageurl)
    else:
        print("downloading image number ", imageurli +
                1, " of ", len(data), " in ", k)
        r = requests.get(imageurl).content
    with open('./images/' + path + str(imageurli+1) + ".jpg", 'wb') as f:
        f.write(r)
for k, v in json.items():
    print("downloading:", k)
    path = k.replace("-", " ")+'/'
    os.system('mkdir -p "' + './images/' + path + '"')
    data = v
    for imageurli in range(len(data)):
        imageurl = data[imageurli]
        func___(imageurl,data,k,path,imageurli)
print("Done!")
