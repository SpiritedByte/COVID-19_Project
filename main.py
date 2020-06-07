# Import functions as modules from other .py files
from get_stats import getStats
from stats_parser import csv_parser
from make_graph import cases_plot # Need to make deaths plot too

# First, get latest stats using getStats()
getStats()

# Then, parse the data: we only need the rows with 'England', and the date and cumulative values
imported = csv_parser()
cases_filtered_import = imported[0]
deaths_filtered_import = imported[1]

# Finally, make the graph
cases_plot(cases_filtered_import)