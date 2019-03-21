import json
import threading
import urllib
import urllib.request
import os


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

def downloadImage(title, url, num):
    try:
        mkdir('./comic/' + title)
        urllib.request.urlretrieve(url,'./comic/' + title + '/' + str(num).zfill(2) + '.jpg')
    except Exception as e:
        print(e)
        print('error: try again')
        return downloadImage(title, url, num)

with open('./opurls.json', encoding='utf-8') as f:
    urlsjson = f.read()
    urlsdistlist = json.loads(urlsjson)
    
    for ep in urlsdistlist:
        title = ep['title']
        urls = ep['urls']
        threads = []
        num = 1
        for url in urls:
            t = threading.Thread(target = downloadImage, args = (title, url, num))
            threads.append(t)
            num = num + 1
        for th in threads:
            th.start()
            th.join()
            while True:
                if (len(threading.enumerate()) < 3):
                    break

    f.close()