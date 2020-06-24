import matplotlib.pyplot as plt

def plot(cases,deaths):
    #cases.plot(x='Specimen date',y='Cumulative lab-confirmed cases',color='green')
    #deaths.plot(x='Reporting date',y='Cumulative deaths',color='red')
    plt.figure("Cumulative deaths and cases")
    ax = plt.gca()
    cases.plot(kind='bar', x='Specimen date', y='Cumulative lab-confirmed cases',ax=ax, color='green')
    deaths.plot(kind='bar', x='Reporting date', y='Cumulative deaths', ax=ax, color='red')
    plt.show()