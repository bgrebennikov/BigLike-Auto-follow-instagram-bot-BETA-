from InstagramAPI import InstagramAPI
from bs4 import BeautifulSoup
import requests
import time
import os

InstaApi = InstagramAPI("bgrebennikovv", "2135135186")
InstaApi.login()


def get_user_id(username):
    InstaApi.searchUsername(username)
    user_id = InstaApi.LastJson["user"]["pk"]
    return user_id


def get_self_info():
    InstaApi.getSelfUsernameInfo()
    info = InstaApi.LastJson['user']
    return info


home_url = "http://biglike.org/"
login_url = "http://biglike.org/login.php"

instagram_url = "https://www.instagram.com/bgrebennikovv/"

session = requests.Session()

data = {"linkinsta": instagram_url,
        "type": "instalog"}
sendData = session.post(login_url, data)
res = sendData.json()
phrase = res['response']['phrase']

attention = input("'" + phrase + "'")

data = {"instchkcom": "true"}
sendData = session.post(login_url, data)
res = sendData.json()['response']['type']
if res == "ok":
    print("Success! Code: " + res)
else:
    print("Error, code: " + res)


def startMember():
    while True:
        os.system("cls")

        page = session.get("http://biglike.org/instasub/").text
        soup = BeautifulSoup(page, 'html.parser')
        try:
            id = soup.find('div', {'class': 'p-10'}).get('id')
        except:
            return False
        aLink = soup.find('div', {'class': 'p-10'})
        onclick = aLink.find('a').get('onclick')
        splitOnclick = str(onclick).split('"')
        iLink = splitOnclick[3]

        points = soup.find('font', {'id': 'points'}).text

        uname = iLink.split("/")[3]
        try:
            uId = get_user_id(uname)
        except:
            session.get("http://biglike.org/ajax.php?divid=1&taskid="+id+"&task=instasub")
            return False

        InstaApi.follow(uId)
        print("follow: " + uname)
        check_url = "http://biglike.org/ajax.php?divid=" + id + "&taskid=" + id + "&task=instasub"
        check = session.get(check_url)
        print("Points: " + points)

        time.sleep(121)

while True:
    if startMember() == False:
        print(startMember())
        time.sleep(5)
