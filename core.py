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

def check_proxy(proxy, protocol):
    url = random.choice(TEST_SITES)
    try:
        r = requests.head(url, proxies={protocol: proxy})
        print(f'r.status_code   {r.status_code}')
        if r.status_code == 200:
            return True
        return
    except:
        return

active_proxy_list = []
counter = 0
for item in proxy_list:
    ip = item[0]
    port = item[1]
    https = item[3]

    if https == 'yes' or 'Yes':
        counter +=1
        if check_proxy(f'{ip}:{port}', 'https'):
            active_proxy_list.append(item)



print(len(proxy_list))
print(counter)