import urllib.request

url = input("Enter url:")

response = urllib.request.urlopen(url)
headers = response.getheaders()

for header in headers:
    print(header)
