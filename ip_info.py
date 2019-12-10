import requests
from bs4 import BeautifulSoup

ip = input('ip: ')

resp = requests.get('https://ipinfo.io/' + ip,headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'})
soup = BeautifulSoup(resp.text,'html.parser')

print('########################################')
for i in soup.find_all('ul',class_="address-list")[0].find_all('li'):
    print(i.find_all('span')[0].get_text().strip() + ': ' + i.find_all('span')[1].get_text().strip())

print('/****************************************/')
for i in soup.find_all('ul',class_="address-list")[1].find_all('li'):
    print(i.find_all('span')[0].get_text().strip() + ': ' + i.find_all('span')[1].get_text().strip())

if 'There are 0 domain names hosted on this IP address.' in resp.text:
    print('########################################')
    quit()
else:
    print('/****************************************/')
    for i in soup.find_all('ul',class_="address-list")[2].find_all('li'):
        print('domain: ' + i.find_all('span')[0].a.get_text())

print('########################################')


