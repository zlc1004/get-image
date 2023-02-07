from selenium import webdriver
import time
import config
import json,v4_download_engine

chrome=webdriver.Chrome(config.chrome_driver_path)
tasks=config.task.split(',')
data={}
for task in tasks:
    chrome.get("https://www.google.com/search?tbm=isch&q="+task)
    for i in range(5):
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    time.sleep(3)
    out=chrome.execute_script('var json;var cn="rg_i";(function () {var aaa = []; for (let i = 0; i < document.getElementsByClassName(cn).length; i++) {aaa.push(document.getElementsByClassName(cn)[i]["src"]);}; json = JSON.stringify(aaa); return json;})();return json;')
    # out=chrome.execute_script('return json')
    # chrome.e
    # print(out)
    with open("./log.log",'w') as f:
        f.write(out)
    # exit()
    # out=out[1:-1]
    out=json.loads(out)
    data[task]=out
chrome.close()

for k,v in data.items():
    v4_download_engine.mkdir(v4_download_engine.joinpath(config.save_path,k))
    for i_ in range(len(v)):
        i=v[i_]
        if config.thread:
            v4_download_engine.download_image_thread(i, v4_download_engine.joinpath(
                config.save_path, k), "/"+k+'_'+str(i_+1)+'.jpg')
        else:
            v4_download_engine.download_image(i, v4_download_engine.joinpath(
                config.save_path, k), "/"+k+'_'+str(i_+1)+'.jpg')
