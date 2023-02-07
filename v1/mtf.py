with open('./task/task') as f:
    readdata = f.read()
    # print(readdata)                                 /////////// debug ///////////
    if readdata == '':
        print('No task')
        exit()
    tasks = readdata.split(",")

for i in tasks:
    with open('./task/data/'+i,"w") as f:
        f.write("")