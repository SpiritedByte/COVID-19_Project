import requests
import os
import traceback
import sys
from pathlib import Path
from datetime import datetime
import logging

# This script contains a function that will download the necessary .csv stats files

# [@] = user information
# [!] = query/condition
# [?] = user input or question
# [*] = action
# [/] = error

url_cases = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv'
url_deaths = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-deaths_latest.csv'
LOG_FILENAME = 'last_modified.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

##################################

# create new folder to store the statistics
def getStats():
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = Path("stats/")
    path_to_stats = cwd / path
    #print(path_to_stats)

    print("[!] Checking if 'stats' folder is present...")
    if not os.path.exists(path_to_stats):
        print("[*] Creating 'stats' folder...")
        os.makedirs(path_to_stats)
    else:
        try:
            unix_datetime_cases = datetime.utcfromtimestamp(os.path.getmtime(os.path.join(path_to_stats, "covid-cases.csv")))
            unix_datetime_deaths = datetime.utcfromtimestamp(os.path.getmtime(os.path.join(path_to_stats, "covid-deaths.csv")))
            print("[@] 'covid-cases.csv' last modified: {}".format(unix_datetime_cases))
            print("[@] 'covid-deaths.csv' last modified: {}".format(unix_datetime_deaths))
            logging.debug("[@] 'covid-cases.csv' last modified: {}".format(unix_datetime_cases))
            logging.debug("[@] 'covid-deaths.csv' last modified: {}".format(unix_datetime_deaths))
        except:
            print("[/] Hmm... I can't seem to find the CSV files required for this to function.")

    

    print("[*] Attempting to download COVID-19 cases...")
    try:
        response = requests.get(url_cases)
        with open(os.path.join(path_to_stats, "covid-cases.csv"), 'wb') as f:
            f.write(response.content)
    except:
        traceback.print_exc()
        print("[/] Failed to download COVID-19 cases.")
    else:
        print("[!] Successfully downloaded COVID-19 cases!")

    print("[*] Attempting to download COVID-19 deaths...")
    try:
        response = requests.get(url_deaths)
        with open(os.path.join(path_to_stats, "covid-deaths.csv"), 'wb') as f:
            f.write(response.content)
    except:
        print("[/] Failed to download COVID-19 deaths!")
    else:
        print("[!] Successfully downloaded COVID-19 deaths!")

getStats()