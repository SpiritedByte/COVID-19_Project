import requests
import os
import csv
import traceback
import sys

url_cases = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv'
url_deaths = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-deaths_latest.csv'

##################################

# create new folder to store the statistics
def getStats():
    cwd = os.getcwd()
    # print(cwd)
    if sys.platform.startswith('darwin') or sys.platform.startswith('linux2') or sys.platform.startswith('linux'):
        new_folder = os.path.join(cwd, 'stats')
        # print(new_folder)
        # os.path.join(cwd, r'/second_part')
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        else:
            pass
        
        print("Attempting to download COVID-19 cases...")
        try:
            response = requests.get(url_cases)
            with open(os.path.join("stats", "covid-cases.csv"), 'wb') as f:
                f.write(response.content)
        except:
            traceback.print_exc()
            print("Failed to download COVID-19 cases.")
        else:
            print("Successful.")

        print("Attempting to download COVID-19 deaths...")
        try:
            response = requests.get(url_deaths)
            with open(os.path.join("stats", "covid-deaths.csv"), 'wb') as f:
                f.write(response.content)
        except:
            print("Failed to download COVID-19 deaths.")
        else:
            print("Successful.")
        
    elif sys.platform.startswith('win32'):
        new_folder = os.path.join(cwd, 'stats')
        # print(new_folder)
        # os.path.join(cwd, '/stats')
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        else:
            pass

        print("Attempting to download COVID-19 cases...")
        try:
            response = requests.get(url_cases)
            with open(os.path.join("stats", "covid-cases.csv"), 'wb') as f:
                f.write(response.content)
        except:
            print("Failed to download COVID-19 cases.")
        else:
            print("Successful.")
        
        print("Attempting to download COVID-19 deaths...")
        try:
            response = requests.get(url_deaths)
            with open(os.path.join("stats", "covid-deaths.csv"), 'wb') as f:
                f.write(response.content)
        except:
            print("Failed to download COVID-19 deaths.")
        else:
            print("Successful.")

        
    else:
        print("Sorry, I don't know what your OS is :(")
        sys.exit()





