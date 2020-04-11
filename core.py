from helper import get_proxy_list
import threading
import requests
import random

TEST_SITES = [
    'https://www.python.org/',
    'https://www.kaggle.com/',
    'https://github.com/',
]

proxy_list = get_proxy_list()
active_proxy_list = []


def check_proxy(proxy, protocol):
    url = random.choice(TEST_SITES)
    try:
        r = requests.head(url, proxies={protocol: proxy})
        if r.status_code == 200:
            active_proxy_list.append([proxy, protocol])
        return
    except:
        return

def get_free_https_proxies():

    threads = []

    for item in proxy_list:
        ip = item[0]
        port = item[1]
        https = item[3]

        if https == 'yes' or https == 'Yes':
            t = threading.Thread(target=check_proxy, args=[f'{ip}:{port}', 'https'])
            t.start()
            threads.append(t)

    for thread in threads:
        thread.join(timeout=5)

get_free_https_proxies()