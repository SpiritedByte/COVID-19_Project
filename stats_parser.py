from csv import reader
import os
from pathlib import Path
import pandas as pd

def csv_parser():
    # Get abs path
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = Path("stats/")
    path_to_stats = cwd / path

    # Open files
    covid_case_file_path = path_to_stats / "covid-cases.csv"
    covid_death_file_path = path_to_stats / "covid-deaths.csv"

    # open csv files
    cases = pd.read_csv(covid_case_file_path)
    deaths = pd.read_csv(covid_death_file_path)

    cases_filtered_england = cases.loc[cases['Area name'] == "England"]
    deaths_filtered_england = deaths.loc[deaths['Area name'] == "England"]

    cases_filtered_england = cases_filtered_england[['Specimen date', 'Cumulative lab-confirmed cases']]
    deaths_filtered_england = deaths_filtered_england[['Reporting date', 'Cumulative deaths']]

    cases_filtered_england = cases_filtered_england.sort_values(by = 'Specimen date')
    deaths_filtered_england = deaths_filtered_england.sort_values(by = 'Reporting date')

    return cases_filtered_england,deaths_filtered_england