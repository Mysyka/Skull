import requests
hostname = '10.200.8.'
i = '200'

hostname = hostname+i
i = 'i+1'

host = 'http://hostname'
# hostname = "google.com"  # example
response = requests.get(host).status_code

# and then check the response...
#if response == 0:
#    print(hostname, 'is up!')

#else:
#    print(hostname, 'is down!')
