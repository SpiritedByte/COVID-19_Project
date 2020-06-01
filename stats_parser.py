from csv import reader
import os
from pathlib import Path

def csv_parser():
    # Get abs path
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = Path("stats/")
    path_to_stats = cwd / path

    # Open files
    covid_case_file = path_to_stats / "covid-cases.csv"
    covid_death_file = path_to_stats / "covid-deaths.csv"

    #covid_case_list = csv.reader(open(covid_case_file, 'r'))
    #covid_death_list = csv.reader(open(covid_death_file, 'r'))

    # read csv file as a list of lists
    with open(covid_case_file, 'r') as case_read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(case_read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        
        new_covid_case_list = []
        for lst in list_of_rows:
            # print(row[0])
            if lst[0] == "England":
                new_covid_case_list.append(lst)
            else:
                pass
    
    with open(covid_death_file, 'r') as death_read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader_2 = reader(death_read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows_2 = list(csv_reader_2)
        
        new_covid_death_list = []
        for lst in list_of_rows_2:
            # print(row[0])
            if lst[0] == "England":
                new_covid_death_list.append(lst)
            else:
                pass
        print(new_covid_death_list)


csv_parser()
