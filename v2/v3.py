import re
import threading
import urllib
import os
import requests


def get_onepage_urls(onepageurl):
    if not onepageurl:
        print('已到最后一页, 结束')
        return [], ''
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        fanye_url = ''
        return pic_urls, fanye_url
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    fanye_urls = re.findall(re.compile(
        r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)
    fanye_url = 'http://image.baidu.com' + fanye_urls[0] if fanye_urls else ''
    return pic_urls, fanye_url


# save_dir = "./image"
def down_pic(pic_urls, path):
    for i, pic_url in enumerate(pic_urls):
        threading.Thread(target=downloadone, args=(pic_url, i, path)).start()


def downloadone(pic_url, i, save_dir):
    try:
        pic = requests.get(pic_url, timeout=15)
        string = os.path.join(save_dir, (str(i + 1) + '.jpg'))
        with open(string, 'wb') as f:
            f.write(pic.content)
            print('成功下载第%s张图片' % str(i + 1))
    except Exception as e:
        print('下载第%s张图片时失败' % str(i + 1))
        print(e)


def main(path, keyword, howmuch):
    print("下载:", keyword)
    print("下载页数:", howmuch)
    print("保存路径:", path)
    url_init_first = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='
    url_init = url_init_first + urllib.parse.quote(keyword, safe='/')
    all_pic_urls = []
    onepage_urls, fanye_url = get_onepage_urls(url_init)
    all_pic_urls.extend(onepage_urls)
    fanye_count = 0
    while 1:
        onepage_urls, fanye_url = get_onepage_urls(fanye_url)
        fanye_count += 1
        print('第%s页' % fanye_count)
        if fanye_count == howmuch:
            break
        if fanye_url == '' and onepage_urls == []:
            break
        all_pic_urls.extend(onepage_urls)
    down_pic(list(set(all_pic_urls)), path)
