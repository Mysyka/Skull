import requests

urls = ['http://yandex.ru', 'http://google.ru', 'http://mail.ru',
       'http://rbc.ru', 'http://rambler.ru', 'http://yahoo.com', 'http://megafon.ru']
for i in urls:
    for n in range(101):
        a = requests.get(i).status_code
        if a!=200:
            print(a)