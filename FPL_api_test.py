import requests
import pandas as pd
import numpy as np
import json

pd.options.mode.chained_assignment = None  # default='warn' # Removes Settingwithcopywarning

# Getting FPL API keys by converting them to json
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
data = r.json()

with open("data.json", "w") as FPL_data:
    json.dump(data, FPL_data, indent=4)



