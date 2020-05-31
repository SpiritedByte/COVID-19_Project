import requests
import os
import csv
import sys

url_cases = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv'
url_deaths = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-deaths_latest.csv'

##################################

# create new folder to store the statistics

cwd = os.getcwd()
# print(cwd)
if sys.platform.startswith('darwin') or sys.platform.startswith('linux2'):
    new_folder = os.path.join(cwd, 'stats')
    # print(new_folder)
    # os.path.join(cwd, r'/second_part')
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    else:
        pass
    
    print("Attempting to download COVID-19 cases...")
    try:
        r1 = requests.get(url_cases, allow_redirects=True)
        #open('covid-cases.csv', 'wb').write(r1.content)

        with open((new_folder + '/covid-cases.csv'), 'wb') as case:
            case.write(r1)
    except:
        print("Failed to download COVID-19 cases.")
    else:
        print("Successful.")

    print("Attempting to download COVID-19 deaths...")
    try:
        r2 = requests.get(url_deaths, allow_redirects=True)
        #open('covid-cases.csv', 'wb').write(r1.content)

        with open((new_folder + '/covid-deaths.csv'), 'wb') as death:
            death.write(r2)
    except:
        print("Failed to download COVID-19 cases.")
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
        r3 = requests.get(url_cases, allow_redirects=True)
        #open('covid-cases.csv', 'wb').write(r1.content)

        with open((new_folder + '\covid-cases.csv'), 'wb') as case:
            case.write(r3)
    except:
        print("Failed to download COVID-19 cases.")
    else:
        print("Successful.")
    
    print("Attempting to download COVID-19 deaths...")
    try:
        r4 = requests.get(url_deaths, allow_redirects=True)
        #open('covid-cases.csv', 'wb').write(r1.content)

        with open((new_folder + '\covid-deaths.csv'), 'wb') as deaths:
            deaths.write(r4)
    except:
        print("Failed to download COVID-19 deaths.")
    else:
        print("Successful.")

    
else:
    print("Sorry, I don't know what your OS is :(")
    sys.exit()



