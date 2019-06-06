import requests
url = "https://stepic.org/media/attachments/course67/3.6.2/895.txt"
get = requests.get(url=url)

print(len(get.text.splitlines()))


