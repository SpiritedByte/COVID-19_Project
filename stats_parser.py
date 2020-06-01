import csv
from pathlib import Path

def csv_parser():
    # Get abs path
    data_folder = Path("stats/")
    # print(str(data_folder))

    # Open files
    covid_case_file = data_folder / "covid-cases.csv"
    covid_death_file = data_folder / "covid-deaths.csv"

    with open(covid_case_file, 'rb') as c:
        pass

    with open(covid_death_file, 'rb') as d:
        pass

