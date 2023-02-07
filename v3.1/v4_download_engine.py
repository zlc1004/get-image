import threading
import requests
import os
import base64


def download_image(imageurl, path, file_name):
    try:
        r = None
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
    except Exception as e:
        with open("./err.log", "a") as f:
            f.write("err in download_image:"+str(e))
            f.write("\n")


def download_image_thread(url, save_path, file_name):
    t = threading.Thread(target=download_image,
                         args=(url, save_path, file_name))
    t.start()
    return t


def get_website_source_code(url):
    try:
        resp = requests.get(url).text
        return resp
    except Exception as e:
        with open("./err.log", "a") as f:
            f.write("err in get_website_source_code:"+(str(e).split("\n")[-1]))
            f.write("\n")


def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.system('mkdir "'+path+'"')
        return True
    else:
        return False


def joinpath(path1, path2):
    return os.path.join(path1, path2)


def main():
    def err1():
        err2()

    def err2():
        err3()

    def err3():
        err4()

    def err4():
        err5()

    def err5():
        err6()

    def err6():
        requests.get("https://www..com").raise_for_status()
    try:
        err1()
    except Exception as e:
        with open("./err.log", "a") as f:
            f.write("error test in v4_download_engine:" +
                    (str(e).split("\n")[-1]))
            f.write("\n")


if __name__ == '__main__':
    main()
