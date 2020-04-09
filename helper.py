from bs4 import BeautifulSoup
import requests

URLs = [
    'https://free-proxy-list.net/',
    'https://www.us-proxy.org/',
    'https://www.socks-proxy.net/',
    'https://free-proxy-list.net/uk-proxy.html',
    'https://www.sslproxies.org/',

]

def get_proxies_from_free_proxy_list(url):
    proxy_domain = url
    r = requests.get(proxy_domain)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id='proxylisttable')

    proxy_list = []

    for row in table.find_all('tr'):
        column = row.find_all('td')
        try:
            proxy_ip = column[0].get_text()
            proxy_port = column[1].get_text()
            proxy_code = column[2].get_text()
            proxy_is_secure = column[6].get_text()
            proxy_list.append([proxy_ip, proxy_port, proxy_code, proxy_is_secure])
        except IndexError:
            pass

    return proxy_list

def get_proxy_list():
    proxies = []

    for url in URLs:
        for proxy in get_proxies_from_free_proxy_list(url):
            proxies.append(proxy)
    return proxies
