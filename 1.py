import requests

urls = {'url0': 'http://yandex.ru',
        'url1': 'http://google.ru',
        'url2': 'http://mail.ru',
        'url3': 'http://rbc.ru',
        'url4': 'http://rambler.ru',
        'url5': 'http://yahoo.com'}

for i in range(100):
    print(
    requests.get(urls['url0']).status_code,'\n',
    requests.get(urls['url1']).status_code,'\n',
    requests.get(urls['url2']).status_code,'\n',
    requests.get(urls['url3']).status_code,'\n',
    requests.get(urls['url4']).status_code,'\n',
    requests.get(urls['url5']).status_code
    )


print(requests.get('http://yandex.ru').status_code)
#get_stat = requests.get(url['url0']).status_code

#r = requests.get(url0)
#k = requests.get('http://google.ru')
#c = requests.get('http://mail.ru')
#f = requests.get('http://rbc.ru')
#l = requests.get('http://rambler.ru')
#p = requests.get('http://yahoo.com')


