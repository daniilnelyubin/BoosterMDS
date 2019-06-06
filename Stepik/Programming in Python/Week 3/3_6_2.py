import requests
url = "https://stepic.org/media/attachments/course67/3.6.3/"
add = "699991.txt"
while True:
    get = requests.get(url+add)
    text = get.text.split()
    if text[0]=="We":
        print("Last file: "+get.text)
        break
    else:
        add = text[0]
    print(get.text)