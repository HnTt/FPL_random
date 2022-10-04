import getpass
import requests
import json

def login():
    # email = input("Email: ")
    pword = getpass.getpass()
    # team_id = input("Team ID: ")
    s = requests.session()

    headers = {
    'authority': 'users.premierleague.com' ,
    'cache-control': 'max-age=0' ,
    'upgrade-insecure-requests': '1' ,
    'origin': 'https://fantasy.premierleague.com' ,
    'content-type': 'application/x-www-form-urlencoded' ,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' ,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
    'sec-fetch-site': 'same-site' ,
    'sec-fetch-mode': 'navigate' ,
    'sec-fetch-user': '?1' ,
    'sec-fetch-dest': 'document' ,
    'referer': 'https://fantasy.premierleague.com/my-team' ,
    'accept-language': 'en-US,en;q=0.9,he;q=0.8' ,
    }

    data = {
        "login": "teitnah@gmail.com", 
        "password": pword, 
        "app": "plfpl-web", 
        "redirect_uri": "https://fantasy.premierleague.com/"
    }

    url = "https://users.premierleague.com/accounts/login/"

    res = s.post(url, data = data,  headers = headers)

    team_url = "https://fantasy.premierleague.com/api/my-team/8095706/"
    res = s.get(team_url)
    team_data = res.json()
    with open("data_team.json", "w") as FPL_data:
        json.dump(team_data, FPL_data, indent=4)

login()
