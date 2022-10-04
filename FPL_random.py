# To do:
    # Reformat current players table

import requests
import pandas as pd
import numpy as np
import getpass
import json

pd.options.mode.chained_assignment = None  # default='warn' # Removes Settingwithcopywarning

# Getting FPL API keys by converting them to json
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
database = r.json()
database.keys()
# Create dataframes for elements (players), element_types(positions) and teams
elements_df = pd.DataFrame(database['elements'])
elements_types_df = pd.DataFrame(database['element_types'])
teams_df = pd.DataFrame(database['teams'])
# Element_
player_names_df = elements_df
player_names_df['position'] = player_names_df.element_type.map(elements_types_df.set_index('id').singular_name)
player_names_df['team'] = player_names_df.team.map(teams_df.set_index('id').name)
player_names_df = elements_df[['id', 'first_name', 'second_name', 'web_name', 'position', 'team', 'total_points', 'now_cost']]

def main():
    current_team = login()
    yes = input_team(current_team)
    print(yes)
    

    # with open("data_t.json", "w") as FPL_data:
    #     json.dump(current_team, FPL_data, indent=2)
    
    # team = generate_team(elements_df, elements_types_df, teams_df) # Remember to assign variables to outputs in main function
    # print(team)

def login():
    # email = input("Email: ")
    # team_id = input("Team ID: ")
    s = requests.Session() # requests.Session() must be kept as s for some reason

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
        "password": "HanWe1FPL.", 
        "app": "plfpl-web", 
        "redirect_uri": "https://fantasy.premierleague.com/"
    }

    url = "https://users.premierleague.com/accounts/login/"

    res = s.post(url, data = data,  headers = headers)

    team_url = "https://fantasy.premierleague.com/api/my-team/8095706/"
    res = s.get(team_url)
    current_team = res.json()
    
    return current_team
    
def input_team(current_team):
    # Create empty dataframe
    current_players_df = pd.DataFrame()
    # For each dictionary in list 'picks', find player in player_names.df and append data
    # current_players_df
    for i in current_team['picks']:
        player = player_names_df.loc[player_names_df.id == i['element']]
        current_players_df = pd.concat([current_players_df, player])
    
    return current_players_df

# def generate_transfer():



def generate_team(elements_df, elements_types_df, teams_df):
    # Create DataFrames from data. Elements = players, element_type = position
    # Get databases for each position
    player_names_df = elements_df[['first_name','second_name','web_name','element_type','team', 'total_points', 'now_cost']]
    player_names_df['position'] = player_names_df.element_type.map(elements_types_df.set_index('id').singular_name)
    player_names_df['team'] = player_names_df.team.map(teams_df.set_index('id').name)

    gk_names_df = player_names_df.loc[player_names_df.position =='Goalkeeper']
    def_names_df = player_names_df.loc[player_names_df.position =='Defender']
    mid_names_df = player_names_df.loc[player_names_df.position =='Midfielder']
    for_names_df = player_names_df.loc[player_names_df.position =='Forward']

    # Randomly generate team by position
    team_gk = gk_names_df.sample(n=2)
    team_def = def_names_df.sample(n=5)
    team_mid = mid_names_df.sample(n=5)
    team_for = for_names_df.sample(n=3)
    team = pd.concat([team_gk, team_def, team_mid, team_for])
    
    return team
# while team_df['now_cost'].sum() >= 1000:
#     team_gk = gk_names_df.sample(n=2)
#     team_def = def_names_df.sample(n=5)
#     team_mid = mid_names_df.sample(n=5)
#     team_for = for_names_df.sample(n=3)
#     team_df = pd.concat([team_gk, team_def, team_mid, team_for])

# def gameweek():
#     pd.DataFrame(json['elements'])


# def check_budget():
    

# print(team_df['now_cost'].sum())

# print(team_df)

if __name__ == "__main__":
    main()