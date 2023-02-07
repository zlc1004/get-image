from selenium import webdriver
import time
import config as cfg
import json
import v4_download_engine

class default_config_google():
    def __init__(self,task):
        self.task = task
        self.image_search_engine_link = r'https://www.google.com/search?q={}&tbm=isch'
        self.image_class = r'rg_i'
        self.nextpage_or_scrolldown = 1
        self.scrolldown_times = 5
        self.how_many_pages = 0
        self.next_page_css_or_xpath = 0
        self.next_page_css_selector = r''
        self.next_page_xpath = r''
        self.run_js_when_next_page = 0
        self.what_js = r''
        self.thread = 0
        self.chrome_driver_path = r'./chromedriver'
        self.save_path = r'./images'

class default_config_istock():
    def __init__(self,task):
        self.task = task
        self.image_search_engine_link = r'https://www.istockphoto.com/search/2/image?phrase={}'
        self.image_class = r'MosaicAsset-module__thumb___klD9E'
        self.nextpage_or_scrolldown = 0                     # 0:nextpage, 1:scrolldown
        self.scrolldown_times = 5
        self.how_many_pages = 3
        self.next_page_css_or_xpath = 0                     # 0:css, 1:xpath
        self.next_page_css_selector = r'.PaginationRow-module__nextButton___bTZ91'
        self.next_page_xpath = r''
        self.run_js_when_next_page = 0                     # 0:no, 1:yes
        self.what_js = r''
        self.thread = 0                                     # 0:no, 1:yes
        self.chrome_driver_path = r'./chromedriver'
        self.save_path = r'./images'

if cfg.use_default == 1:
    if cfg.default_engine == 'google':
        config = default_config_google(cfg.task)
    elif cfg.default_engine == 'istock':
        config = default_config_istock(cfg.task)
    else:
        print('default_engine error')
        exit()
else:
    config = cfg

config.task=list(set(config.task.split(',')))

######## debug ################ debug ################ debug ################ debug ################ debug ################ debug ########

# with open('./log.test', 'w') as f:
#     f.write(str(config.task))
# exit()

######## debug ################ debug ################ debug ################ debug ################ debug ################ debug ########

chrome = webdriver.Chrome()
try:
    tasks = config.task
    data = {}
    if config.nextpage_or_scrolldown == 1:
        for task in tasks:
            chrome.get(config.image_search_engine_link.format(task))
            for i in range(config.scrolldown_times):
                chrome.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
            time.sleep(3)
            out = chrome.execute_script('var json;var cn="'+config.image_class +
                                        '";(function () {var aaa = []; for (let i = 0; i < document.getElementsByClassName(cn).length; i++) {aaa.push(document.getElementsByClassName(cn)[i]["src"]);}; json = JSON.stringify(aaa); return json;})();return json;')
            # out=chrome.execute_script('return json')
            # chrome.e
            # print(out)
            with open("./log.log", 'a') as f:
                f.write(out)
            # exit()
            # out=out[1:-1]
            out = json.loads(out)
            data[task] = out
    elif config.nextpage_or_scrolldown == 0:
        for task in tasks:
            chrome.get(config.image_search_engine_link.format(task))
            time.sleep(5)
            data[task] = []
            for i in range(config.how_many_pages):
                out = chrome.execute_script('var json;var cn="'+config.image_class +
                                            '";(function () {var aaa = []; for (let i = 0; i < document.getElementsByClassName(cn).length; i++) {aaa.push(document.getElementsByClassName(cn)[i]["src"]);}; json = JSON.stringify(aaa); return json;})();return json;')
                with open("./log.log", 'a') as f:
                    f.write(out)
                # exit() ##  debug  ##:
                time.sleep(1)
                chrome.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                out = json.loads(out)
                data[task] += out
                if config.run_js_when_next_page:
                    chrome.execute_script(config.what_js)
                if config.next_page_css_or_xpath == 0:
                    chrome.find_element_by_css_selector(config.next_page_css_selector).click()
                elif config.next_page_css_or_xpath == 1:
                    chrome.find_element_by_xpath(config.next_page_css_selector).click()
    else:
        print("config.nextpage_or_scrolldown is not 0 or 1")
        chrome.close()
        exit()
    chrome.close()
    for k, v in data.items():
        v4_download_engine.mkdir(v4_download_engine.joinpath(config.save_path, k))
        for i_ in range(len(v)):
            i = v[i_]
            if config.thread:
                v4_download_engine.download_image_thread(i, v4_download_engine.joinpath(
                    config.save_path, k), "/"+k+'_'+str(i_+1)+'.jpg')
            else:
                v4_download_engine.download_image(i, v4_download_engine.joinpath(
                    config.save_path, k), "/"+k+'_'+str(i_+1)+'.jpg')
except Exception as e:
    with open("./err.log", 'a') as f:
        f.write("main err:"+(str(e).split('\n')[0]))
        f.write('\n')
finally:
    chrome.close()
