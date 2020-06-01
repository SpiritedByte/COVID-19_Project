import requests
import os
import traceback
import sys
from pathlib import Path

url_cases = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv'
url_deaths = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-deaths_latest.csv'

##################################

# create new folder to store the statistics
def getStats():
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = Path("stats/")
    path_to_stats = cwd / path
    #print(path_to_stats)

    if not os.path.exists(path_to_stats):
        os.makedirs(path_to_stats)
    else:
        pass
    
    print("Attempting to download COVID-19 cases...")
    try:
        response = requests.get(url_cases)
        with open(os.path.join(path_to_stats, "covid-cases.csv"), 'wb') as f:
            f.write(response.content)
    except:
        traceback.print_exc()
        print("Failed to download COVID-19 cases.")
    else:
        print("Successful.")

    print("Attempting to download COVID-19 deaths...")
    try:
        response = requests.get(url_deaths)
        with open(os.path.join(path_to_stats, "covid-deaths.csv"), 'wb') as f:
            f.write(response.content)
    except:
        print("Failed to download COVID-19 deaths.")
    else:
        print("Successful.")

getStats()
