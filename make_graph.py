import matplotlib.pyplot as plt
import pandas as pd
from stats_parser import csv_parser

imported = csv_parser()
cases_filtered_import = imported[0]
deaths_filtered_import = imported[1]

def cases_plot(cases):
    plt.xlabel('Date')
    plt.ylabel('Cases')
    cases.plot(kind='scatter',x='Specimen date',y='Cumulative lab-confirmed cases',color='red')
    plt.show()