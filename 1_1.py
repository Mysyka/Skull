import requests

import urllib3
urllib3.disable_warnings()

urls = ['http://yandex.ru', 'http://google.ru', 'http://mail.ru',
       'http://rbc.ru', 'http://rambler.ru', 'http://yahoo.com', 'http://megafon.ru']
for i in urls:
    for n in range(2):
        a = requests.get(i, verify=False).status_code
        if a!=200:
            print(a)