# Import modules
import os
import sys
from pathlib import Path
import pandas as pd
import requests
import traceback
from datetime import datetime
import matplotlib.pyplot as plt


# VARIABLES AND INITIALISATION
url_cases = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv'
url_deaths = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-deaths_latest.csv'


# FUNCTIONS
def bar_plot(cases=None, deaths=None, dataset=None, title="Plot"):

    # Validate dataset choice
    if dataset == "cumulative":
        y_values_cases = "Cumulative lab-confirmed cases"
        y_values_deaths = "Cumulative deaths"
    elif dataset == "daily":
        y_values_cases = "Daily lab-confirmed cases"
        y_values_deaths = "Daily change in deaths"
    else:
        print("[/] Unrecognised dataset '{}' (choose either 'daily' or 'cumulative')".format(dataset))
        sys.exit(1)

    # Initialise figure
    plt.figure(title, figsize=[12, 6])
    ax = plt.gca()

    # Plots
    cases.plot(
        kind='bar',
        x='Specimen date',
        y=y_values_cases,
        color='blue',
        ax=ax,
        sharex=True)
    deaths.plot(
        kind='bar',
        x='Reporting date',
        y=y_values_deaths,
        color='red',
        ax=ax)

    # Set title and auto-format dates
    plt.gcf().autofmt_xdate()
    ax.set_title(title)

    # Adjust size of subplots and rotate x-ticks
    plt.subplots_adjust(
        left=0.06,
        bottom=0.20,
        right=0.94,
        top=0.90)
    plt.show()


def getStats():
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = Path("stats/")
    path_to_stats = cwd / path

    print("[*] Checking if 'stats' folder is present...")
    if not os.path.exists(path_to_stats):
        print("[*] Does not exist. Creating 'stats' folder...")
        os.makedirs(path_to_stats)
    else:
        try:
            unix_datetime_cases = datetime.utcfromtimestamp(
                os.path.getmtime(os.path.join(
                    path_to_stats, "covid-cases.csv")))
            unix_datetime_deaths = datetime.utcfromtimestamp(os.path.getmtime(
                os.path.join(path_to_stats, "covid-deaths.csv")))
            print("[@] 'covid-cases.csv' last modified: {}".format(
                unix_datetime_cases))
            print("[@] 'covid-deaths.csv' last modified: {}".format(
                unix_datetime_deaths))

            if unix_datetime_cases.date() and unix_datetime_deaths.date() == datetime.today().date():
                print("[@] Local data is up-to-date. Skipping download.")
                return None
            else:
                pass
        except Exception:
            print("[/] It appears that the data has not been downloaded.")

    print("[*] Attempting to download COVID-19 cases...")
    try:
        response = requests.get(url_cases)
        with open(os.path.join(path_to_stats, "covid-cases.csv"), 'wb') as f:
            f.write(response.content)
    except Exception:
        traceback.print_exc()
        print("[/] Failed to download COVID-19 cases.")
    else:
        print("[@] Successfully downloaded COVID-19 cases!")

    print("[*] Attempting to download COVID-19 deaths...")
    try:
        response = requests.get(url_deaths)
        with open(os.path.join(path_to_stats, "covid-deaths.csv"), 'wb') as f:
            f.write(response.content)
    except Exception:
        print("[/] Failed to download COVID-19 deaths!")
    else:
        print("[@] Successfully downloaded COVID-19 deaths!")


def csv_parser():
    # Get abs path
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = Path("stats/")
    path_to_stats = cwd / path

    # Get path to files
    covid_case_file_path = path_to_stats / "covid-cases.csv"
    covid_death_file_path = path_to_stats / "covid-deaths.csv"

    # Read CSV files
    cases = pd.read_csv(covid_case_file_path)
    deaths = pd.read_csv(covid_death_file_path)

    # Get England data
    cases_filtered_england = cases.loc[cases['Area name'] == "England"]
    deaths_filtered_england = deaths.loc[deaths['Area name'] == "England"]

    # Sort by date
    cases_sorted = cases_filtered_england.sort_values(by='Specimen date')
    deaths_sorted = deaths_filtered_england.sort_values(by='Reporting date')

    # Return data from function
    return cases_sorted, deaths_sorted


# First, get latest stats using getStats()
getStats()

# Then, parse the data: we only need the dates and their corresponding values.
imported = csv_parser()
cases = imported[0]
deaths = imported[1]

# Finally, make the graph(s)
bar_plot(
    cases=cases,
    deaths=deaths,
    dataset="cumulative",
    title="Cumulative Cases and Deaths")
bar_plot(
    cases=cases,
    deaths=deaths,
    dataset="daily",
    title="Daily Cases and Deaths")
