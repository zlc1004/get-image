import threading
import requests
import os
import base64

def download_image(imageurl,path,file_name):
    r=None
    if imageurl.startswith("data:image/png;base64,"):
        imageurl = imageurl.replace("data:image/png;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl == "":
        return
    elif imageurl.startswith("data:image/jpeg;base64,"):
        imageurl = imageurl.replace("data:image/jpeg;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/jpg;base64,"):
        imageurl = imageurl.replace("data:image/jpg;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/gif;base64,"):
        imageurl = imageurl.replace("data:image/gif;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/bmp;base64,"):
        imageurl = imageurl.replace("data:image/bmp;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/webp;base64,"):
        imageurl = imageurl.replace("data:image/webp;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/svg+xml;base64,"):
        imageurl = imageurl.replace("data:image/svg+xml;base64,", "")
        r = base64.b64decode(imageurl)
    elif imageurl.startswith("data:image/tiff;base64,"):
        imageurl = imageurl.replace("data:image/tiff;base64,", "")
        r = base64.b64decode(imageurl)
    else:
        r = requests.get(imageurl).content
    with open(path + file_name, 'wb') as f:
        f.write(r)

def download_image_thread(url,save_path,file_name):
    t = threading.Thread(target=download_image, args=(url,save_path,file_name))
    t.start()
    return t

def get_website_source_code(url):
    resp = requests.get(url).text
    return resp

def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.system('mkdir "'+path+'"')
        return True
    else:
        return False

def joinpath(path1,path2):
    return os.path.join(path1,path2)